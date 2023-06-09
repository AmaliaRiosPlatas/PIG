from django.db import models

# Create your models here.

class Veterinaria (models.Model):
    nombre = models.CharField(max_length=30, verbose_name= 'Veterinaria')
    direccion= models.CharField(max_length=30, verbose_name= 'Direccion')
    telefono= models.IntegerField(verbose_name='Telefono')
    # direccion u otros datos de local... 


class Cliente (models.Model):
    nombre = models.CharField(max_length=30, verbose_name= 'Nombre')
    apellido = models.CharField(max_length=80, verbose_name= 'Apellido')
    telefono = models.IntegerField(verbose_name= 'Teléfono')
    domicilio = models.CharField(max_length=80, verbose_name= 'Domicilio')
    email = models.CharField(max_length=30, verbose_name= 'Email de contacto')
    dni = models.IntegerField(verbose_name= 'DNI')
    #mascota = models.CharField(max_length=30, verbose_name= 'Nombre de mascota')
    veterinaria = models.ForeignKey(Veterinaria, on_delete= models.CASCADE)



class Mascota (models.Model) :
    #id = models.IntegerField(verbose_name='ID')    #No habria porque poner un ID
    nombre=models.CharField(max_length=50, verbose_name= 'Nombre')
    raza = models.CharField(max_length=50, verbose_name= 'Raza')
    edad = models.IntegerField(verbose_name= 'Edad')
    tamanio = models.ImageField(verbose_name= 'Tamanio')
    cliente = models.ForeignKey(Cliente, verbose_name= 'Cliente', on_delete= models.CASCADE)   # le falta aclarar con quien esta conectado


class Servicios (models.Model) :
    #id = models.CharField(max_length=20, verbose_name= 'ID de Servicios')    #Aca lo mismo
    nombreServicio = models.CharField(max_length=30, verbose_name= 'Nombre del servicio')
    servicio = models.ManyToManyField(Veterinaria)     #(Mascota)














    
    

