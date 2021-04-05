from django.shortcuts import render, redirect

from .models import *
from django.contrib import messages

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
        "nome_pagina": "Registrar pessoa",
        "form": form,
    }

    return render(request, "cadastro/registrar_pessoa.html", context)

def listar_pessoas(request):

    list_pessoas = Pessoa.objects.all()

    context = {
        "list_pessoas": list_pessoas,
    }

    return render(request, "cadastro/listar_pessoa.html", context)
