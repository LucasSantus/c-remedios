from django import forms
from .models import Pessoa, Remedio, Receita

class PessoaForm(forms.ModelForm):

    def save(self, commit=True):
        user = super(PessoaForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = Pessoa
        fields = ('nome', 'cpf', 'data_nascimento', 'password')

        error_messages = {
            "nome":{
                "required": "É obrigatório o Nome Completo do individuo para a realização do registro",
            },

            "cpf":{
                "required": "É obrigatório o CPF do individuo para a realização do registro",
                "invalid": "Insira um CPF válido!",
            },
            "data_nascimento":{
                "required": "É obrigatório a Data de Nascimento do individuo para a realização do registro",
                "invalid": "Insira uma Data de Nascimento válida!",
            },
            "password":{
                "required": "É obrigatório a Senha do individuo para a realização do registro",
            },
        }

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
        fields = ('pessoa', 'remedio', 'intervalo', 'data_inicio', 'quantidade_dias','dosagem')

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
            "quantidade_dias":{
                "required": "Insira a quantidade de dias para tomar o remédio!",
            },
            "dosagem":{
                "required": "Insira uma dosagem!",
            },
        }