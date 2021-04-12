from django.contrib import admin
from .models import Agendamento, Horario_Agendamento

admin.site.register(Agendamento)
admin.site.register(Horario_Agendamento)