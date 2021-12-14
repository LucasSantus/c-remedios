from django.contrib import admin
from .models import Usuario,Estado,Cidade

class CidadeAdmin(admin.ModelAdmin): 
    # list_filter = ['descricao']
    # search_fields = ('codigo_IBGE','descricao')
    view_on_site = False

admin.site.register(Usuario)
admin.site.register(Estado)
admin.site.register(Cidade, CidadeAdmin)