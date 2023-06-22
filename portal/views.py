
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from django.http import HttpResponseNotAllowed

from portal.forms import ContactoForm, ClienteForm, NuevaMascotaForm, ServicioForm
from django.contrib.auth.mixins import LoginRequiredMixin


from portal.models import Cliente, Mascota

from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from django.core.mail import send_mail
from django.conf import settings




def sacarTurno(request):
    if request.method=='GET':
        context={'form1':ServicioForm}
        return render(request, 'portal/turnos.html', context)
    elif request.method=='POST':
        usuario=request.user
        veterinaria=request.POST.get("veterinaria")
        nombreServicio=request.POST.get("nombreServicio")
        date=request.POST.get("date")
        comentario=request.POST.get("comentario")            
        try:
            send_mail("Solicitud Turno","El usuario: {usuario}, del a veterinaria: {veterinaria},solicita{nombreServicio}, para el día{date} y escribe el siguiente mensaje:{comentario}","{usuario}",["to@example.com"],fail_silently=False)
            return redirect('mascotas_list')
        except:
            context={'form1':ServicioForm,
                     'error':'El turno no fue enviado, comunicarse por telefono.'}
            return render(request, 'portal/turnos.html', context)


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



class ClienteListView(LoginRequiredMixin, ListView):
    login_url = '/log'
    redirect_field_name = 'redirect_to'
    model = Cliente
    template_name = 'portal/cliente_list.html'

    def get_queryset(self, *args, **kwargs):
        return Mascota.objects.filter(usuario=self.request.user)



class MascotasListView(LoginRequiredMixin, ListView):
    login_url = '/log'
    redirect_field_name = 'redirect_to'
    model = Mascota    
    template_name = 'portal/mascotas_list.html'

    def get_queryset(self, *args, **kwargs):
        return Mascota.objects.filter(usuario=self.request.user)
    


class MascotasUpdateView(UpdateView):
    model = Mascota
    form_class = NuevaMascotaForm
    template_name = 'portal/mascotas.html'
    success_url = reverse_lazy('mascotas_list')



class MascotasDeleteView(DeleteView):
    model = Mascota
    template_name = 'portal/mascotas_eliminar.html'
    success_url = reverse_lazy('mascotas_list')


def crearCliente(request):
    if request.method=='GET':
        context={'form':ClienteForm}
        return render (request, 'portal/nuevoCliente.html', context)
    elif request.method=='POST':
        try:
            form = ClienteForm(request.POST)
            nuevoCliente = form.save(commit=False)
            nuevoCliente.usuario=request.user
            nuevoCliente.save()
            return redirect('mascotas_list')
        except:
           context={'form':ClienteForm,
                    'error':'Algo salio mal!!!'}
           return render (request, 'portal/nuevoCliente.html', context)
 
def crearMascota(request):
    if request.method=='GET':
        context={'form':NuevaMascotaForm}
        return render(request, 'portal/mascotas.html', context)
    elif request.method=='POST':
        form = NuevaMascotaForm(request.POST)
        nuevaMascota=form.save(commit=False)
        nuevaMascota.usuario=request.user
        nuevaMascota.save()
        return redirect('mascotas_list')
    







