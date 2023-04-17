from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request,'index.html')

def servicios(request):
    
    return render(request,'servicios.html')

def adopciones(request):
    return render(request,'adopciones.html')

def contacto(request):
    return render(request,'contacto.html')
    
# def probarBase(request):
#     return render (request, 'base.html')

