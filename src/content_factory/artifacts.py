from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class ArtifactStore:
    def __init__(self, output_dir: str | Path | None = None) -> None:
        self.output_dir = Path(output_dir or "artifacts")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def save_result(self, topic_id: int, payload: dict[str, Any], output_path: str | Path) -> dict[str, Any]:
        result = {
            "topic_id": topic_id,
            "payload": payload,
            "output_path": str(output_path),
        }
        manifest_path = self.output_dir / f"topic_{topic_id}_result.json"
        manifest_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        return result
