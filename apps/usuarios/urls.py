from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    # SIGN UP
    path('usuario/signup/', SignUpView.as_view(), name='signup'),
    
    # LOGIN
    path("usuario/login/", auth_views.LoginView.as_view(template_name="usuarios/login/login.html"), name="login"),
    
    # LOGOUT
    path("usuario/logout/", auth_views.LogoutView.as_view(template_name="usuarios/logout/logout.html"), name="logout"),
    
    # PROFILE
    path('usuario/perfil/', perfil, name='perfil'),

    # RESET PASSWORD
    path('usuario/password/reset/sent/', auth_views.PasswordResetDoneView.as_view(template_name="usuarios/reset_password/reset-password-done.html"), name="password_reset_done"),
    path('usuario/password/reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="usuarios/reset_password/reset-password-confirm.html"), name="password_reset_confirm"),
    path('usuario/password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name="usuarios/reset_password/reset-password-complete.html"), name="password_reset_complete"),
    path('usuario/password/reset/', auth_views.PasswordResetView.as_view(template_name="usuarios/reset_password/reset-password.html"), name="reset_password"),
]