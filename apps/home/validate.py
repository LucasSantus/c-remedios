from django.contrib.auth.models import Group
from usuarios.models import Usuario
from django.http import JsonResponse

# Validar se o usuário está cadastrado.
def validate_user(request):
    user = request.GET.get('username', None)
    data = {
        'is_user': Usuario.objects.filter(email__iexact=user).exists(),
    }
    if not data['is_user']:
        data['error_message'] = 'Este e-mail não está cadastrado!'
    return JsonResponse(data)

def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_email': Usuario.objects.filter(email__iexact=email).exists(),
    }
    if data['is_email']:
        data['error_message'] = 'Este e-mail já está cadastrado!'
    return JsonResponse(data)

def validate_email_registered(request):
    email = request.GET.get('email', None)
    data = {
        'is_email_registered': Usuario.objects.filter(email__iexact=email).exists(),
    }
    
    if not data['is_email_registered']:
        data['error_message'] = 'Este e-mail não está cadastrado no sistema!'
    return JsonResponse(data)

def RetornaGrupo(request):
    objUsuario = request.user
    try:
        objGrupo = objUsuario.groups.get(pk=objUsuario.idGroup)
    except Group.DoesNotExist:
        listGroups = objUsuario.groups.all()
        objGrupo = listGroups[0]
        objUsuario.idGroup = objGrupo.id
        objUsuario.save()
    return objGrupo