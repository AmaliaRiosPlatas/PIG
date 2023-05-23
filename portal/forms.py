from django import forms

class ContactoForm(forms.Form):
    """ cambio 21/5 """
    nombre = forms.CharField(label = 'Nombre', max_length=30, widget=forms.TextInput(attrs={'class':'Formulario_input'}))
    apellido = forms.CharField(label = 'Apellido', max_length=80, widget=forms.TextInput(attrs={'class':'Formulario_input'})) 
    telefono = forms.IntegerField(label = 'Teléfono', widget=forms.NumberInput(attrs={'class':'Formulario_input'})) 
    domicilio = forms.CharField(label = 'Domicilio', max_length=100, widget=forms.TextInput(attrs={'class':'Formulario_input'}))
    email = forms.EmailField(label = 'Email de contacto', widget=forms.EmailInput(attrs={'class':'Formulario_input'}))
    dni = forms.IntegerField(label = 'DNI', widget=forms.TextInput(attrs={'class':'Formulario_input'}))
    mascota = forms.CharField(label = 'Nombre de Mascota', max_length=80, widget=forms.TextInput(attrs={'class':'Formulario_input'}))
    asunto = forms.CharField(label = 'Asunto', max_length=1500, widget=forms.TextInput(attrs={'class':'Formulario_input'}))
    comentario = forms.CharField(label = 'Ingrese su comentario', widget=forms.TextInput(attrs={'class':'Formulario_input'}))


