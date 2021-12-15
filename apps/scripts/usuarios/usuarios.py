from usuarios.models import Usuario, Cidade
from django.contrib.auth.models import Group
import datetime, json, random
from django.db import connection, reset_queries
import time
from project.settings import capitalize_name

"""
python manage.py shell
exec(open('apps/scripts/usuarios/usuarios.py').read())
"""

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

def registrar_usuarios():
    start = time.time()

    with open("apps/scripts/usuarios/usuarios.json") as json_file:
        list_usuarios_json = json.load(json_file)
        json_file.close()

    print(BOLD + "\n--------------------------------------------------" + RESET)
    print(BOLD + "\nFoi iniciado a geração de registros dos usuários padrões!\n" + RESET)
    print(BOLD + "--------------------------------------------------\n" + RESET)

    list_obj_usuarios = [] # Lista para armazenar os usuarios como objeto.
    list_usuarios = [] # Lista para armazenar os usuarios.

    list_usuarios_email = [ obj.email for obj in Usuario.objects.all() ] # Lista para armazenar todas os e-mails de todos os usuários.

    cidade = Cidade.objects.get(descricao = "Três Corações")
    date_nasc = datetime.datetime.now()

    paciente = Group.objects.get(name = 'Paciente')

    contador = 0

    for usuario in list_usuarios_json:
        nome = ' '.join(usuario['nome'].split()[:1])
        sobrenome = ' '.join(usuario['nome'].split()[2:])

        bairro = usuario['endereco']['logradouro'].split()[0]
        logradouro = ' '.join(usuario['endereco']['logradouro'].split()[1:])

        obj_usuario = Usuario(
            nome = capitalize_name(nome), 
            sobrenome = capitalize_name(sobrenome), 
            password = "pbkdf2_sha256$260000$BpWOEBnkT0ENdZdAg7NNxg$VGxS0Ijjv5z+KmatU6E2vCSf49+QG/zPxOIYJEQbtcw=", 
            genero = usuario['sexo'], 
            cpf = usuario['documentos']['cpf'], 
            email = usuario['email'], 
            cidade = cidade, 
            bairro = capitalize_name(bairro), 
            logradouro = capitalize_name(logradouro), 
            cep = usuario['endereco']['cep'].replace(".", ""), 
            complemento = capitalize_name("Casa"), 
            dataNascimento = date_nasc, 
            numeroResidencial = random.randint(1, 900), 
            telefone = usuario['telefone'].replace(')', ') '), 
            idGroup = paciente.id,
            is_active = True, 
            is_superuser = False
        )
        list_obj_usuarios.append(obj_usuario)
        contador += 1

    for usuario in list_obj_usuarios:
        if not usuario.email in list_usuarios_email:
            list_usuarios.append(usuario)

    if list_usuarios:
        Usuario.objects.bulk_create(list_usuarios)

    list_usuarios = Usuario.objects.prefetch_related('groups').all()
   
    for usuario in list_usuarios:
        usuario.groups.add(paciente)

    end = time.time()

    print(end - start)

    print(len(connection.queries))

    reset_queries()

registrar_usuarios()