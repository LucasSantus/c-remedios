from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # REGISTRAR
    path("receita/registrar/", registrar_receita, name="registrar_receita"),
    path("remedio/registrar/", registrar_remedio, name="registrar_remedio"),

    # EDITAR
    # path("receita/editar/<int:id_receita>/", editar_receita, name="editar_receita"),
    # path("remedio/editar/<int:id_remedio>/", editar_remedio, name="editar_remedio"),

    # DELETAR
    # path("receita/deletar/<int:id_receita>/", deletar_receita, name="deletar_receita"),
    # path("remedio/deletar/<int:id_remedio>/", deletar_remedio, name="deletar_remedio"),
    
    # LISTAR
    path("remedios/listar/", listar_remedios, name="listar_remedios"),
]
