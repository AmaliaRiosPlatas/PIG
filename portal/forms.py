from django.forms import ModelForm
from django import forms
from .models import Mascota, Cliente



class ContactoForm(forms.Form):
    
    nombre = forms.CharField(label = 'Nombre', max_length=30)
    apellido = forms.CharField(label = 'Apellido', max_length=80, widget=forms.TextInput(attrs={'class':'Formulario_input'})) 
    telefono = forms.IntegerField(label = 'Teléfono', widget=forms.NumberInput(attrs={'class':'Formulario_input'})) 
    domicilio = forms.CharField(label = 'Domicilio', max_length=100, widget=forms.TextInput(attrs={'class':'Formulario_input'}))
    email = forms.EmailField(label = 'Email de contacto', widget=forms.EmailInput(attrs={'class':'Formulario_input'}))
    dni = forms.IntegerField(label = 'DNI', widget=forms.TextInput(attrs={'class':'Formulario_input'}))
    mascota = forms.CharField(label = 'Nombre de Mascota', max_length=80, widget=forms.TextInput(attrs={'class':'Formulario_input'}))
    asunto = forms.CharField(label = 'Asunto', max_length=1500, widget=forms.TextInput(attrs={'class':'Formulario_input'}))
    comentario = forms.CharField(label = 'Ingrese su comentario', widget=forms.TextInput(attrs={'class':'Formulario_input'}))


class NuevaMascotaForm(forms.ModelForm):

    #nombre=forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    #raza=forms.CharField(label='Raza', widget=forms.TextInput(attrs={'class':'form-control'}))
    #edad=forms.CharField(label='Edad', widget=forms.TextInput(attrs={'class':'form-control'}))
    #tamanio=forms.CharField(label='Tamaño', widget=forms.TextInput(attrs={'class':'form-control'}))
    #cliente=request.user

    class Meta:
        model = Mascota
        fields = ['nombre','raza','edad','tamanio']
        labels = {'nombre':'Nombre', 'raza':'Raza', 'edad':'Edad', 'tamanio':'Tamaño'}
        widgets = {
            'nombre': forms.TextInput(attrs={'class':''}),
            'raza': forms.TextInput(attrs={'class':''}),
            'edad': forms.TextInput(attrs={'class':''}),
            'tamanio': forms.TextInput(attrs={'class':''}),
            'vacunas': forms.Select(attrs={'class':''}),
            'veterinaria': forms.Select(attrs={'class':''}),
        }


class LoginForm(forms.Form):
    usuario=forms.CharField(label="Usuario", max_length=50, widget=forms.TextInput(attrs={'class':'usuario'}))
    contrasenia=forms.CharField(label="Contraseña", max_length=50, widget=forms.TextInput(attrs={'class':'contrasenia'}))


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'domicilio', 'email', 'dni', 'veterinaria', 'usuario', 'contrasenia']
        widgets ={
            'nombre': forms.TextInput(attrs={'class':''}),
            'apellido': forms.TextInput(attrs={'class':''}),
            'telefono': forms.TextInput(attrs={'class':''}),
            'domicilio': forms.TextInput(attrs={'class':''}),
            'email': forms.EmailInput(attrs={'class':''}),
            'dni': forms.TextInput(attrs={'class':''}),
            'veterinaria': forms.Select(attrs={'class':''}),
            'usuario': forms.TextInput(attrs={'class':''}),
            'contrasenia': forms.PasswordInput(attrs={'class':''}),

        }

