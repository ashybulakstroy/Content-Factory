from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from content_factory.artifacts import ArtifactStore


def test_artifact_store_writes_manifest(tmp_path):
    store = ArtifactStore(output_dir=tmp_path / "artifacts")
    payload = {"title": "Gentle routine", "hook": "A small reset", "body": ["Breathe"], "cta": "Save this"}

    result = store.save_result(topic_id=7, payload=payload, output_path=tmp_path / "reel.png")

    manifest_path = tmp_path / "artifacts" / "topic_7_result.json"
    assert manifest_path.exists()
    assert result["topic_id"] == 7
    assert result["payload"]["title"] == "Gentle routine"
