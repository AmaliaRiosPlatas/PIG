from django.contrib import admin
from .models import Servicio, Veterinaria

# Register your models here.

admin.site.register(Servicio)
admin.site.register(Veterinaria)
# admin.site.register(Vacuna)