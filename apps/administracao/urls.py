from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    #cadastrar
    path("cadastrar-receita/", cadastrar_receita, name="cadastrar_receita"),
    path("cadastrar-agendamento/", cadastrar_agendamento, name="cadastrar_agendamento"),
    path("cadastrar-horario/", cadastrar_horario_agendamento, name="cadastrar_horario"),

    #listar
    path("listar-receita/", listar_receitas, name="listar_receitas"),
]
