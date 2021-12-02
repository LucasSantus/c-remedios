from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
import debug_toolbar

urlpatterns = [
    # ADMIN''
    path('admin/', admin.site.urls),

    # APP'S
    path('', include('home.urls')),
    path('', include('usuarios.urls')),
    path('', include('receitas.urls')),
    path('__debug__/', include(debug_toolbar.urls)),    

]