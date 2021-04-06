from django import forms
from .models import Receita, Agendamento, Horario_Agendamento

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ('pessoa', 'remedio', 'intervalo', 'data_inicio', 'dosagem')

        error_messages = {
            "pessoa":{
                "required": "Selecione uma pessoa!",
            },

            "remedio":{
                "required": "Selecione um remédio!",
            },
            "intervalo":{
                "required": "Insira um intervalo!",
            },
            "data_inicio":{
                "required": "Selecione uma data!",
                "invalid": "Insira uma Data válida!",
            },
            "dosagem":{
                "required": "Insira uma dosagem!",
            },
        }

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ('nome', 'receita', 'horario_inicio', 'concluido', 'reajuste')

        error_messages = {
            "nome":{
                "required": "Insira o Nome!",
            },

            "receita":{
                "required": "Selecione a receita!",
            },

            "horario_inicio":{
                "required": "Insira um intervalo!",
            },
        }

class HorarioAgendamentoForm(forms.ModelForm):
    class Meta:
        model = Horario_Agendamento
        fields = ("__all__")
