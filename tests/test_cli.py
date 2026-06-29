from pathlib import Path
import subprocess
import sys


def test_cli_runs(tmp_path):
    output = subprocess.run(
        [
            sys.executable,
            "main.py",
            "--db",
            str(tmp_path / "content_factory.db"),
            "--output",
            str(tmp_path / "output"),
        ],
        cwd=Path(__file__).resolve().parents[1],
        capture_output=True,
        text=True,
        check=True,
    )

    assert "topic_id" in output.stdout
    assert "rendered" in output.stdout
