# Content Factory

Content Factory — это локальный прототип для генерации идей для Instagram Reels и сохранения их в виде артефактов без использования официального API Instagram. Проект объединяет генерацию контента, проверку безопасности, рендеринг, очередь задач, планирование и шаг публикации в простой пайплайн на Python.

## Обзор
Этот репозиторий содержит лёгкий конвейер для создания коротких социальных концептов. Проект подходит для локальных экспериментов и может быть расширен до полноценной интеграции с реальной публикацией позже.

## Возможности
- Генерация структурированных концептов Reel по промпту
- Базовая проверка безопасности перед принятием контента
- Создание placeholder-изображений и видео-артефактов
- Хранение очереди задач и обработанных тем в SQLite
- Сохранение истории запусков и результатов публикации

## Структура проекта
- [main.py](main.py) — точка входа CLI
- [src/content_factory/pipeline.py](src/content_factory/pipeline.py) — слой оркестрации
- [src/content_factory/llm_router_new.py](src/content_factory/llm_router_new.py) — маршрутизатор генерации контента
- [src/content_factory/safety.py](src/content_factory/safety.py) — проверки безопасности
- [src/content_factory/renderer.py](src/content_factory/renderer.py) — рендеринг изображений
- [src/content_factory/video_renderer.py](src/content_factory/video_renderer.py) — рендеринг видео
- [src/content_factory/queue.py](src/content_factory/queue.py) — управление очередью
- [src/content_factory/scheduler.py](src/content_factory/scheduler.py) — история запусков
- [src/content_factory/publisher.py](src/content_factory/publisher.py) — заглушка шага публикации

## Быстрый старт
1. Создайте и активируйте виртуальное окружение
   - Windows: `.venv\Scripts\python -m venv .venv`
   - Активация: `.venv\Scripts\Activate.ps1`
2. Установите зависимости
   - `pip install -r requirements.txt`
3. Запустите CLI
   - `python main.py --title "Gentle evening routine" --audience women --objective comfort --template routine`
4. Запустите тесты
   - `pytest -q`

## Примечание
Текущий модуль публикации сохраняет результат публикации и манифест артефакта. Реальная публикация в Instagram пока не реализована.
