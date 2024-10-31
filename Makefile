build:
	docker compose build

run:
	HOST_UID=$(shell id -u) HOST_GID=$(shell id -g) docker compose run --rm \
		--entrypoint 'python src/run.py' \
		-w /home/qosf/work \
		notebooks

notebooks:
	HOST_UID=$(shell id -u) HOST_GID=$(shell id -g) docker compose up --remove-orphans

.PHONY: build run notebooks
