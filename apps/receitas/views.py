from django.shortcuts import render, redirect
from .models import Remedio
from .forms import  RemedioForm, ReceitaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from receitas.models import Receita
from vinculos.models import ReceitaMedicoPaciente
from usuarios.models import Usuario, MedicoPaciente
from .models import Agendamento, Horario_Agendamento
from django.utils import timezone
import datetime

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
def registrar_receita(request,id_medicoPaciente):
    objMedicoPaciente = MedicoPaciente.objects.get(pk=id_medicoPaciente)
    
    form = ReceitaForm()
    if request.method == "POST":
        form = ReceitaForm(request.POST)
        if form.is_valid():
            receita = form.save(commit = False)
            receita.medicoPaciente = objMedicoPaciente
            receita.save()
            messages.success(request, "Receita registrado com sucesso!")
            return redirect("ViewHome")

    context = {
        "form": form,
        "action": "Registrar"
    }

    return render(request, "receitas/receita/registrar_receita.html", context)

@login_required    
def dosagem_usuario(request,id_receita):
    horario_atual = timezone.now()
    objReceita = Receita.objects.get(pk=id_receita)
    objAgendaReceita = Agendamento.objects.get(receita=objReceita)
    nome_pagina = objReceita.remedio.nome
    listHorario = Horario_Agendamento.objects.filter(agendamento=objAgendaReceita)

    listHorarios_false = []

    for horario in listHorario:
        if not horario.concluido:
            listHorarios_false.append(horario)

    cont = 0 
    for l in listHorarios_false:
        if l.horario <= horario_atual:
            cont += 1

    if cont > 1:

        messages.error(request,"Você não tomou sua ultima dose no horário certo, Por favor selecione uma nova data!") 

        for l in listHorarios_false:
            l.delete()
        
        return redirect("configura_horario_dosagem",id_receita )     
        
    else:
        if request.POST:
            idObjHorario = request.POST.get('tomou_remedio', None)
            if idObjHorario:
                objHorario = Horario_Agendamento.objects.get(pk=idObjHorario)
                objHorario.concluido = True
                objHorario.save()
                if objHorario == Horario_Agendamento.objects.filter(agenda_receita=objAgendaReceita).last():
                    objAgendaReceita.concluido = True
                    objAgendaReceita.save()
            

            return redirect("registrar_receita")


    context = {
        "nome_pagina": "Dosagens - "+ nome_pagina,
        "objAgendaReceita" : objAgendaReceita,
        'listHorario' : listHorario,
        'horario_atual' : horario_atual,
    }

    return render(request,"lista_dosagem.html",context)

@login_required
def configura_horario_dosagem(request,id_receita):
    listHorarios = []
    objReceita = Receita.objects.get(pk=id_receita)

    try:
        objAgenda_receita = Agendamento.objects.get(receita=objReceita)
    except:
        objAgenda_receita = None

    totalDoze = int((objReceita.quantidade_dias*24)/objReceita.intervalo)

    if not objAgenda_receita:
        if request.POST:
            data_de_inicio = request.POST.get('data_de_inicio', None)  
            if data_de_inicio:       
                horario_inicio_remedio=datetime.datetime.strptime(data_de_inicio,'%Y-%m-%d %H:%M')    
                Agendamento(receita = objReceita, data_inicio = horario_inicio_remedio,
                    data_de_termino = horario_inicio_remedio + timezone.timedelta(days=objReceita.quantidade_dias)).save()

                Horario_Agendamento(agendamento=objAgenda_receita,horario=horario_inicio_remedio).save()

                list_obj_horario = []
                for q in range(totalDoze):
                    horario_inicio_remedio += timezone.timedelta(hours=objReceita.intervalo)
                    objHorario = Horario_Agendamento(agendamento = objAgenda_receita, horario = horario_inicio_remedio)
                    list_obj_horario.append(objHorario)
                
                if list_obj_horario:  
                    Horario_Agendamento.objects.bulk_create(list_obj_horario)

                return redirect("dosagem_usuario",id_receita)  
            else:
                return redirect("configura_horario_dosagem",id_receita )
    else:
        listHorarios = Horario_Agendamento.objects.filter(agendamento=objAgenda_receita)

        totalDoze -= len(listHorarios)
        if request.POST:
            data_de_inicio = request.POST.get('data_de_inicio', None)
            
            if data_de_inicio:        
                horario_inicio_remedio=datetime.datetime.strptime(data_de_inicio,'%Y-%m-%d %H:%M')    
                objAgenda_receita.reajuste = True
                objAgenda_receita.data_inicio = horario_inicio_remedio 
                objAgenda_receita.data_de_termino = horario_inicio_remedio + timezone.timedelta(days=objReceita.quantidade_dias)
                objAgenda_receita.save()
                
                objHorario = Horario_Agendamento(agendamento = objAgenda_receita, horario = horario_inicio_remedio).save()

                list_obj_horario = []
                for q in range(totalDoze-1):
                    horario_inicio_remedio += timezone.timedelta(hours=objReceita.intervalo)
                    objHorario = Horario_Agendamento(agendamento = objAgenda_receita, horario = horario_inicio_remedio)
                    list_obj_horario.append(objHorario)
                
                if list_obj_horario:  
                    Horario_Agendamento.objects.bulk_create(list_obj_horario)

                messages.success(request, "Ebaa! Horarios Reagendados com sucesso!")
                return redirect("dosagem_usuario",id_receita)
                
            else:
                messages.error(request, "Opps! Algo de errado aconteceu, por favor selecione um horario!")
                return redirect("configura_horario_dosagem",id_receita )

    context = {
        "nome_pagina":"datas disponiveis",
        "listHorarios" : listHorarios,
    }

    return render(request,"configura_horarios.html",context)

@login_required
def registrar_paciente(request):
    listPacientes = Usuario.objects.filter(groups__name="Paciente")

    if request.method == "POST":

        objPaciente = Usuario.objects.get(pk=request.POST.get('paciente',None))
        try:
            MedicoPaciente.objects.get(paciente = objPaciente,medico = request.user)
            messages.info(request, "Ops esse paciente já é seu...")
            
        except MedicoPaciente.DoesNotExist:
            MedicoPaciente(paciente=objPaciente,medico=request.user).save()
            messages.success(request, "Paciente registrado com sucesso!")

        return redirect("ViewHome")

    context = {
        "listPacientes": listPacientes,
        "action": "registrar paciente"
    }

    return render(request, "receitas/paciente/cadastrar-paciente.html", context)

