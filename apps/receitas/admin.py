from django.contrib import admin
from .models import *

admin.site.register(Remedio)
admin.site.register(Receita)
admin.site.register(Agendamento)
admin.site.register(Horario_Agendamento)