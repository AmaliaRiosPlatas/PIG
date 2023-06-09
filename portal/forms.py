from django.forms import ModelForm
from django import forms
from .models import Mascota

class ContactoForm(forms.Form):
    
    nombre = forms.CharField(label = 'Nombre', max_length=30, widget=forms.TextInput(attrs={"class":"Formulario_input"}))
    apellido = forms.CharField(label = 'Apellido', max_length=80, widget=forms.TextInput(attrs={'class':'Formulario_input'})) 
    telefono = forms.IntegerField(label = 'Teléfono', widget=forms.NumberInput(attrs={'class':'Formulario_input'})) 
    domicilio = forms.CharField(label = 'Domicilio', max_length=100, widget=forms.TextInput(attrs={'class':'Formulario_input'}))
    email = forms.EmailField(label = 'Email de contacto', widget=forms.EmailInput(attrs={'class':'Formulario_input'}))
    dni = forms.IntegerField(label = 'DNI', widget=forms.TextInput(attrs={'class':'Formulario_input'}))
    mascota = forms.CharField(label = 'Nombre de Mascota', max_length=80, widget=forms.TextInput(attrs={'class':'Formulario_input'}))
    asunto = forms.CharField(label = 'Asunto', max_length=1500, widget=forms.TextInput(attrs={'class':'Formulario_input'}))
    comentario = forms.CharField(label = 'Ingrese su comentario', widget=forms.TextInput(attrs={'class':'Formulario_input'}))


class NuevaMascota(forms.ModelForm):

    nombre=forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    raza=forms.CharField(label='Raza', widget=forms.TextInput(attrs={'class':'form-control'}))
    edad=forms.CharField(label='Edad', widget=forms.TextInput(attrs={'class':'form-control'}))
    tamanio=forms.CharField(label='Tamaño', widget=forms.TextInput(attrs={'class':'form-control'}))
    #cliente=request.user

    class Meta:
        model = Mascota
        fields = ['nombre','raza','edad','tamanio']