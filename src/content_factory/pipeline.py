from __future__ import annotations

from pathlib import Path
from typing import Any

from .artifacts import ArtifactStore
from .db import SQLiteStore
from .queue import QueueService
from .renderer import Renderer
from .safety import SafetyGate


class ContentPipeline:
    def __init__(self, db_path: str | Path | None = None, output_dir: str | Path | None = None) -> None:
        self.store = SQLiteStore(db_path)
        self.queue = QueueService(db_path)
        self.renderer = Renderer(output_dir)
        self.safety = SafetyGate()
        self.artifacts = ArtifactStore(output_dir)

    def create_topic(self, title: str, audience: str, objective: str, template: str) -> int:
        return self.store.create_topic(title, audience, objective, template)

    def enqueue_topic(self, topic_id: int) -> int:
        return self.queue.enqueue_topic(topic_id)

    def process_topic(self, topic_id: int, payload: dict[str, Any], output_path: str | Path | None = None) -> dict[str, Any]:
        safety_result = self.safety.evaluate(payload)
        if safety_result["status"] != "SAFE":
            self.queue.update_status(self.queue.list_pending()[0]["id"] if self.queue.list_pending() else 0, "blocked")
            return {"topic_id": topic_id, "status": safety_result["status"], "reason": safety_result["reason"]}

        output_path = self.renderer.render_reel(payload, output_path)
        self.artifacts.save_result(topic_id, payload, output_path)
        self.queue.update_status(self.queue.list_pending()[0]["id"] if self.queue.list_pending() else 0, "rendered")
        return {"topic_id": topic_id, "status": "rendered", "output_path": str(output_path)}

    def close(self) -> None:
        self.store.close()
        self.queue.close()
