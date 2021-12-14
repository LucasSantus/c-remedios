ENV = env
MANAGE = python manage.py

help: ## Help comand
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST); \

active-windows:
	$(ENV)\Scripts\activate; \

active-linux:
	. $(ENV)/bin/activate; \

windows:
	python -m venv $(ENV); \
	$(ENV)\Scripts\activate; \

linux:
	python3 -m venv $(ENV); \
	. $(ENV)/bin/activate; \

update-pip:
	python -m pip install --upgrade pip; \
	pip install -r requirements.txt; \

runserver:
	$(MANAGE) runserver; \

migrate: ## Migrate Models
	$(MANAGE) makemigrations home; \
	$(MANAGE) makemigrations usuarios; \
	$(MANAGE) makemigrations receitas; \
	$(MANAGE) makemigrations automated_logging; \
	$(MANAGE) migrate; \

i-linux: linux update-pip migrate runserver ## Install Project Linux
i-windows: windows update-pip migrate runserver ## Install Project Linux

r-linux: active-linux runserver ## Run Project Linux
r-windows: active-windows runserver ## Run Project Windows

il: i-linux ## Abreviation Install Linux
iw: i-windows ## Abreviation Install Windows

rl: r-linux ## Abreviation Run Linux
rw: r-windows ## Abreviation Run Windows

clean: ## Clean project
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "migrations" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f *.log
	@rm -rf $(ENV)
	@rm -rf db.sqlite3