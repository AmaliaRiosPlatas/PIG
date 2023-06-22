from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Veterinaria (models.Model):
    nombre = models.CharField(max_length=30, verbose_name= 'Veterinaria')
    direccion = models.CharField(max_length=30, verbose_name= 'Direccion')
    telefono = models.IntegerField(verbose_name='Telefono')
    def __str__(self):
        return f"{self.nombre}"
    

class Servicio (models.Model):
    #id = models.CharField(max_length=20, verbose_name= 'ID de Servicios')    #Aca lo mismo
    SERVICIOS_CHOICE=[
        ('CASTRACIONES', "Castraciones"),
        ('VACUNACION', "Vacunacion"),
        ('BANIO', "Baño"),
        ('PELUQUERIA', "Peluqueria"),
        ('CONSULTA', "Consulta"),
    ]
    nombreServicio = models.CharField(max_length=30, choices=SERVICIOS_CHOICE, verbose_name= 'Nombre del servicio')
    
    veterinaria = models.ManyToManyField(Veterinaria, verbose_name= 'Veterinaria')
        
    def __str__(self):
        return f"{self.nombreServicio}"
    

class Cliente (models.Model):
    usuario= models.OneToOneField(User,on_delete= models.CASCADE)
    nombre = models.CharField(max_length=30, verbose_name= 'Nombre')
    apellido = models.CharField(max_length=80, verbose_name= 'Apellido')
    telefono = models.IntegerField(verbose_name= 'Teléfono')
    domicilio = models.CharField(max_length=80, verbose_name= 'Domicilio')
    email = models.CharField(max_length=30, verbose_name= 'Email de contacto')
    dni = models.IntegerField(verbose_name= 'DNI')
    #mascota = models.CharField(max_length=30, verbose_name= 'Nombre de mascota')
    veterinaria = models.ForeignKey(Veterinaria, on_delete= models.CASCADE)
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.usuario}"
    
# class Usuario(models.Model):
#     cliente =models.ForeignKey(Cliente, on_delete= models.CASCADE)
#     usuario = models.CharField(max_length=30, verbose_name= 'Usuario')
#     contrasenia = models.CharField(max_length=30, verbose_name= 'Contraseña')
#     rol= models.CharField(max_length=30, verbose_name= 'Rol', default='cliente')

# class Vacuna (models.Model):
#     vacuna = models.CharField(max_length=30, verbose_name= 'Vacunas')

#     def __str__(self):
#         return f"vacunas: {self.vacunas}"


class Mascota (models.Model):
    #id = models.IntegerField(verbose_name='ID')    #No habria porque poner un ID
    nombre = models.CharField(max_length=50, verbose_name= 'Nombre')
    raza = models.CharField(max_length=50, verbose_name= 'Raza')
    edad = models.IntegerField(verbose_name= 'Edad')
    tamanio = models.CharField(max_length=50, verbose_name= 'Tamanio')
    # vacuna = models.ManyToManyField(Vacuna, verbose_name= 'Vacunas', blank=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, verbose_name= 'Cliente', on_delete= models.CASCADE)
    usuario= models.ForeignKey(User, on_delete= models.CASCADE)

    def getUsuario(self):
        return self.usuario
        

    # def get_absolute_url(self):
    #     return reverse('mascotas_list')
    
















    
    

