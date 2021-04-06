from django.shortcuts import render, redirect
from .models import Receita
from .forms import ReceitaForm

def cadastrar_receita(request):
    form = ReceitaForm()

    if request.method == "POST":
        form = ReceitaForm(request.POST)

        if form.is_valid():
            pessoa = form.save()
            pessoa.save()
            
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