from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    #cadastrar
    path("cadastrar-receita/", cadastrar_receita, name="cadastrar_receita"),

    #listar
    path("listar-receita/", listar_receitas, name="listar_receitas"),
]
