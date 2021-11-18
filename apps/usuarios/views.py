from .models import *
from .forms import *
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    template_name = 'usuarios/signup/signup.html'
    form_class = UsuarioForm
