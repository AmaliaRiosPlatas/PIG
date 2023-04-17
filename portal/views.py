from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'titulo' : 'Inicio'}
    return render(request,'index.html', context)

def servicios(request):
    context = {'titulo' : 'Inicio'}
    return render(request,'servicios.html', context)

def adopciones(request):
    return render(request,'adopciones.html')

def contacto(request):
    return render(request,'contacto.html')
    
# def probarBase(request):
#     return render (request, 'base.html')

