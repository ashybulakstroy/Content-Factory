from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from content_factory.publisher import Publisher


def test_publisher_records_publish_result(tmp_path):
    publisher = Publisher(output_dir=tmp_path)
    result = publisher.publish("demo.mp4", "demo")

    assert result["status"] == "queued"
    assert result["artifact"] == "demo.mp4"
    assert (tmp_path / "publish_result.json").exists()
