.PHONY: lint test

lint:
	docker compose run --rm clinic flake8

test:
	docker compose run --rm clinic pytest
