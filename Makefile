.PHONY: install clean run

clean:
	find . -name '__pycache__' -type d -exec rm -rf {} +
	find . -name '*.pyc' -type f -exec rm -rf {} +

install:
	uv sync

run:
	uvicorn spotlight.api:app --port 5000 --reload

gradio:
	gradio app.py
