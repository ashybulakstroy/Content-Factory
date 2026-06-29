from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from content_factory.pipeline import ContentPipeline


def test_pipeline_renders_safe_payload(tmp_path):
    pipeline = ContentPipeline(db_path=tmp_path / "content_factory.db", output_dir=tmp_path / "output")
    topic_id = pipeline.create_topic(
        title="Gentle routine",
        audience="women",
        objective="comfort",
        template="routine",
    )
    pipeline.enqueue_topic(topic_id)

    result = pipeline.process_topic(
        topic_id,
        {
            "title": "Gentle routine",
            "hook": "A calm reset for your morning",
            "body": ["Take a slow breath", "Set one simple intention"],
            "cta": "Save this for later",
        },
        output_path=tmp_path / "reel.png",
    )

    assert result["status"] == "rendered"
    assert Path(result["output_path"]).exists()

    pipeline.close()
