from django.shortcuts import render, redirect
from .models import Agendamento, Horario_Agendamento
from .forms import AgendamentoForm, HorarioAgendamentoForm
from django.contrib import messages

def cadastrar_agendamento(request):
    form = AgendamentoForm()

    if request.method == "POST":
        form = AgendamentoForm(request.POST)

        if form.is_valid():
            agendamento = form.save()
            agendamento.save()
            
            messages.success(
                request, "Agendamento registrado com sucesso!"
            )
            
            return redirect("index")

    context = {
        "nome_pagina": "Cadastrar Agendamento",
        "form": form,
    }

    return render(request, "administracao/cadastrar_agendamento.html", context)

def cadastrar_horario_agendamento(request):
    form = HorarioAgendamentoForm()

    if request.method == "POST":
        form = HorarioAgendamentoForm(request.POST)

        if form.is_valid():
            horario = form.save()
            horario.save()
            
            messages.success(
                request, "Horário registrado com sucesso!"
            )
            
            return redirect("index")

    context = {
        "nome_pagina": "Cadastrar Horário",
        "form": form,
    }

    return render(request, "administracao/cadastrar_horario-agendamento.html", context)
