from __future__ import annotations

import argparse
from pathlib import Path

from src.content_factory.pipeline import ContentPipeline
from src.content_factory.llm_router_new import LLMRouter


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the content factory pipeline")
    parser.add_argument("--db", default="content_factory.db")
    parser.add_argument("--output", default="output")
    parser.add_argument("--title", default="Gentle evening routine")
    parser.add_argument("--audience", default="women")
    parser.add_argument("--objective", default="comfort")
    parser.add_argument("--template", default="routine")
    parser.add_argument("--prompt", default="Create a calm, safe, short Instagram reel concept")
    args = parser.parse_args()

    router = LLMRouter()
    payload = router.generate_content(args.prompt)

    pipeline = ContentPipeline(db_path=args.db, output_dir=args.output)
    try:
        topic_id = pipeline.create_topic(
            title=args.title,
            audience=args.audience,
            objective=args.objective,
            template=args.template,
        )
        pipeline.enqueue_topic(topic_id)
        result = pipeline.process_topic(
            topic_id,
            {
                **payload,
                "title": payload.get("title", args.title),
                "hook": payload.get("hook", "A calm reset for your audience"),
                "body": payload.get("body", [args.prompt]),
                "cta": payload.get("cta", "Save this for later"),
            },
            output_path=Path(args.output) / "reel.png",
        )
        print({"topic_id": topic_id, **result})
    finally:
        pipeline.close()


if __name__ == "__main__":
    main()
