# Content Factory

Content Factory is a local prototype for generating Instagram Reel concepts and saving them as renderable artifacts without relying on the official Instagram API. The project combines content generation, safety checks, rendering, queueing, scheduling, and a publish step into a simple Python pipeline.

## English

### Overview
This repository contains a lightweight content pipeline for creating short-form social media concepts. It is designed for local experimentation and can be extended with a real publishing integration later.

### Main features
- Generate structured reel concepts from a prompt
- Apply a basic safety gate before accepting content
- Render placeholder images and video artifacts
- Track queued work and processed topics in SQLite
- Record run history and publish results

### Project structure
- [main.py](main.py) — CLI entry point
- [src/content_factory/pipeline.py](src/content_factory/pipeline.py) — orchestration layer
- [src/content_factory/llm_router_new.py](src/content_factory/llm_router_new.py) — content generation router
- [src/content_factory/safety.py](src/content_factory/safety.py) — safety checks
- [src/content_factory/renderer.py](src/content_factory/renderer.py) — image rendering
- [src/content_factory/video_renderer.py](src/content_factory/video_renderer.py) — video rendering
- [src/content_factory/queue.py](src/content_factory/queue.py) — queue management
- [src/content_factory/scheduler.py](src/content_factory/scheduler.py) — run history
- [src/content_factory/publisher.py](src/content_factory/publisher.py) — publish step stub

### Quick start
1. Create and activate a virtual environment
   - Windows: `.venv\Scripts\python -m venv .venv`
   - Activate: `.venv\Scripts\Activate.ps1`
2. Install dependencies
   - `pip install -r requirements.txt`
3. Run the CLI
   - `python main.py --title "Gentle evening routine" --audience women --objective comfort --template routine`
4. Run tests
   - `pytest -q`

### Notes
The current publisher module records a publish result and artifact manifest. It does not yet perform a real Instagram post.

## Русский

Подробная версия документации доступна в [README.ru.md](README.ru.md).
