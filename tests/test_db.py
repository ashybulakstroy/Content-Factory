from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from content_factory.db import SQLiteStore


def test_store_creates_schema_and_persists_topic(tmp_path):
    db_path = tmp_path / "content_factory.db"
    store = SQLiteStore(db_path)

    topic_id = store.create_topic(
        title="Morning calm",
        audience="women",
        objective="comfort",
        template="tips",
    )

    topic = store.get_topic(topic_id)

    assert topic is not None
    assert topic["title"] == "Morning calm"
    assert topic["audience"] == "women"
    assert topic["objective"] == "comfort"
    assert topic["template"] == "tips"
    assert topic["status"] == "planned"
