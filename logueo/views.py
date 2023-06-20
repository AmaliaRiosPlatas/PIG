from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse



def iniSesion(request):
    if request.method == 'GET':
        return render(request, 'logueo/login.html',{'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(user)
        print(request.POST)
        if user is None:
         return render(request, 'logueo/login.html',{
            'form': AuthenticationForm,
            'error': 'Usuario o contraseña incorrecta'})
        else:
            login(request, user)
            return redirect('mascotas_list')
        
def creaUsuario(request):
    if request.method == 'GET':
        return render(request, 'logueo/registro.html', {'form': UserCreationForm})
    else:
        if request.POST ['password1'] == request.POST ['password2']:
           # print(request.POST)
           # try:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('nuevoCliente')
        #    except:
        #        return render (request, 'creaUsuario.html' ,{'form':UserCreationForm, 'error':'El usuario ya existe'})
        return render (request, 'logueo/registro.html' ,{'form':UserCreationForm, 'error':'Las contraseñas no coinciden'})
    
def cerrarSesion(request):
    logout(request)
    return redirect('inicio')