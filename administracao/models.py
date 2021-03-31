from django.db import models
from cadastro.models import *

class Receita(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    remedio = models.ForeignKey(Remedio, on_delete=models.CASCADE)
    intervalo = float() #intervalo q a pessoa irá tomar o remedio
    data_inicio = date() #o dia q a pessoa vai começar a tomar o remedio
    dosagem = int #a dosagem do remedio

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
        db_table = "receita"

    def __str__(self):
        return self.remedio
    
class Agendamento(models.Model):
    nome
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    horario_inicio = datetime() #o dia e hora q a pessoa começou a tomar o remedio
    horario_termino = datetime()#o dia e hora q a pessoa terminou de tomar o remedio
    concluido = boolean #caso foi concluido
    reajuste = ?
       
    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
        db_table = "receita"

    def __str__(self):
        return self.remedio
    
    