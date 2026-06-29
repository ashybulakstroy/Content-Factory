from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any


class SQLiteStore:
    def __init__(self, db_path: str | Path | None = None) -> None:
        self.db_path = Path(db_path or "content_factory.db")
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._connect()
        self._initialize_schema()

    def _connect(self) -> None:
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

    def _initialize_schema(self) -> None:
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS topics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                audience TEXT NOT NULL,
                objective TEXT NOT NULL,
                template TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'planned',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        self.conn.commit()

    def create_topic(
        self,
        title: str,
        audience: str,
        objective: str,
        template: str,
        status: str = "planned",
    ) -> int:
        cursor = self.conn.execute(
            """
            INSERT INTO topics (title, audience, objective, template, status)
            VALUES (?, ?, ?, ?, ?)
            """,
            (title, audience, objective, template, status),
        )
        self.conn.commit()
        return int(cursor.lastrowid)

    def get_topic(self, topic_id: int) -> dict[str, Any] | None:
        row = self.conn.execute(
            "SELECT id, title, audience, objective, template, status, created_at FROM topics WHERE id = ?",
            (topic_id,),
        ).fetchone()
        if row is None:
            return None
        return dict(row)

    def close(self) -> None:
        self.conn.close()
