from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from content_factory.safety import SafetyGate


def test_safety_gate_rejects_blocked_content():
    gate = SafetyGate()
    payload = {
        "title": "How to treat anxiety",
        "hook": "Need a quick fix",
        "body": ["Try this method"],
        "cta": "DM me",
    }
    result = gate.evaluate(payload)
    assert result["status"] == "REJECTED"
    assert "blocked term" in result["reason"]


def test_safety_gate_accepts_safe_content():
    gate = SafetyGate()
    payload = {
        "title": "Gentle evening routine",
        "hook": "A calm reset for your night",
        "body": ["Take a slow breath", "Put your phone away"],
        "cta": "Save this for later",
    }
    result = gate.evaluate(payload)
    assert result["status"] == "SAFE"
