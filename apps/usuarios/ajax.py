from .models import Estado,Cidade
from django.http import HttpResponse
from django.core import serializers

def AjaxRetornaCidade(request):
    Sigla = request.GET.get('UF', None)
    estado = Estado.objects.get(sigla=Sigla)
    ListCidades = Cidade.objects.select_related('estado').filter(estado=estado).order_by("descricao")
    data = serializers.serialize('json', ListCidades)
    return HttpResponse(data, content_type="application/json")