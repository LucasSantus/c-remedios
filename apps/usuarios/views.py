from .models import *
from .forms import *
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

class SignUpView(CreateView):
    template_name = 'usuarios/signup/signup.html'
    form_class = UsuarioForm

@login_required
def perfil(request):
    form = UsuarioForm()
    context = {
        "form" : form,
    }
    return render(request, "usuarios/perfil/perfil.html", context)
