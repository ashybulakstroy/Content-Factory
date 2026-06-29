from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from content_factory.scheduler import Scheduler


def test_scheduler_runs_once_and_records_run(tmp_path):
    scheduler = Scheduler(output_dir=tmp_path)

    run_id = scheduler.run_once("demo")

    assert isinstance(run_id, str)
    assert (tmp_path / f"{run_id}.json").exists()
