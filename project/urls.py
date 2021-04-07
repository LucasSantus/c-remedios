from django.contrib import admin
from django.urls import path, include
from cadastro.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('', include('home.urls')),
    path('cadastro/', include('cadastro.urls')),
    path('administracao/', include('administracao.urls')),
]