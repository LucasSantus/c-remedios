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
    objUser = request.user
    form = PerfilForm(instance=objUser)
    
    if request.method == "POST":
        form = PerfilForm(request.POST,instance=objUser)
        print("aqui")
        if form.is_valid():
            print("é valido")
            objUser = form.save()

            messages.success(request, "Receita registrado com sucesso!")
            return redirect("perfil")
        else:
            print(form.errors.as_data)
    context = {
        "form" : form,
    }

    return render(request, "usuarios/perfil/perfil.html", context)
