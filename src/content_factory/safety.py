from __future__ import annotations

from typing import Any


class SafetyGate:
    def __init__(self) -> None:
        self.blocked_terms = [
            "diagnosis",
            "treat",
            "treatment",
            "suicide",
            "self-harm",
            "panic attack",
            "medication",
        ]

    def evaluate(self, payload: dict[str, Any]) -> dict[str, Any]:
        text_parts = [
            str(payload.get("title", "")),
            str(payload.get("hook", "")),
            *[str(item) for item in payload.get("body", [])],
            str(payload.get("cta", "")),
        ]
        text = " ".join(text_parts).lower()
        for term in self.blocked_terms:
            if term in text:
                return {"status": "REJECTED", "reason": f"blocked term: {term}"}
        return {"status": "SAFE", "reason": "passed basic safety checks"}
