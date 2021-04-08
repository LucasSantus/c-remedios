from django.contrib import admin
from .models import Pessoa, Remedio, Receita

admin.site.register(Pessoa)
admin.site.register(Remedio)
admin.site.register(Receita)
