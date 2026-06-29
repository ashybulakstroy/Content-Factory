from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from content_factory.llm_router_new import LLMRouter


def test_llm_router_falls_back_without_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    router = LLMRouter(api_key=None)
    payload = router.generate_content("A calm routine")

    assert payload["title"] == "Fallback topic"
    assert payload["body"] == ["A calm routine"]
