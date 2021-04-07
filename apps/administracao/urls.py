from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    #cadastrar
    path("cadastrar-agendamento/", cadastrar_agendamento, name="cadastrar_agendamento"),
    path("cadastrar-horario/", cadastrar_horario_agendamento, name="cadastrar_horario"),
]
