from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class Scheduler:
    def __init__(self, output_dir: str | Path | None = None) -> None:
        self.output_dir = Path(output_dir or "output")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def run_once(self, job_name: str) -> str:
        run_id = f"{job_name}_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}" 
        payload = {
            "job_name": job_name,
            "started_at": datetime.now(timezone.utc).isoformat(),
            "status": "scheduled",
        }
        manifest_path = self.output_dir / f"{run_id}.json"
        manifest_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        return run_id
