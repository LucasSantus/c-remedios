from django.db.models import Prefetch
from usuarios.models import Estado, Cidade
import json
import requests
from django.db import connection, reset_queries
import time

"""
python manage.py shell
exec(open('apps/scripts/teste.py').read())
"""

start = time.time()

def print_list_obj(cidades, quantidade):
    for a in range(quantidade):
        for cidade in cidades:
            print(f"""
            descricao: {cidade.descricao}
            codigo_IBGE: {cidade.codigo_IBGE}
            data_registrado: {cidade.data_registrado}
            """)

def print_list(cidades, quantidade):
    for a in range(quantidade):
        for cidade in cidades:
            print(f"""
            descricao: {cidade['descricao']}
            codigo_IBGE: {cidade['codigo_IBGE']}
            estado: {cidade['estado']}
            data_registrado: {cidade['data_registrado']}
            """)

def cidades_obj_list():
    cidades_qs = Cidade.objects.all()

    return cidades_qs

def cidades_list():
    cidades_qs = Cidade.objects.select_related('estado').all()

    cidades = []
    for cidade in cidades_qs:
        estado = {
            "descricao": cidade.estado.descricao,
            "sigla": cidade.estado.sigla,
            "data_registrado": cidade.estado.data_registrado
        }
        cidades.append({
            "descricao": cidade.descricao,
            "codigo_IBGE": cidade.codigo_IBGE,
            "estado": estado,
            "data_registrado": cidade.data_registrado,
        })
    
    return cidades

print_list_obj(cidades_obj_list(), 15)
"""
Tempo percorrido: 6.625569820404053
Quantidade de consultas realizadas: 1
"""

# print_list(cidades_list(), 15)

end = time.time()

print(f"\nTempo percorrido: {end - start}")

print(f"\nQuantidade de consultas realizadas: {len(connection.queries)}")

reset_queries()