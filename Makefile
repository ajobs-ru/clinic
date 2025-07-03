.PHONY: lint test

lint:
	docker compose run --rm clinic flake8

test:
	docker compose run --rm clinic pytest

up:
	docker compose up -d --build

down:
	docker compose down
