from dataclasses import dataclass

import pytest

from shared.llm.router import LLMResponse, LLMRouter


@dataclass
class FakeProvider:
    name: str
    model: str = "fake"
    fail: bool = False
    calls: int = 0

    def complete(self, prompt, system, max_tokens):
        self.calls += 1
        if self.fail:
            raise ConnectionError("down")
        return LLMResponse(
            text=f"{self.name}:{prompt}",
            provider=self.name,
            model=self.model,
            input_tokens=1000,
            output_tokens=1000,
        )


def make(fail_fast=False):
    return LLMRouter(fast=FakeProvider("ollama", fail=fail_fast), smart=FakeProvider("claude"))


def test_fast_tier_uses_local():
    r = make()
    assert r.complete("hi", tier="fast").provider == "ollama"


def test_auto_routes_hard_tasks_to_claude():
    r = make()
    assert r.complete("plan this", task="planning").provider == "claude"
    assert r.complete("x" * 5000).provider == "claude"
    assert r.complete("short").provider == "ollama"


def test_fallback_when_local_fails():
    r = make(fail_fast=True)
    resp = r.complete("hi", tier="fast")
    assert resp.provider == "claude"


def test_smart_failure_is_raised():
    r = LLMRouter(fast=FakeProvider("ollama"), smart=FakeProvider("claude", fail=True))
    with pytest.raises(ConnectionError):
        r.complete("hi", tier="smart")


def test_cost_tracking():
    r = make()
    r.complete("a", tier="fast")
    r.complete("b", tier="smart")
    assert r.total_cost_usd == pytest.approx(0.018)
