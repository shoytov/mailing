.PHONY: start stop tests
.SILENT: start stop tests

start:
	docker-compose up -d --build

stop:
	docker-compose down

tests:
	docker-compose run --rm app pytest --junitxml=test_results/results.xml -vv .
