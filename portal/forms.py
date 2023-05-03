from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label = 'Nombre', max_length=30)
    apellido = forms.CharField(label = 'Apellido', max_length=80)
    email = forms.EmailField(label = 'Email de contacto')
    asunto = forms.CharField(label = 'Asunto', max_length=1500)
    comentario = forms.CharField(label = 'Ingrese su comentario')

