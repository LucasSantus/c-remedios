from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required    
def dosagem_usuario(request,id_receita):

    horario_inicio_remedio = timezone.now()
    horario_atual = timezone.now()
    objPessoa = Pessoa.objects.get(pk=request.user.id)
    objReceita = Receita.objects.get(pk=id_receita)

    objAgenda_receita = Agenda_receita.objects.get(receita=objReceita)

    listHorario = Horario_remedio.objects.filter(agenda_receita=objAgenda_receita)
        
    objAgenda_receita.save()

    if request.POST:
        idObjHorario = request.POST.get('tomou_remedio', None)
        if idObjHorario:
            objHorario = Horario_remedio.objects.get(pk=idObjHorario)
            objHorario.concluido = True
            objHorario.save()
            return redirect("registrar_receita")
        else:
            return redirect("registrar_receita")


    context = {
        "nome_pagina":"Dosagens",
        "usuario" : objPessoa,
        "objAgenda_receita" : objAgenda_receita,
        'listHorario':listHorario,
        'horario_atual' : horario_atual,
    }

    return render(request,"lista_dosagem.html",context)

@login_required
def configura_horario_dosagem(request,id_receita):
    data_now = timezone.now()
    listHorarios = []
    
    objPessoa = Pessoa.objects.get(pk=request.user.id)
    objReceita = Receita.objects.get(pk=id_receita)

    totalDoze = int((objReceita.quantidade_dias*24)/objReceita.intervalo)    
    if request.POST:
        data_de_inicio = request.POST.get('data_de_inicio', None)        
        horario_inicio_remedio =datetime.datetime.strptime(data_de_inicio,'%Y-%m-%d %H:%M')    
        print(horario_inicio_remedio)
        objAgenda_receita = Agenda_receita()
        objAgenda_receita.receita = objReceita
        objAgenda_receita.data_inicio = horario_inicio_remedio 
        objAgenda_receita.data_de_termino = horario_inicio_remedio + timezone.timedelta(days=objReceita.quantidade_dias)
        objAgenda_receita.save()
        
        objHorario = Horario_remedio()
        objHorario.agenda_receita = objAgenda_receita
        objHorario.horario = horario_inicio_remedio
        objHorario.save()
        
        for q in range(totalDoze):
            horario_inicio_remedio += timezone.timedelta(hours=objReceita.intervalo)
            objHorario = Horario_remedio()
            objHorario.agenda_receita = objAgenda_receita
            objHorario.horario = horario_inicio_remedio
            objHorario.save()
        return redirect("dosagem_usuario",id_receita )


    context = {
        "nome_pagina":"datas disponiveis",
        "usuario" : objPessoa,
        "listHorarios" : listHorarios,
    }

    return render(request,"configura_horarios.html",context)

