from django.shortcuts import render, redirect
from cadastro.models import Receita
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    list_receitas = Receita.objects.all()

    context = {
        "nome_pagina": "Home",
        "list_receitas": list_receitas,
    }

    return render(request, "home/index.html")