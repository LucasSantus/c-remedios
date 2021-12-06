"""
python manage.py shell
exec(open('apps/scripts/main.py').read())
"""

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

# print("Testando ele ")

exec(open('apps/scripts/grupos/grupos.py').read())
exec(open('apps/scripts/cidades/cidades.py').read())