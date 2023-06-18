from django.urls import path
from logueo import views as logueo
#from django.contrib.auth.views import LoginView
#from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', logueo.iniSesion, name='login'),
    path('registro/', logueo.creaUsuario, name='registro'),
    path('logout/', logueo.cerrarSesion, name='cerrarSesion'),
]