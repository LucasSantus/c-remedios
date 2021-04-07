from django import forms
from .models import Agendamento, Horario_Agendamento

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
