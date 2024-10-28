build:
	# docker compose build --build-arg HOST_UID=$(shell id -u) --build-arg HOST_GID=$(shell id -g) --build-arg HOST_UNAME=$(shell whoami) 
	docker compose build
run:

	HOST_UID=$(shell id -u) HOST_GID=$(shell id -g) docker compose run

notebooks:
	HOST_UID=$(shell id -u) HOST_GID=$(shell id -g) docker compose run --rm notebooks
	
