from django.shortcuts import render, redirect
from .models import *
from .forms import PessoaForm, RemedioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def cadastrar_pessoa(request):

    form = PessoaForm()

    if request.method == "POST":
        form = PessoaForm(request.POST)

        if form.is_valid():
            pessoa = form.save()
            pessoa.save()
            
            messages.success(
                request, "Pessoa registrado com sucesso!"
            )
            
            return redirect("listar_pessoas")

    context = {
        "nome_pagina": "Registrar Pessoa",
        "form": form,
    }

    return render(request, "cadastro/cadastrar_pessoa.html", context)

@login_required
def listar_pessoas(request):

    list_pessoas = Pessoa.objects.all()

    context = {
        "nome_pagina": "Listar Pessoas",
        "list_pessoas": list_pessoas,
    }

    return render(request, "cadastro/listar_pessoas.html", context)

@login_required
def cadastrar_remedio(request):

    form = RemedioForm()

    if request.method == "POST":
        form = RemedioForm(request.POST)

        if form.is_valid():
            pessoa = form.save()
            pessoa.save()
            
            messages.success(
                request, "Remédio registrado com sucesso!"
            )
            
            return redirect("listar_remedios")

    context = {
        "nome_pagina": "Cadastrar Remédio",
        "form": form,
    }

    return render(request, "cadastro/cadastrar_remedio.html", context)

@login_required
def listar_remedios(request):

    list_remedios = Remedio.objects.all()

    context = {
        "nome_pagina": "Listar Remédios",
        "list_remedios": list_remedios,
    }

    return render(request, "cadastro/listar_remedios.html", context)
