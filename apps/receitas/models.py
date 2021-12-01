from django.db import models

class Remedio(models.Model):
    nome = models.CharField(verbose_name = "Nome", max_length = 100)
    descricao = models.TextField(verbose_name = "Descrição", max_length = 340)
    data_hora_registrado = models.DateTimeField("Horário registrado", auto_now_add = True)
    
    class Meta:
        verbose_name = "Remédio"
        verbose_name_plural = "Remédios"

    def __str__(self):
        return self.nome

class Receita(models.Model):
    usuario = models.ForeignKey("usuarios.Usuario", on_delete = models.CASCADE, verbose_name = "Usuário", related_name = 'usuario_ReceitaFK')
    remedio = models.ForeignKey(Remedio, on_delete = models.CASCADE , verbose_name = "Remédio", related_name = 'remedio_ReceitaFK')
    intervalo = models.FloatField(verbose_name = "Intervalo")
    quantidade_dias = models.PositiveIntegerField(verbose_name = "Quantidade de dias", default = 0)
    data_inicio = models.DateField(verbose_name = "Data de Ínicio", auto_now = False, blank = True, null = True)
    dosagem = models.PositiveIntegerField(verbose_name = "Dosagem")
    data_hora_registrado = models.DateTimeField("Horário registrado", auto_now_add = True)

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"

    def __str__(self):
        return f"{self.usuario.nome} - {self.remedio.nome}"
