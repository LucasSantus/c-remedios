from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UsuarioManager(BaseUserManager):

    def create_user(self, cpf, password=None):
        usuario = self.model(
            cpf = cpf
        )

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)
        
        usuario.save()
        
        return usuario
    
    def create_superuser(self, cpf, password):
        usuario = self.create_user(
            cpf = cpf,
            password = password,
        )

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)

        usuario.save()

        return usuario

class Pessoa(AbstractBaseUser,PermissionsMixin):

    nome = models.CharField(
        verbose_name = "Nome Completo:",
        max_length=194,
    )

    cpf = models.CharField(
        verbose_name = "CPF:",
        max_length=11,
        unique=True,
    )

    data_nascimento = models.DateField(
        verbose_name = "Data de Nascimento:",
        auto_now_add=False,
        auto_now=False,
        null=True,
    )

    horario_criacao = models.DateTimeField(
        verbose_name = "Horário do Cadastro no Sistema:",
        auto_now_add=True,
    )
      
    is_active = models.BooleanField(
        verbose_name="Usuário está ativo",
        default=True, 
    )
    is_staff  = models.BooleanField(
        verbose_name="Usuário é da equipe de desenvolvimento",
        default= False,
    )

    is_superuser = models.BooleanField(
        verbose_name= "Usuário é um superusuario",
        default=False,
    )

    USERNAME_FIELD = "cpf"

    objects = UsuarioManager()

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        db_table = "pessoas"

    def __str__(self):
        return self.nome
    
class Remedio(models.Model):
    
    nome = models.CharField(
        verbose_name = "Nome do Remédio:",
        max_length=194,
    )

    descricao = models.TextField(
        verbose_name = "Descrição do Remédio:",
        max_length=340,
    )
    
    class Meta:
        verbose_name = "Remédio"
        verbose_name_plural = "Remédios"
        db_table = "remedio"

    def __str__(self):
        return self.nome

class Receita(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name = "Pessoa:")
    remedio = models.ForeignKey(Remedio, on_delete=models.CASCADE , verbose_name = "Remédio:")
    intervalo = models.FloatField(verbose_name = "Intervalo:")
    quantidade_dias = models.PositiveIntegerField(
        verbose_name = "Total de dias",
        help_text = "total de dias que será consumido o remédio",
        default = 0,
    )
    data_inicio = models.DateTimeField(
        verbose_name = "Data de Ínicio:",
        auto_now=False,
        blank=True,
        null=True,
    )
    dosagem = models.IntegerField(verbose_name = "Dosagem:")#a dosagem do remedio

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
        db_table = "receita"

    def __str__(self):
        return str("{} - {}".format(self.pessoa.nome, self.remedio.nome))
   