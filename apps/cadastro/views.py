from django.shortcuts import render, redirect

from .models import Pessoa, Remedio, Receita
from .forms import PessoaForm, RemedioForm, ReceitaForm

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

def cadastrar_receita(request):
    form = ReceitaForm()

    if request.method == "POST":
        form = ReceitaForm(request.POST)

        if form.is_valid():
            receita = form.save()
            receita.save()
            
            messages.success(
                request, "Receita registrada com sucesso!"
            )
            
            return redirect("listar_receitas")

    context = {
        "nome_pagina": "Cadastrar Receita",
        "form": form,
    }

    return render(request, "administracao/cadastrar_receita.html", context)

def listar_receitas(request):

    list_receitas = Receita.objects.all()

    context = {
        "nome_pagina": "Listar Receitas",
        "list_receitas": list_receitas,
    }

    return render(request, "administracao/listar_receitas.html", context)