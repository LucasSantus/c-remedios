from django.contrib import messages
from .models import *
from .forms import *
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

class SignUpView(CreateView):
    template_name = 'usuarios/signup/signup.html'
    form_class = UsuarioForm

@login_required
def perfil(request):
    form = UsuarioForm(instance = request.user)
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Receita registrado com sucesso!")
            return redirect("perfil")
            
    context = {
        "form" : form,
    }

    return render(request, "usuarios/perfil/perfil.html", context)
