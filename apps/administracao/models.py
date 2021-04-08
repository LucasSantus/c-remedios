# from django.db import models
 
# class Agendamento(models.Model):
#     nome = models.CharField(
#         verbose_name = "Nome do Agendamento:",
#         max_length=194,
#     )
#     receita = models.ForeignKey(Receita, on_delete=models.CASCADE, verbose_name = "Receita:")
#     horario_inicio = models.DateTimeField(
#         verbose_name = "Horário Ínicio:",
#         auto_now=False,
#         blank=True,
#         null=True,
#     )#o dia e hora q a pessoa começou a tomar o remedio
#     horario_termino = models.DateTimeField(
#         verbose_name = "Horário Término:",
#         auto_now=False,
#         blank=True,
#         null=True,
#     )#o dia e hora q a pessoa terminou de tomar o remedio

#     concluido = models.BooleanField(
#         verbose_name = "Concluído:",
#         max_length=194,
#     )

#     reajuste = models.BooleanField(
#         verbose_name = "Reajuste:",
#         max_length=194,
#     )
       
#     class Meta:
#         verbose_name = "Agendamento"
#         verbose_name_plural = "Agendamentos"
#         db_table = "agendamento"

#     def __str__(self):
#         return self.nome

# class Horario_Agendamento(models.Model):
#     agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE, verbose_name = "Agendamento:")
    
#     horario = models.DateTimeField(
#         verbose_name = "Horário:",
#         auto_now=False,
#         blank=True,
#         null=True,
#     )

#     concluido = models.BooleanField(
#         verbose_name = "Concluído:",
#         max_length=194,
#     )
       
#     class Meta:
#         verbose_name = "Horário do Agendamento"
#         verbose_name_plural = "Horários dos Agendamentos"
#         db_table = "horario_agendamento"

#     def __str__(self):
#         return str(self.horario)
