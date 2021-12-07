ENV = env
MANAGE = python manage.py

help: ## Help comand
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install-windows: ## Install project windows
	python -m venv $(ENV); \
	$(ENV)\Scripts\activate; \
	build

install-linux: ## Install project linux
	python3 -m venv $(ENV); \
	. $(ENV)/bin/activate; \
	build

build: ## Build project
	python -m pip install --upgrade pip; \
	pip install -r requirements.txt; \
	$(MANAGE) makemigrations home; \
	$(MANAGE) makemigrations usuarios; \
	$(MANAGE) makemigrations receitas; \
	$(MANAGE) makemigrations automated_logging; \
	$(MANAGE) migrate; \
	$(MANAGE) runserver; \

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "migrations" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f *.log
	@rm -rf $(ENV)
	@rm -rf db.sqlite3