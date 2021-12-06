ENV = env
MANAGE = python manage.py

help: ## Help comand
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build: ## Build project
	python3 -m venv $(ENV); \
	. $(ENV)/bin/activate; \
	python -m pip install --upgrade pip; \
	pip install -r requirements.txt; \
	$(MANAGE) makemigrations home; \
	$(MANAGE) makemigrations usuarios; \
	$(MANAGE) makemigrations receitas; \
	$(MANAGE) makemigrations automated_logging; \
	$(MANAGE) migrate; \

script: ## Run script's
	ls
	. $(ENV)/bin/activate; \
	cd apps/scripts; \
	python3 main.py; \

script2: ## Run script's
	. $(ENV)/bin/activate; \
	python manage.py shell; \
	open('apps/scripts/main.py').read()

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "migrations" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f *.log
	@rm -rf $(ENV)
	@rm -rf db.sqlite3