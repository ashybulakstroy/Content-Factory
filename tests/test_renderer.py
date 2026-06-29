from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from content_factory.renderer import Renderer


def test_renderer_creates_image_file(tmp_path):
    renderer = Renderer(output_dir=tmp_path)
    payload = {
        "title": "Calm habits",
        "hook": "Small changes matter",
        "body": ["Take one quiet breath", "Set a simple boundary"],
        "cta": "Save this for later",
    }

    output_path = renderer.render_reel(payload, tmp_path / "reel.png")

    assert output_path.exists()
    assert output_path.suffix == ".png"
