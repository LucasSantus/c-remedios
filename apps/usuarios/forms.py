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
        # fields = ['email', 'cpf', 'nome', "sobrenome", "telefone", "dataNascimento", "password", "confirm_password"]
    
        error_messages = {
            "email":{
                "required": "O e-mail é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um e-mail válido!",
            },
            "nome":{
                "required": "O nome é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um nome válido!",
            },
            "cpf":{
                "required": "O cpf é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um cpf válido!",
            },
            "sobrenome":{
                "required": "O sobrenome é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um sobrenome válido!",
            },
            "telefone":{
                "required": "O telefone é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um telefone válido!",
            },
            "password":{
                "required": "A senha é obrigatória para realizar o registro!",
                "invalid": "Por favor, insira uma senha válida!",
            },
            "dataNascimento":{
                "invalid": "Por favor, insira um formato válido de data de nascimento (DD/MM/AAAA)!",
            },
        }
        
        # widgets = {
        #     "email": forms.TextInput(attrs={'placeholder':'Insira o e-mail...'}),
        #     "cpf": forms.TextInput(attrs={'placeholder':'Insira o cpf...'}),
        #     "nome": forms.TextInput(attrs={'placeholder':'Insira o nome...'}),
        #     "sobrenome": forms.TextInput(attrs={'placeholder':'Insira o sobrenome...'}),
        #     "telefone": forms.TextInput(attrs={'placeholder':'Insira o telefone...'}),
        #     "dataNascimento": forms.TextInput(attrs={'placeholder':'Insira a data de nascimento...'}),
        #     "password": forms.TextInput(attrs={'placeholder':'Insira a senha...'}),
        # }
        
        labels = {
            "email": 'E-mail: ',
            "cpf": 'CPF: ',
            "nome": 'Nome: ',
            "sobrenome": 'Sobrenome: ',
            "telefone": 'Telefone: ',
            "dataNascimento": 'Data de Nascimento: ',
            "password": 'Senha: ',
        }