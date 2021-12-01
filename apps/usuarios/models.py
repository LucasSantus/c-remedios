from django.db import models
from django.urls import reverse
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import MinLengthValidator


class Estado(models.Model):
    descricao = models.CharField(verbose_name = 'Nome', max_length = 30)
    sigla = models.CharField(verbose_name = 'Sigla', max_length = 2)
    dataHorarioCriacao = models.DateTimeField(verbose_name = 'Data e hora de criação', auto_now_add = True)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ['descricao']
    
    def __str__(self):
        return self.descricao

class Cidade(models.Model):
    descricao = models.CharField(verbose_name = 'Nome', max_length = 50)
    codigo_IBGE = models.IntegerField(verbose_name = 'Código do IBGE')
    estado = models.ForeignKey(Estado, on_delete = models.CASCADE, related_name = 'estado_CidadeFK')
    dataHorarioCriacao = models.DateTimeField(verbose_name = 'Data e hora de criação', auto_now_add = True)

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        ordering = ['descricao']

    def __str__(self):
        return str(self.descricao)

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
    GENERO =[
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("O", "Outro"),
        ("P", "Prefiro não dizer"),
    ]

    nome = models.CharField(verbose_name = "Nome", max_length = 60)
    sobrenome = models.CharField(verbose_name = "Sobrenome", max_length = 150)
    email = models.EmailField(verbose_name = "E-mail", max_length = 194, unique = True) 
    cpf = models.CharField(verbose_name = "CPF", max_length = 14, unique = True)
    dataNascimento = models.DateField(verbose_name = "Data de nascimento", auto_now_add = False, auto_now = False, blank = True, null = True)
    genero = models.CharField(verbose_name = 'Genero', max_length = 1, choices = GENERO, blank = True, null = True)
    telefone = models.CharField(verbose_name = "Telefone", max_length = 15, blank = True, null = True)
    cep = models.CharField(verbose_name = 'CEP', max_length = 9, blank = True, null = True)
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE, related_name = 'cidade_UsuarioFK', null = True)
    bairro = models.CharField(verbose_name = 'Bairro', max_length = 50, blank = True, null = True)
    logradouro = models.CharField(verbose_name = 'Logradouro', max_length = 100, blank = True, null = True)
    complemento = models.CharField(verbose_name = 'Complemento', max_length = 50, null = True, blank = True)
    numeroResidencial = models.CharField(verbose_name = 'Número da residência', max_length = 10, blank = True, null = True)
    idGroup = models.IntegerField(verbose_name = 'Id do grupo', default = 1, blank = True, null = True)
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
