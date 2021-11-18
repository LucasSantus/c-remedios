from django import forms
from .models import *

class RemedioForm(forms.ModelForm):
    class Meta:
        model = Remedio
        fields = ('nome', 'descricao')

        error_messages = {
            "nome":{
                "required": "É obrigatório o Nome do individuo para a realização do registro",
            },

            "descricao":{
                "required": "É obrigatório o CPF do individuo para a realização do registro",
            },
        }

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ('remedio', 'intervalo', 'data_inicio', 'quantidade_dias','dosagem')

        error_messages = {
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
            "quantidade_dias":{
                "required": "Insira a quantidade de dias para tomar o remédio!",
            },
            "dosagem":{
                "required": "Insira uma dosagem!",
            },
        }