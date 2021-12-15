from django.db import models

class MedicoPaciente(models.Model):
    medico = models.ForeignKey("usuarios.Usuario", on_delete = models.CASCADE,verbose_name = "Médico",related_name = 'medico_MedicoPacienteFK')
    paciente = models.ForeignKey("usuarios.Usuario", on_delete = models.CASCADE,verbose_name = "Paciente",related_name = 'paciente_MedicoPacienteFK')   
    data_registrado = models.DateTimeField(verbose_name = "Horário do registro", auto_now_add = True)
    
    class Meta:
        verbose_name = "Médico e paciente"
        verbose_name_plural = "Médicos e pacientes"

    def __str__(self):
        return str(self.medico) + "-" + str(self.paciente)

class Remedio(models.Model):    

    TIPO =[
        ("C", "Comprimido"),
        ("G", "Gota"),
        ("V", "Vacina"),
    ]

    nome = models.CharField(verbose_name = "Nome", max_length = 100)
    descricao = models.TextField(verbose_name = "Descrição", max_length = 340)
    tipo = models.CharField(verbose_name = 'Tipo remedio', max_length = 1, choices = TIPO)
    data_registrado = models.DateTimeField(verbose_name = "Horário do registro", auto_now_add = True)
    
    class Meta:
        verbose_name = "Remédio"
        verbose_name_plural = "Remédios"

    def __str__(self):
        return self.nome

class Receita(models.Model):
    medicoPaciente = models.ForeignKey(MedicoPaciente, on_delete = models.CASCADE, verbose_name = "Usuário", related_name = 'medicoPaciente_ReceitaFK')
    remedio = models.ForeignKey(Remedio, on_delete = models.CASCADE , verbose_name = "Remédio", related_name = 'remedio_ReceitaFK')
    intervalo = models.FloatField(verbose_name = "Intervalo")
    quantidade_dias = models.PositiveIntegerField(verbose_name = "Quantidade de dias", default = 0)
    data_inicio = models.DateField(verbose_name = "Data de Ínicio", auto_now = False, blank = True, null = True)
    dosagem = models.PositiveIntegerField(verbose_name = "Dosagem")
    data_registrado = models.DateTimeField(verbose_name = "Horário do registro", auto_now_add = True)

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"

    def __str__(self):
        return f"{self.medicoPaciente.paciente} - {self.remedio.nome}"

class Agendamento(models.Model):

    STATUS =[
        ("A", "Andamento"),
        ("C", "Concluido"),
    ]


    nome = models.CharField(verbose_name = "Nome do Agendamento:",max_length=194)
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE, verbose_name = "Receita:", related_name = 'receita_AgendamentoFK')
    horario_inicio = models.DateTimeField(verbose_name = "Horário inicio:",auto_now=False,blank=True,null=True)
    horario_termino = models.DateTimeField(verbose_name = "Horário término:",auto_now=False,blank=True,null=True)
    status = models.CharField(verbose_name = 'statusAgendamento', max_length = 1, choices = STATUS,default="A")
    reajuste = models.BooleanField(verbose_name = "Reajuste:",null=True)
    data_registrado = models.DateTimeField(verbose_name = "Horário do registro", auto_now_add = True)

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
        db_table = "agendamento"

    def __str__(self):
        return self.nome

class Horario_Agendamento(models.Model):
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE, verbose_name = "Agendamento:",related_name = 'agendamento_Horario_AgendamentoFK')
    horario = models.DateTimeField(verbose_name = "Horário:",auto_now = False,blank = True,null = True)
    concluido = models.BooleanField(verbose_name = "Concluído:", max_length = 194, null = True,default=False)
    data_hora_registro = models.DateTimeField("Horário registrado", auto_now_add = True)
    
    class Meta:
        verbose_name = "Horário do Agendamento"
        verbose_name_plural = "Horários dos Agendamentos"
        db_table = "horario_agendamento"

    def __str__(self):
        return str(self.horario)
