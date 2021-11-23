from django.shortcuts import render, redirect
from .models import Remedio
from .forms import  RemedioForm, ReceitaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# REMÉDIO
@login_required
def registrar_remedio(request):
    form = RemedioForm()
    if request.method == "POST":
        form = RemedioForm(request.POST)
        if form.is_valid():
            remedio = form.save()
            remedio.save()
            messages.success(request, "Remédio registrado com sucesso!")
            return redirect("listar_remedios")

    context = {
        "form": form,
    }

    return render(request, "receitas/remedio/registrar_remedio.html", context)

@login_required
def listar_remedios(request):
    list_remedios = Remedio.objects.all()
    context = {
        "list_remedios": list_remedios,
    }
    return render(request, "receitas/remedio/listar_remedios.html", context)

# RECEITA
@login_required
def registrar_receita(request):
    form = ReceitaForm()
    if request.method == "POST":
        form = ReceitaForm(request.POST)
        if form.is_valid():
            receita = form.save(commit = False)
            receita.pessoa = request.user
            receita.save()
            messages.success(request, "Receita registrado com sucesso!")
            return redirect("index")

    context = {
        "form": form,
    }

    return render(request, "cadastro/registrar_receita.html", context)