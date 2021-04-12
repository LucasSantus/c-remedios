from django.shortcuts import render, redirect
from cadastro.models import Receita
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from cadastro.models import Pessoa
from administracao.models import Agendamento

from django.utils import timezone
from datetime import date    

@login_required
def index(request):

    horario_atual = timezone.now()
    data_atual = horario_atual.date()

    objPessoa = Pessoa.objects.get(pk=request.user.id)
    
    list_receitas = Receita.objects.filter(pessoa=objPessoa).order_by("-pk")
    listReceitas = []

    for q in list_receitas:
        try:
            objAgenda = Agendamento.objects.filter(receita=q)
        
        except Agendamento.DoesNotExist:
            objAgenda = None
            
        obj = {
            "Receita":q,
            "Agenda":objAgenda,
        }
        listReceitas.append(obj)
        
    context = {
        "nome_pagina" : "Home",
        "list_receitas" : listReceitas, 
        "usuario" : objPessoa,
        "data_atual" : data_atual,
    }

    return render(request, "home/index.html", context)

    list_receitas = Receita.objects.all()
