from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from content_factory.video_renderer import VideoRenderer


def test_video_renderer_creates_mp4(tmp_path):
    renderer = VideoRenderer(output_dir=tmp_path)
    payload = {
        "title": "Calm evening",
        "hook": "A simple reset",
        "body": ["Take a breath", "Set one intention"],
        "cta": "Save this for later",
    }

    output_path = renderer.render_video(payload, output_path=tmp_path / "demo.mp4")

    assert output_path.exists()
    assert output_path.suffix == ".mp4"
