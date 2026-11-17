"""Hybrid, cost-aware LLM router: local Ollama for cheap calls, Claude for hard ones.

Every module calls LLMs through `LLMRouter.complete()` so cost/latency are logged uniformly
and providers can be swapped or mocked in tests.
"""

from __future__ import annotations

import logging
import os
import time
from dataclasses import dataclass, field
from typing import Literal, Protocol

import httpx

log = logging.getLogger(__name__)

Tier = Literal["fast", "smart", "auto"]

# USD per 1M tokens (input, output). Update when pricing changes.
PRICING: dict[str, tuple[float, float]] = {"ollama": (0.0, 0.0), "claude": (3.0, 15.0)}


@dataclass
class LLMResponse:
    text: str
    provider: str
    model: str
    input_tokens: int = 0
    output_tokens: int = 0
    latency_s: float = 0.0

    @property
    def cost_usd(self) -> float:
        inp, out = PRICING.get(self.provider, (0.0, 0.0))
        return (self.input_tokens * inp + self.output_tokens * out) / 1_000_000


class Provider(Protocol):
    name: str
    model: str

    def complete(self, prompt: str, system: str | None, max_tokens: int) -> LLMResponse: ...


@dataclass
class OllamaProvider:
    model: str = field(default_factory=lambda: os.getenv("OLLAMA_MODEL", "llama3.2:3b"))
    host: str = field(default_factory=lambda: os.getenv("OLLAMA_HOST", "http://localhost:11434"))
    timeout: float = 120.0
    name: str = "ollama"

    def complete(self, prompt: str, system: str | None, max_tokens: int) -> LLMResponse:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "system": system or "",
            "stream": False,
            "options": {"num_predict": max_tokens},
        }
        r = httpx.post(f"{self.host}/api/generate", json=payload, timeout=self.timeout)
        r.raise_for_status()
        data = r.json()
        return LLMResponse(
            text=data.get("response", ""),
            provider=self.name,
            model=self.model,
            input_tokens=data.get("prompt_eval_count", 0),
            output_tokens=data.get("eval_count", 0),
        )


@dataclass
class ClaudeProvider:
    model: str = field(default_factory=lambda: os.getenv("CLAUDE_MODEL", "claude-sonnet-4-5"))
    name: str = "claude"

    def complete(self, prompt: str, system: str | None, max_tokens: int) -> LLMResponse:
        import anthropic  # lazy import keeps tests light

        client = anthropic.Anthropic()
        kwargs = {"system": system} if system else {}
        msg = client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}],
            **kwargs,
        )
        text = "".join(b.text for b in msg.content if getattr(b, "type", "") == "text")
        return LLMResponse(
            text=text,
            provider=self.name,
            model=self.model,
            input_tokens=msg.usage.input_tokens,
            output_tokens=msg.usage.output_tokens,
        )


@dataclass
class LLMRouter:
    fast: Provider = field(default_factory=OllamaProvider)
    smart: Provider = field(default_factory=ClaudeProvider)
    auto_threshold_chars: int = 4000
    hard_tags: frozenset[str] = frozenset({"reasoning", "planning", "code", "judge"})
    history: list[LLMResponse] = field(default_factory=list)

    def choose(self, prompt: str, tier: Tier, task: str | None = None) -> Provider:
        if tier == "fast":
            return self.fast
        if tier == "smart":
            return self.smart
        if (task and task in self.hard_tags) or len(prompt) > self.auto_threshold_chars:
            return self.smart
        return self.fast

    def complete(
        self,
        prompt: str,
        *,
        tier: Tier = "auto",
        task: str | None = None,
        system: str | None = None,
        max_tokens: int = 1024,
    ) -> LLMResponse:
        provider = self.choose(prompt, tier, task)
        start = time.perf_counter()
        try:
            resp = provider.complete(prompt, system, max_tokens)
        except Exception as exc:  # noqa: BLE001 - fall back on any local failure
            if provider is self.smart:
                raise
            log.warning("fast provider failed (%s); falling back to smart", exc)
            provider = self.smart
            resp = provider.complete(prompt, system, max_tokens)
        resp.latency_s = time.perf_counter() - start
        self.history.append(resp)
        log.info("llm call provider=%s model=%s cost=$%.5f", resp.provider, resp.model, resp.cost_usd)
        return resp

    @property
    def total_cost_usd(self) -> float:
        return sum(r.cost_usd for r in self.history)
