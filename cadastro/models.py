from django.db import models

class Pessoa(models.Model):

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