from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    #cadastrar
    path("cadastrar-receita/", cadastrar_receita, name="cadastrar_receita"),
    path("cadastrar-pessoa/", cadastrar_pessoa, name="cadastrar_pessoa"),
    path("cadastrar-remedio/", cadastrar_remedio, name="cadastrar_remedio"),
    
    #listar
    path("listar-pessoas/", listar_pessoas, name="listar_pessoas"),
    path("listar-remedios/", listar_remedios, name="listar_remedios"),
]
