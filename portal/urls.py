from django.urls import path, include
from portal import views
from django.contrib.auth import views as auth_views

#from django.contrib.auth.views import LoginView
#from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('adopciones/', views.adopciones, name='adopciones'),
    path('contacto/', views.contacto, name='contacto'),   

    #path('turnos/', views.ServicioListView.as_view(), name='turnos'), 

    path('cliente_list/', views.ClienteListView.as_view(), name = 'cliente_list'),
    
    path('mascotas_list/', views.MascotasListView.as_view(), name = 'mascotas_list'),
    path('mascotas/', views.crearMascota, name='mascotas'),
    path('mascotas_editar/<int:pk>', views.MascotasUpdateView.as_view(), name='mascotas_editar'),
    path('mascotas_eliminar/<int:pk>', views.MascotasDeleteView.as_view(), name='mascotas_eliminar'),

    path('nuevoCliente/', views.crearCliente, name='nuevoCliente'),
    # path('editarCliente/<int:id_cliente>', views.editarCliente, name='editarCliente')

    # path('registro/', views.registro, name='registro'), 

   

    



   
]
