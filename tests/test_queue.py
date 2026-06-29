from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from content_factory.db import SQLiteStore
from content_factory.queue import QueueService


def test_queue_service_enqueues_and_updates_status(tmp_path):
    db_path = tmp_path / "content_factory.db"
    store = SQLiteStore(db_path)
    queue = QueueService(db_path)

    topic_id = store.create_topic(
        title="Evening reset",
        audience="women",
        objective="calm",
        template="routine",
    )

    item_id = queue.enqueue_topic(topic_id)
    pending = queue.list_pending()

    assert len(pending) == 1
    assert pending[0]["topic_id"] == topic_id
    assert pending[0]["status"] == "queued"

    queue.update_status(item_id, "processing")
    queued_item = queue.get_by_id(item_id)

    assert queued_item is not None
    assert queued_item["status"] == "processing"
