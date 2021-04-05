from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    #cadastrar
    path("cadastrar-pessoa/", cadastrar_pessoa, name="cadastrar_pessoa"),
    
    #listar
    path("listar-pessoas/", listar_pessoas, name="listar_pessoas"),
]
