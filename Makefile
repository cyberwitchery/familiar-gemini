.PHONY: dev format lint test clean

dev:
	pip install -e ".[dev]"

format:
	ruff format .

lint:
	ruff format --check .
	ruff check .
	mypy src

test:
	pytest -q

clean:
	rm -rf build/ dist/ *.egg-info/ .pytest_cache/ .mypy_cache/ .ruff_cache/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
