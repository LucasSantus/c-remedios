from django.db import models
from receitas.models import Receita
from usuarios.models import MedicoPaciente

class ReceitaMedicoPaciente(models.Model):
    medico_paciente = models.ForeignKey(MedicoPaciente, on_delete = models.CASCADE, verbose_name = "Medico Paciente", related_name = 'medicoPaciente_ReceitaMedicoPacienteFK')
    receita = models.ForeignKey(Receita, on_delete = models.CASCADE , verbose_name = "Receita", related_name = 'receita_ReceitaMedicoPacienteFK')
    data_registrado = models.DateTimeField(verbose_name = "Horário do registro", auto_now_add = True)
    
    class Meta:
        verbose_name = "Receita Médico Paciente"
        verbose_name_plural = "Receitas Médicos Pacientes"
        app_label = 'vinculos'

    def __str__(self):
        return str(self.medico) + " - " + str(self.paciente)