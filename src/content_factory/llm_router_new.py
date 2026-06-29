from __future__ import annotations

import json
import os
from typing import Any

from openai import OpenAI


class LLMRouter:
    def __init__(self, api_key: str | None = None, base_url: str | None = None, model: str | None = None) -> None:
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.base_url = base_url
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        self.client = None
        if self.api_key:
            self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

    def generate_content(self, prompt: str) -> dict[str, Any]:
        if not self.client:
            return {
                "title": "Fallback topic",
                "hook": "A calm reset for your audience",
                "body": [prompt],
                "cta": "Save this for later",
            }

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
            text={
                "format": {
                    "type": "json_schema",
                    "name": "reel_payload",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "title": {"type": "string"},
                            "hook": {"type": "string"},
                            "body": {"type": "array", "items": {"type": "string"}},
                            "cta": {"type": "string"},
                        },
                        "required": ["title", "hook", "body", "cta"],
                        "additionalProperties": False,
                    },
                }
            },
        )

        if hasattr(response, "output_parsed") and response.output_parsed is not None:
            return response.output_parsed

        if getattr(response, "output_text", None):
            return json.loads(response.output_text)

        return {
            "title": "Fallback topic",
            "hook": "A calm reset for your audience",
            "body": [prompt],
            "cta": "Save this for later",
        }
