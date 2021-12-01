from django.shortcuts import render
from receitas.models import Receita
from django.contrib.auth.decorators import login_required
from datetime import date
from django.utils import timezone

from administracao.models import Agendamento
import datetime

def base(request):
    context = {}
    if request.user.is_authenticated:
        url_path = request.path
        list_path = []
        if len(url_path) == 1:
            list_path.append('/')
        else:
            for url in url_path[1:]:
                if url == '/':
                    break
                else:
                    list_path.append(url)
                
        url_active = "".join(list_path)
    
        date = datetime.datetime.now().date()
        context = {
            'year': date.year,
            'url_active': url_active
        }
    return context

@login_required
def index(request):
    receitas = Receita.objects.filter(usuario = request.user).order_by("-pk")
    listReceitas = []
    for receita in receitas:
        try:
            agendamento = Agendamento.objects.filter(receita = receita)
        except Agendamento.DoesNotExist:
            agendamento = None
            
        obj = {
            "receita": receita,
            "Agendamento": agendamento,
        }

        listReceitas.append(obj)

    context = {
        "list_receitas": listReceitas,
    }

    return render(request, "home/index.html", context)
