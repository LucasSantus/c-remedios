from django.db import models
from django.urls import reverse
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def create_user(self, cpf, email, nome, sobrenome, password = None, **kwargs):
        if not email:
            raise ValueError('Insira um e-mail para continuar!')
        if not nome:
            raise ValueError('Insira um nome para continuar!')
        if not sobrenome:
            raise ValueError('Insira um sobrenome para continuar!')
        if not cpf:
            raise ValueError('Insira um cpf para continuar!')
        
        usuario = self.model(
            email = self.normalize_email(email),
            cpf = cpf,
            nome = nome,
            sobrenome = sobrenome,
            **kwargs
        )

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False
        usuario.is_agronomo = False

        if password:
            usuario.set_password(password)
        usuario.save()

        return usuario

    def create_superuser(self, cpf, email, nome, sobrenome, password, **kwargs):
        usuario = self.create_user(
            email = self.normalize_email(email),
            nome = nome,
            cpf = cpf,
            sobrenome = sobrenome,
            password = password,
            **kwargs
        )

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.is_agronomo = False
        usuario.set_password(password)
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser, PermissionsMixin):
    cpf = models.CharField(verbose_name = "CPF", max_length = 14, unique = True)
    email = models.EmailField(verbose_name = "E-mail", max_length = 194, unique = True) 
    nome = models.CharField(verbose_name = "Nome", max_length = 60)
    sobrenome = models.CharField(verbose_name = "Sobrenome", max_length = 150)
    telefone = models.CharField(verbose_name = "Telefone", max_length = 15, null = True, blank = True)
    data_nascimento = models.DateField(verbose_name = "Data de nascimento", auto_now_add = False, auto_now = False, null = True, blank = True)
    is_agronomo = models.BooleanField(verbose_name = "Usuário agronomo", default = False)
    is_active = models.BooleanField(verbose_name = "Usuário ativo", default = True)
    is_staff = models.BooleanField(verbose_name = "Usuário desenvolvedor", default = False)
    is_superuser = models.BooleanField(verbose_name = "Super usuário", default = False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['nome', 'sobrenome', 'cpf']

    objects = UsuarioManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        app_label = "usuarios"

    def get_short_name(self):
        short_nome = self.nome.split()
        short_sobrenome = self.sobrenome.split()
        tam = len(short_sobrenome)
        return str(short_nome[0] + " " + short_sobrenome[tam-1])

    def get_full_name(self):
        return str(self.nome + " " + self.sobrenome)

    def get_absolute_url(self):
        return reverse('index')
        # return reverse('index', args=[str(self.id)]) CASO NECESSITASSE PASSAR ID

    def __str__(self):
        return self.get_full_name()
    