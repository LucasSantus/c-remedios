from django.shortcuts import render
from cadastro.models import Receita
from django.contrib.auth.decorators import login_required
from datetime import date    
from administracao.models import Agendamento

@login_required
def index(request):
    receitas = Receita.objects.filter(pessoa = request.user).order_by("-pk")
    listReceitas = []
    for receita in receitas:
        try:
            agendamento = Agendamento.objects.filter(receita = receita)
        except Agendamento.DoesNotExist:
            agendamento = None
            
        obj = {
            "receita": receita,
            "agenda": agendamento,
        }

        listReceitas.append(obj)

    context = {
        "receitas" : listReceitas,
    }

    return render(request, "home/index.html", context)
