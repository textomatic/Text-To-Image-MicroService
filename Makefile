setup:
	pip install --upgrade pip
	pip install -r requirements.txt

format:
	black app/*.py
	black tests/*.py

lint:
	pylint --disable=R,C app/main.py

test:
	python -m pytest -vv --cov=app tests/test_main.py

all: setup format lint test