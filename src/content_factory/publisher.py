from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class Publisher:
    def __init__(self, output_dir: str | Path | None = None) -> None:
        self.output_dir = Path(output_dir or "output")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def publish(self, artifact_path: str | Path, caption: str) -> dict[str, Any]:
        result = {
            "status": "queued",
            "artifact": str(artifact_path),
            "caption": caption,
        }
        manifest_path = self.output_dir / "publish_result.json"
        manifest_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        return result
