from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # RECEITA
    path("receita/registrar/<int:id_medico_paciente>", registrar_receita, name="registrar_receita"),
    path("receita/detalhe/agendamento/<int:id_receitaMedicoPaciente>", detalhe_receita_paciente, name="detalhe_receita_paciente"),

    # REMÉDIO
    path("remedio/registrar/", registrar_remedio, name="registrar_remedio"),
    path("remedios/listar/", listar_remedios, name="listar_remedios"),

    # PACIENTE
    path('paciente/registrar/', registrar_paciente, name="registrar_paciente"),

    # LISTAR
    path("receita/listar/<int:id_medico_paciente>", listar_receitas, name="listar_receitas"),

    path('dosagens-usuario/<int:id_receita>/', dosagem_usuario, name="dosagem_usuario"),
    path('configurar-horarios-dosagens/<int:id_receita>', configura_horario_dosagem, name="configura_horario_dosagem"),

    # EDITAR
    # path("receita/editar/<int:id_receita>/", editar_receita, name="editar_receita"),
    # path("remedio/editar/<int:id_remedio>/", editar_remedio, name="editar_remedio"),

    # DELETAR
    # path("receita/deletar/<int:id_receita>/", deletar_receita, name="deletar_receita"),
    # path("remedio/deletar/<int:id_remedio>/", deletar_remedio, name="deletar_remedio"),
]