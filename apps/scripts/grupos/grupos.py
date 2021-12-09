from django.contrib.auth.models import Group

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

"""
python manage.py shell
exec(open('apps/scripts/grupos/grupos.py').read())
"""

def registrar_grupos():
    groups = Group.objects.all()
    list_groups = ["Paciente", "Medico"]
    list_obj_groups = []

    print(BOLD + "\n-----------------------------------------------" + RESET)
    print(BOLD + "\nFoi iniciado a geração de registros dos grupos!\n" + RESET)
    print(BOLD + "-----------------------------------------------\n" + RESET)

    for group in list_groups:
        if not group in groups:
            obj_group = Group(name = group)
            list_obj_groups.append(obj_group)
        else:
            print(RED + "O grupo" + RESET + BOLD + f" {group} " + RESET + RED + "já está registrado no sistema!" + RESET)
    if list_obj_groups:
        Group.objects.bulk_create(list_obj_groups)

registrar_grupos()