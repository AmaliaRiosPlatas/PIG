from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template import loader

from portal.forms import ContactoForm

# Create your views here.

def index(request):
    
    return render(request,'portal/index.html')

def servicios(request):
    
    return render(request,'portal/servicios.html')

def adopciones(request):
    return render(request,'portal/adopciones.html')


def contacto(request):

    if(request.method == 'POST'):
        mensaje = None
        contacto_form = ContactoForm(request.POST)
        mensaje = 'Tu mensaje ha sido enviado. Te responderemos a la brevedad'

    elif request.method == 'GET':
        contacto_form = ContactoForm()

    else:
        return HttpResponseNotAllowed(f"Metodo {request.method} no soportado")
    

    context = {
        'contacto_form' : contacto_form
    }

    return render(request,'portal/contacto.html', context)


    
# def probarBase(request):
#     return render (request, 'base.html')

