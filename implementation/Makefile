setup:
	poetry install

develop:
	poetry run uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload --reload-dir src --no-access-log

test:
	poetry run pytest tests