from __future__ import annotations

from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont


class Renderer:
    def __init__(self, output_dir: str | Path | None = None) -> None:
        self.output_dir = Path(output_dir or "output")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def render_reel(self, payload: dict[str, Any], output_path: str | Path | None = None) -> Path:
        width, height = 1080, 1920
        image = Image.new("RGB", (width, height), color=(24, 24, 24))
        draw = ImageDraw.Draw(image)

        font = ImageFont.load_default()
        title = payload.get("title", "Untitled")
        hook = payload.get("hook", "")
        body = " ".join(payload.get("body", []))
        cta = payload.get("cta", "")

        draw.text((50, 80), title, fill=(255, 255, 255), font=font)
        draw.text((50, 220), hook, fill=(220, 220, 220), font=font)
        draw.text((50, 360), body, fill=(200, 200, 200), font=font)
        draw.text((50, 1700), cta, fill=(120, 230, 180), font=font)

        target_path = Path(output_path or self.output_dir / "reel.png")
        target_path.parent.mkdir(parents=True, exist_ok=True)
        image.save(target_path)
        return target_path
