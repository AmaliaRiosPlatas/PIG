from django.forms import ModelForm
from django import forms
from .models import Mascota, Cliente, Servicio


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
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'raza': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'tamanio': forms.TextInput(attrs={'class':'form-control'}),
            #'vacunas': forms.Select(attrs={'class':''}),
            'veterinaria': forms.Select(attrs={'class':'form-control'}),
        }


# class LoginForm(forms.Form):
#     usuario=forms.CharField(label="Usuario", max_length=50, widget=forms.TextInput(attrs={'class':'usuario'}))
#     contrasenia=forms.CharField(label="Contraseña", max_length=50, widget=forms.TextInput(attrs={'class':'contrasenia'}))


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'domicilio', 'email', 'dni', 'veterinaria']
        labels = {'nombre':'Nombre', 'apellido':'Apellido', 'telefono':'Telefono', 'domicilio':'Domicilio', 'email':'E-mail', 'dni':'DNI', 'veterinaria':'Sucursal'}
        widgets ={
            
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'dni': forms.NumberInput(attrs={'class':'form-control'}),
            'veterinaria': forms.Select(attrs={'class':'form-control'}),
           }
        


#class ServicioForm(forms.ModelForm):
#    class Meta:
#        model = Servicio
#        fields = ['nombreServicio', 'veterinaria']
#        labels = {'nombreServicio':'Servicio', 'veterinaria':'Veterinaria'}
#        widgets = {
#            'nombreServicio': forms.Select(attrs={'class':''}),
#            'veterinaria': forms.Select(attrs={'class':''}),
#       }
        


# class UsuarioForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ['usuario', 'contrasenia']
#         labels = {'usuario':'Usuario', 'contrasenia':'Contraseña'}

