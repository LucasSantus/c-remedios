from usuarios.models import Estado, Cidade
import json
import requests
from django.db import connection, reset_queries
import time

"""
python manage.py shell
exec(open('apps/scripts/cidades/cidades.py').read())
"""

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

start = time.time()

with open("apps/scripts/cidades/estados.json") as json_file:
    list_estados_json = json.load(json_file)
    json_file.close()

print(BOLD + "\n--------------------------------------------------" + RESET)
print(BOLD + "\nFoi iniciado a geração de registros dos estados e cidades!\n" + RESET)
print(BOLD + "--------------------------------------------------\n" + RESET)

list_obj_estados = [] # Lista para armazenar os estados como objeto.
list_obj_cidades = [] # Lista para armazenar as cidades como objeto.
list_estados = [] # Lista para armazenar os estados.
list_cidades = [] # Lista para armazenar as cidades.
list_estados_siglas = [ obj.sigla for obj in Estado.objects.all() ] # Lista para armazenar todas as siglas de todos os estados.
list_cidades_IBGE = [ str(obj.codigo_IBGE) for obj in Cidade.objects.all() ] # Lista para armazenar todas as siglas de todos os estados.

for estado in list_estados_json:
    obj_estado = Estado(descricao = estado['name'], sigla = estado['uf'])
    list_obj_estados.append(obj_estado)

for estado in list_obj_estados:
    if not estado.sigla in list_estados_siglas:
        list_estados.append(estado)

if list_estados:
    Estado.objects.bulk_create(list_estados)

list_estados = Estado.objects.all()

for estado in list_estados:
    try:
        req = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado.sigla}/municipios")
        list_cidades_json = json.loads(req.text)

        for cidade in list_cidades_json:
            obj_cidade = Cidade(descricao = cidade['nome'], codigo_IBGE = cidade['id'], estado = estado)
            list_obj_cidades.append(obj_cidade)
    except:
        pass

list_cidades = []

for cidade in list_obj_cidades:
    if not cidade.codigo_IBGE in list_cidades_IBGE:
        list_cidades.append(cidade)
if list_cidades:  
    Cidade.objects.bulk_create(list_cidades)

end = time.time()

print(end - start)

print(len(connection.queries))

reset_queries()
