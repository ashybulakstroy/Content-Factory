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


def test_llm_router_uses_next_provider_when_first_fails(monkeypatch):
    class FakeClient:
        def __init__(self, responses):
            self.responses = responses

    class FakeResponse:
        def __init__(self, payload):
            self.output_parsed = payload
            self.output_text = None

    class FakeProvider:
        def __init__(self, payload):
            self.payload = payload

        def responses(self):
            return self

        def create(self, **kwargs):
            return FakeResponse(self.payload)

    providers = [
        lambda: (_ for _ in ()).throw(RuntimeError("boom")),
        lambda: FakeProvider({"title": "Second provider", "hook": "Fallback worked", "body": ["ok"], "cta": "Save"}),
    ]

    router = LLMRouter(api_key="fake")
    router.providers = providers
    payload = router.generate_content("A calm routine")

    assert payload["title"] == "Second provider"
    assert payload["hook"] == "Fallback worked"
