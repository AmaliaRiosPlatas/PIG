
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template import loader

from portal.forms import ContactoForm, ClienteForm, NuevaMascotaForm
from portal.forms import LoginForm

from portal.models import Cliente, Mascota

from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


from django.http import HttpResponseRedirect




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


def login(request):

    if(request.method == 'POST'):
        mensaje = None
        login_form = LoginForm(request.POST)
        mensaje = 'Tu mensaje ha sido enviado. Te responderemos a la brevedad'
    elif request.method == 'GET':
        login_form = LoginForm()
    else:
        return HttpResponseNotAllowed(f"Metodo {request.method} no soportado")  

    context = {
        'login_form' : login_form
    }
    return render(request,'portal/login.html', context)


#def login(request):
#    if request.method == 'POST':
#        form = LoginForm(request.POST)
#        if form.is_valid():
#            form.save()
#        return redirect('mascotas_list')
#    else:
#        form = LoginForm()
    
#    return render(request,'portal/login.html', {'form':form})

def registro(request):
    return render(request,'registro.html')




    
# def probarBase(request):
#     return render (request, 'base.html')

def mascotas(request):
    if request.method == 'POST':
        form = NuevaMascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascotas_list')
    else:
        form = NuevaMascotaForm()
    
    return render(request,'portal/mascotas.html', {'form':form})


class RegistroUsuario(CreateView):
    model = Cliente
    template_name = 'portal/registro.html'
    form_class = ClienteForm
    success_url = reverse_lazy('mascotas_list')


class MascotasListView(ListView):
    model = Mascota
    template_name = 'portal/mascotas_list.html'
    

class MascotasCreateView(CreateView):
    model = Mascota
    form_class = NuevaMascotaForm
    template_name = 'portal/mascotas.html'
    succese_url = reverse_lazy('mascotas_list_view')


class MascotasUpdateView(UpdateView):
    model = Mascota
    form_class = NuevaMascotaForm
    template_name = 'portal/mascotas_editar.html'
    #succese_url = reverse_lazy('mascotas_list')


class MascotasDeleteView(DeleteView):
    model = Mascota
    template_name = 'portal/mascotas_eliminar.html'
    #succese_url = reverse_lazy('mascotas_list')







