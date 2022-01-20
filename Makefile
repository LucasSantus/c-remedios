ENV = env
MANAGE = python manage.py

help: ## Help comand
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST); \

windows:
	python -m venv $(ENV); \
	$(ENV)\Scripts\activate; \

linux:
	python3 -m venv $(ENV); \
	. $(ENV)/bin/activate; \

update-pip:
	python -m pip install --upgrade pip; \
	pip install -r requirements.txt; \

run:
	$(MANAGE) runserver; \

migrate: ## Migrate Models
	$(MANAGE) makemigrations home; \
	$(MANAGE) makemigrations usuarios; \
	$(MANAGE) makemigrations receitas; \
	$(MANAGE) makemigrations vinculos; \
	$(MANAGE) makemigrations automated_logging; \
	$(MANAGE) migrate; \

i-linux: linux update-pip migrate run ## Install Project Linux
i-windows: windows update-pip migrate run ## Install Project Linux

il: i-linux ## Abreviation Install Linux
iw: i-windows ## Abreviation Install Windows

clean: ## Clean project
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "migrations" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f *.log
	@rm -rf $(ENV)
	@rm -rf db.sqlite3