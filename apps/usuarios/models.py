from django.db import models
from django.urls import reverse
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import Group
from project.settings import capitalize_name

class Estado(models.Model):
    descricao = models.CharField(verbose_name = 'Nome', max_length = 30, unique = True)
    sigla = models.CharField(verbose_name = 'Sigla', max_length = 2, unique = True)
    data_registrado = models.DateTimeField(verbose_name = "Horário do registro", auto_now_add = True)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ['descricao']
        app_label = 'usuarios'
    
    def __str__(self):
        return self.descricao

class Cidade(models.Model):
    descricao = models.CharField(verbose_name = 'Nome', max_length = 50)
    codigo_IBGE = models.IntegerField(verbose_name = 'Código do IBGE')
    estado = models.ForeignKey(Estado, on_delete = models.CASCADE, related_name = 'estado_CidadeFK')
    data_registrado = models.DateTimeField(verbose_name = "Horário do registro", auto_now_add = True)

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        ordering = ['descricao']
        app_label = 'usuarios'

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

        group = Group.objects.get(name="Paciente")

        usuario.idGroup = group.id
        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False
        if password:
            usuario.set_password(password)
        usuario.save()
        usuario.groups.add(group)
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

        group = Group.objects.get(name="Medico")

        usuario.idGroup = group.id
        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.set_password(password)
        usuario.save()
        usuario.groups.add(group)

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
    dataNascimento = models.DateField(verbose_name = "Data de nascimento", auto_now_add = False, auto_now = False, null = True, blank = True)
    genero = models.CharField(verbose_name = 'Genero', max_length = 1, choices = GENERO)
    telefone = models.CharField(verbose_name = "Telefone", max_length = 16)
    cep = models.CharField(verbose_name = 'CEP', max_length = 9)
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE, related_name = 'cidade_UsuarioFK', null = True, blank = True)
    bairro = models.CharField(verbose_name = 'Bairro', max_length = 100)
    logradouro = models.CharField(verbose_name = 'Logradouro', max_length = 100)
    complemento = models.CharField(verbose_name = 'Complemento', max_length = 100)
    numeroResidencial = models.CharField(verbose_name = 'Número da residência', max_length = 10)
    idGroup = models.IntegerField(verbose_name = 'Id do grupo', default = 1)
    is_active = models.BooleanField(verbose_name = "Usuário ativo", default = True)
    is_staff = models.BooleanField(verbose_name = "Usuário desenvolvedor", default = False)
    is_superuser = models.BooleanField(verbose_name = "Super usuário", default = False)
    data_registrado = models.DateTimeField(verbose_name = "Horário do registro", auto_now_add = True)
    
    USERNAME_FIELD = "email"    
    REQUIRED_FIELDS = ['nome', 'sobrenome', 'cpf']
    
    objects = UsuarioManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        app_label = "usuarios"

    def save(self, *args, **kwargs):
        self.nome = capitalize_name(self.nome)
        self.sobrenome = capitalize_name(self.sobrenome)
        super(Usuario, self).save(*args, **kwargs)

    # def get_short_name(self):
    #     short_nome = self.nome.split()
    #     short_sobrenome = self.sobrenome.split()
    #     tam = len(short_sobrenome)
    #     return str(short_nome[0] + " " + short_sobrenome[tam-1])

    def get_full_name(self):
        return str(self.nome + " " + self.sobrenome)

    def get_absolute_url(self):
        return reverse('index')
        # return reverse('index', args=[str(self.id)]) CASO NECESSITASSE PASSAR ID

    def __str__(self):
        return self.get_full_name()

class MedicoPaciente(models.Model):
    medico = models.ForeignKey(Usuario, on_delete = models.CASCADE, verbose_name = "Médico", related_name = 'medico_MedicoPacienteFK')
    paciente = models.ForeignKey(Usuario, on_delete = models.CASCADE, verbose_name = "Paciente", related_name = 'paciente_MedicoPacienteFK')   
    is_active = models.BooleanField(verbose_name = 'Ativo', default = True)
    data_registrado = models.DateTimeField(verbose_name = "Horário do registro", auto_now_add = True)
    
    class Meta:
        verbose_name = "Médico e Paciente"
        verbose_name_plural = "Médicos e Pacientes"

    def __str__(self):
        return str(self.medico) + " - " + str(self.paciente)