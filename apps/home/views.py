from django.shortcuts import render,redirect
from apps.home.validate import RetornaGrupo
from receitas.models import Receita
from vinculos.models import MedicoPaciente, ReceitaMedicoPaciente
from django.contrib.auth.decorators import login_required
from project.settings import GPMedico, GPPaciente

from receitas.models import Agendamento
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
            'url_active': url_active,
            'idGroup':request.user.idGroup,
            'GPMedico': GPMedico,
            'GPPaciente': GPPaciente,
        }
    return context

@login_required
def ViewHome(request):
    listGroups = [
        {
            'Nome': GPMedico,
            'Url': "ViewDashboardMedico"
        },
        {
            'Nome': GPPaciente,
            'Url': "ViewDashboardPaciente"
        },
    ]

    if request.user.is_authenticated:
        for x in listGroups:
            if RetornaGrupo(request).name == x['Nome']:
                return redirect(x['Url'])

@login_required
def ViewDashboardMedico(request):
    list_pacientes = MedicoPaciente.objects.filter(medico__id = request.user.id, is_active = True)
    context = {
        "list_pacientes": list_pacientes,
    }
    return render(request, "home/medico.html", context)

@login_required
def ViewDashboardPaciente(request):
    listReceitaAgendamento = []
    try:
        listReceitaMedicoPaciente = ReceitaMedicoPaciente.objects.filter(medico_paciente__paciente = request.user)
        
        for objReceitaMedicoPaciente in listReceitaMedicoPaciente:
            try:
                objAgendamento = Agendamento.objects.get(receita = objReceitaMedicoPaciente.receita)
            except Agendamento.DoesNotExist:
                objAgendamento = None
            obj = {
                "objReceitaMedicoPaciente":objReceitaMedicoPaciente,
                "objAgendamento":objAgendamento
            }

            listReceitaAgendamento.append(obj)

    except Receita.DoesNotExist:
        listReceitaMedicoPaciente = None


    context = {
        "listReceitaAgendamento": listReceitaAgendamento,
    }

    return render(request, "home/index.html", context)
