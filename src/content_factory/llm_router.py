from __future__ import annotations

import os
from typing import Any

from openai import OpenAI


class LLMRouter:
    def __init__(self, api_key: str | None = None, base_url: str | None = None, model: str | None = None) -> None:
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"), base_url=base_url)
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def generate_content(self, prompt: str) -> dict[str, Any]:
        response = self.client.responses.create(
            model=self.model,
            input=[
                {
                    "role": "system",
                    "content": "You create short, safe, non-diagnostic Instagram reel content in strict JSON.",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            text={"format": {"type": "json_schema", "name": "reel_payload", "schema": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "hook": {"type": "string"},
                    "body": {"type": "array", "items": {"type": "string"}},
                    "cta": {"type": "string"},
                },
                "required": ["title", "hook", "body", "cta"],
                "additionalProperties": False,
            }}},
        )
        return response.output_parsed
