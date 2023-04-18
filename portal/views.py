from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request,'portal/index.html')

def servicios(request):
    
    return render(request,'portal/servicios.html')

def adopciones(request):
    return render(request,'portal/adopciones.html')

def contacto(request):
    return render(request,'portal/contacto.html')
    
# def probarBase(request):
#     return render (request, 'base.html')

