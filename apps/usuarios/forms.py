from django import forms
from django.forms import widgets
from .models import *

class UsuarioForm(forms.ModelForm):
    confirm_password = forms.CharField(
        max_length = 30, 
        required = True, 
        label = "Confirmação: ",
        error_messages = {
            "required": "A confirmação de senha é obrigatória para realizar o registro!",
            "invalid": "Por favor, insira uma confirmação de senha válida!",
        },
        widget = forms.TextInput(attrs={'placeholder':'Insira a confirmação de senha...'}),
    )
    
    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit = False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user

    class Meta:
        model = Usuario
        fields = ('__all__')
        fields = [
            "nome", "sobrenome", "email", "cpf", "dataNascimento", 
            "genero", "telefone", "cep", "cidade", "bairro", 
            "logradouro", "complemento", "numeroResidencial",  
            "password", "confirm_password"]
    
        error_messages = {
            "nome":{
                "required": "O nome é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um nome válido!",
            },
            "sobrenome":{
                "required": "O sobrenome é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um sobrenome válido!",
            },
            "email":{
                "required": "O e-mail é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um e-mail válido!",
            },
            "cpf":{
                "required": "O cpf é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um cpf válido!",
            },
            "dataNascimento":{
                "invalid": "Por favor, insira um formato válido de data de nascimento (DD/MM/AAAA)!",
            },
            "telefone":{
                "required": "O telefone é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um telefone válido!",
            },
            "genero": {
                "required": "O genero é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira uma gênero válido!",
            },
            "telefone": {
                "required": "O telefone é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira uma telefone válido!",
            },
            "cep": {
                "required": "O cep é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira uma cep válido!",
            },
            "cidade": {
                "required": "A cidade é obrigatória para realizar o registro!",
                "invalid": "Por favor, insira uma cidade válida!",
            },
            "bairro": {
                "required": "O bairro é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um bairro válido!",
            },
            "logradouro": {
                "required": "O logradouro é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um logradouro válido!",
            },
            "complemento": {
                "required": "O complemento é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um complemento válido!",
            },
            "numeroResidencial": {
                "required": "O número residencial é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um número residencial válido!",
            },
            "password:": {
                "required": "A senha é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira uma senha válida!",
            },
            "confirm_password": {
                "required": "A confirmação de senha é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um confirmação de senha válida!",
            },
        }

        widgets = {
            "nome": forms.TextInput(attrs={'placeholder':'Insira o nome...'}),
            "sobrenome": forms.TextInput(attrs={'placeholder':'Insira o sobrenome...'}),
            "email": forms.TextInput(attrs={'placeholder':'Insira o e-mail...'}),
            "cpf": forms.TextInput(attrs={'placeholder':'Insira o cpf...'}),
            "dataNascimento": forms.TextInput(attrs={'placeholder':'Insira a data de nascimento...'}),
            # "genero": forms.TextInput(attrs={'placeholder':'Insira o genero...'}),
            "telefone": forms.TextInput(attrs={'placeholder':'Insira o telefone...'}),
            "cep": forms.TextInput(attrs={'placeholder':'Insira o cep...'}),
            # "cidade": forms.TextInput(attrs={'placeholder':'Insira a cidade...'}),
            "bairro": forms.TextInput(attrs={'placeholder':'Insira o bairro...'}),
            "logradouro": forms.TextInput(attrs={'placeholder':'Insira o logradouro...'}),
            "complemento": forms.TextInput(attrs={'placeholder':'Insira o complemento...'}),
            "numeroResidencial": forms.TextInput(attrs={'placeholder':'Insira o número residencial...'}),
            "password": forms.TextInput(attrs={'placeholder':'Insira a senha...'}),
            "confirm_password": forms.TextInput(attrs={'placeholder':'Insira a confirmação...'}),
        }

        labels = {
            "nome": 'Nome: ',
            "sobrenome": 'Sobrenome: ',
            "email": 'E-mail: ',
            "cpf": 'CPF: ',
            "dataNascimento": 'Data de Nascimento: ',
            "telefone": 'Telefone: ',
            "genero": 'Gênero: ',
            "cep": 'CEP: ',
            "cidade": 'Cidade: ',
            "bairro": 'Bairro: ',
            "logradouro": 'Logradouro: ',
            "complemento": 'Complemento: ',
            "numeroResidencial": 'Número: ',
            "password": 'Senha: ',
            "confirm_password": 'Confirmação de Senha: '
        }


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            "nome", "sobrenome", "email", "cpf", "dataNascimento", 
            "genero", "telefone", "cep", "bairro", 
            "logradouro", "complemento", "numeroResidencial",  
            ]
    
        error_messages = {
            "nome":{
                "required": "O nome é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um nome válido!",
            },
            "sobrenome":{
                "required": "O sobrenome é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um sobrenome válido!",
            },
            "email":{
                "required": "O e-mail é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um e-mail válido!",
            },
            "cpf":{
                "required": "O cpf é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um cpf válido!",
            },
            "dataNascimento":{
                "invalid": "Por favor, insira um formato válido de data de nascimento (DD/MM/AAAA)!",
            },
            "telefone":{
                "required": "O telefone é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um telefone válido!",
            },
            "genero": {
                "required": "O genero é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira uma gênero válido!",
            },
            "telefone": {
                "required": "O telefone é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira uma telefone válido!",
            },
            "cep": {
                "required": "O cep é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira uma cep válido!",
            },
            "cidade": {
                "required": "A cidade é obrigatória para realizar o registro!",
                "invalid": "Por favor, insira uma cidade válida!",
            },
            "bairro": {
                "required": "O bairro é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um bairro válido!",
            },
            "logradouro": {
                "required": "O logradouro é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um logradouro válido!",
            },
            "complemento": {
                "required": "O complemento é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um complemento válido!",
            },
            "numeroResidencial": {
                "required": "O número residencial é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um número residencial válido!",
            },
        }

        widgets = {
            "nome": forms.TextInput(attrs={'placeholder':'Insira o nome...'}),
            "sobrenome": forms.TextInput(attrs={'placeholder':'Insira o sobrenome...'}),
            "email": forms.TextInput(attrs={'placeholder':'Insira o e-mail...'}),
            "cpf": forms.TextInput(attrs={'placeholder':'Insira o cpf...'}),
            "dataNascimento": forms.TextInput(attrs={'placeholder':'Insira a data de nascimento...'}),
            "telefone": forms.TextInput(attrs={'placeholder':'Insira o telefone...'}),
            "cep": forms.TextInput(attrs={'placeholder':'Insira o cep...'}),
            "bairro": forms.TextInput(attrs={'placeholder':'Insira o bairro...'}),
            "logradouro": forms.TextInput(attrs={'placeholder':'Insira o logradouro...'}),
            "complemento": forms.TextInput(attrs={'placeholder':'Insira o complemento...'}),
            "numeroResidencial": forms.TextInput(attrs={'placeholder':'Insira o número residencial...'}),
        }

        labels = {
            "nome": 'Nome: ',
            "sobrenome": 'Sobrenome: ',
            "email": 'E-mail: ',
            "cpf": 'CPF: ',
            "dataNascimento": 'Data de Nascimento: ',
            "telefone": 'Telefone: ',
            "genero": 'Gênero: ',
            "cep": 'CEP: ',
            "cidade": 'Cidade: ',
            "bairro": 'Bairro: ',
            "logradouro": 'Logradouro: ',
            "complemento": 'Complemento: ',
            "numeroResidencial": 'Número: ',
        }