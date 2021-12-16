from django.contrib import admin
from .models import *

class CidadeAdmin(admin.ModelAdmin): 
    # list_filter = ['descricao']
    # search_fields = ('codigo_IBGE','descricao')
    view_on_site = False

admin.site.register(Usuario)
admin.site.register(Estado)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(MedicoPaciente)
