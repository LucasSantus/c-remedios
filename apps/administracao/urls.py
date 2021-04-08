from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    #cadastrar
    path('dosagens-usuario/<int:id_receita>/', dosagem_usuario, name="dosagem_usuario"),
    path('configurar-horarios-dosagens/<int:id_receita>', configura_horario_dosagem, name="configura_horario_dosagem"),
]
