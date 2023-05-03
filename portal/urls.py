from django.urls import path
from portal import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('adopciones/', views.adopciones, name='adopciones'),
    path('contacto/', views.contacto, name='contacto'),    
]
