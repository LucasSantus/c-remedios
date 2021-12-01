from django.shortcuts import render, redirect
from .models import Remedio
from .forms import  RemedioForm, ReceitaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from receitas.models import Receita
from usuarios.models import Usuario
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
def registrar_receita(request):
    form = ReceitaForm()
    if request.method == "POST":
        form = ReceitaForm(request.POST)
        if form.is_valid():
            receita = form.save(commit = False)
            receita.usuario = request.user
            receita.save()
            messages.success(request, "Receita registrado com sucesso!")
            return redirect("index")

    context = {
        "form": form,
        "action": "Registrar"
    }

    return render(request, "receitas/receita/registrar_receita.html", context)

@login_required    
def dosagem_usuario(request,id_receita):
    horario_inicio_remedio = timezone.now()
    horario_atual = timezone.now()
    objPessoa = Usuario.objects.get(pk=request.user.id)
    primeiro_nome = objPessoa.nome.split(None, 1)[0]
    objReceita = Receita.objects.get(pk=id_receita)
    objAgenda_receita = Agendamento.objects.get(receita=objReceita)
    nome_pagina = objReceita.remedio.nome
    listHorario = Horario_Agendamento.objects.filter(agendamento=objAgenda_receita)

    listHorarios_false = []

    for l in listHorario:
        if l.concluido == False:
            listHorarios_false.append(l)
    cont = 0 
    for l in listHorarios_false:
        if l.horario <= horario_atual:
            cont += 1

    if cont > 1:

        print("deu ruim")
        messages.error(request,"Você não tomou sua ultima dose no horário certo, Por favor selecione uma nova data!") 

        for l in listHorarios_false:
            l.delete()
        
        return redirect("configura_horario_dosagem",id_receita )     
        
    else:
        print("está certo")
        if request.POST:
            idObjHorario = request.POST.get('tomou_remedio', None)
            if idObjHorario:
                objHorario = Horario_remedio.objects.get(pk=idObjHorario)
                objHorario.concluido = True
                objHorario.save()
                if objHorario == Horario_remedio.objects.filter(agenda_receita=objAgenda_receita).last():
                    print("testekak")
                    objAgenda_receita.concluido = True
                    objAgenda_receita.save()
                return redirect("registrar_receita")
            else:
                return redirect("registrar_receita")


    context = {
        "nome_pagina": "Dosagens - "+ nome_pagina,
        "usuario" : primeiro_nome,
        "objAgenda_receita" : objAgenda_receita,
        'listHorario':listHorario,
        'horario_atual' : horario_atual,
    }

    return render(request,"lista_dosagem.html",context)

@login_required
def configura_horario_dosagem(request,id_receita):
    data_now = timezone.now()
    listHorarios = []
    
    objPessoa = Usuario.objects.get(pk=request.user.id)
    primeiro_nome = objPessoa.nome.split(None, 1)[0]
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
                objAgenda_receita = Agendamento()
                objAgenda_receita.receita = objReceita
                objAgenda_receita.data_inicio = horario_inicio_remedio 
                objAgenda_receita.data_de_termino = horario_inicio_remedio + timezone.timedelta(days=objReceita.quantidade_dias)
                objAgenda_receita.save()
                
                objHorario = Horario_Agendamento()
                objHorario.agendamento = objAgenda_receita
                objHorario.horario = horario_inicio_remedio
                objHorario.save()
                
                for q in range(totalDoze):
                    horario_inicio_remedio += timezone.timedelta(hours=objReceita.intervalo)
                    objHorario = Horario_Agendamento()
                    objHorario.agendamento = objAgenda_receita
                    objHorario.horario = horario_inicio_remedio
                    objHorario.save()
                return redirect("dosagem_usuario",id_receita )  
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
                
                objHorario = Horario_Agendamento()
                objHorario.agendamento = objAgenda_receita
                objHorario.horario = horario_inicio_remedio
                objHorario.save()
                
                for q in range(totalDoze):
                    horario_inicio_remedio += timezone.timedelta(hours=objReceita.intervalo)
                    objHorario = Horario_Agendamento()
                    objHorario.agendamento = objAgenda_receita
                    objHorario.horario = horario_inicio_remedio
                    objHorario.save()
                return redirect("dosagem_usuario",id_receita )
            else:
                return redirect("configura_horario_dosagem",id_receita )

    context = {
        "nome_pagina":"datas disponiveis",
        "usuario" : primeiro_nome,
        "listHorarios" : listHorarios,
    }

    return render(request,"configura_horarios.html",context)