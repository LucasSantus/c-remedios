from django.contrib import admin
from .models import Receita, Agendamento, Horario_Agendamento

admin.site.register(Receita)
admin.site.register(Agendamento)
admin.site.register(Horario_Agendamento)