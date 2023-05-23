from django.db import models

# Create your models here.

class Veterinaria (models.Model):
    nombre = models.CharField(max_length=30, verbose_name= 'Veterinaria')


class Cliente (models.Model):
    nombre = models.CharField(max_length=30, verbose_name= 'Nombre')
    apellido = models.CharField(max_length=80, verbose_name= 'Apellido')
    telefono = models.IntegerField(verbose_name= 'Teléfono')
    domicilio = models.CharField(max_length=80, verbose_name= 'Domicilio')
    email = models.CharField(max_length=30, verbose_name= 'Email de contacto')
    dni = models.IntegerField(verbose_name= 'DNI')
    mascota = models.CharField(max_length=30, verbose_name= 'Nombre de mascota')
    veterinaria = models.ForeignKey(Veterinaria, on_delete= models.CASCADE)



class Mascota (models.Model) :
    id = models.IntegerField(verbose_name='ID')
    raza = models.CharField(max_length=50, verbose_name= 'Raza')
    edad = models.IntegerField(verbose_name= 'Edad')
    tamaño = models.ImageField(verbose_name= 'Tamaño')
    cliente = models.ForeignKey(verbose_name= 'Cliente', on_delete= models.CASCADE)


class Servicios (models.Model) :
    id = models.CharField(max_length=20, verbose_name= 'ID de Servicios')
    mascotas = models.ManyToManyField(Mascota)














    
    

