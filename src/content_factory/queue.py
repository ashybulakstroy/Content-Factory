from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any


class QueueService:
    def __init__(self, db_path: str | Path | None = None) -> None:
        self.db_path = Path(db_path or "content_factory.db")
        self._connect()
        self._initialize_schema()

    def _connect(self) -> None:
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

    def _initialize_schema(self) -> None:
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS queue_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic_id INTEGER NOT NULL,
                status TEXT NOT NULL DEFAULT 'queued',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        self.conn.commit()

    def enqueue_topic(self, topic_id: int) -> int:
        cursor = self.conn.execute(
            "INSERT INTO queue_items (topic_id, status) VALUES (?, ?)",
            (topic_id, "queued"),
        )
        self.conn.commit()
        return int(cursor.lastrowid)

    def list_pending(self) -> list[dict[str, Any]]:
        rows = self.conn.execute(
            "SELECT id, topic_id, status, created_at, updated_at FROM queue_items WHERE status = 'queued' ORDER BY id"
        ).fetchall()
        return [dict(row) for row in rows]

    def get_by_id(self, item_id: int) -> dict[str, Any] | None:
        row = self.conn.execute(
            "SELECT id, topic_id, status, created_at, updated_at FROM queue_items WHERE id = ?",
            (item_id,),
        ).fetchone()
        if row is None:
            return None
        return dict(row)

    def update_status(self, item_id: int, status: str) -> None:
        self.conn.execute(
            "UPDATE queue_items SET status = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
            (status, item_id),
        )
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()
