
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template import loader
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from portal.forms import ContactoForm, ClienteForm, NuevaMascotaForm, ServicioForm
from django.contrib.auth.mixins import LoginRequiredMixin


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

#def turnos(request):
#    return render(request,'portal/turnos.html')


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


# def login(request):
#     if(request.method == 'POST'):
#         mensaje = None
#         login_form = LoginForm(request.POST)
#         mensaje = 'Tu mensaje ha sido enviado. Te responderemos a la brevedad'
#     elif request.method == 'GET':
#         login_form = LoginForm()
#     else:
#         return HttpResponseNotAllowed(f"Metodo {request.method} no soportado")  
#     context = {
#         'login_form' : login_form
#     }
#     return render(request,'portal/login.html', context)
# def inicioSesion(request):
#     if request.method == 'GET':
#         return render(request, 'portal/login.html',{'form': UsuarioForm})
#     elif  request.method=='POST':
#         user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
#         # print(user)
#         # print(request.POST)
#         if user is None:
#          return render(request, 'portal/login.html',{
#             'form': UsuarioForm,
#             'error': 'Usuario o contraseña incorrecta'})
#         else:
#             login(request, user)
#             return redirect('')


#def login(request):
#    if request.method == 'POST':
#        form = LoginForm(request.POST)
#        if form.is_valid():
#            form.save()
#        return redirect('mascotas_list')
#    else:
#        form = LoginForm()
    
#    return render(request,'portal/login.html', {'form':form})

# def registro(request):
#     if request.method=='GET':
#         context={'form1':UsuarioForm,
#                 'form2':ClienteForm
#                 }
#         return render(request,'portal/registro.html', context)
#     elif request.method=='POST':
#         try:
#             form1=UsuarioForm(request.POST)
#             print(form1)
#             form2=ClienteForm(request.POST)
#             print(form2)
#             if form1.is_valid() and form2.is_valid():
#                 form1.save()
#                 form2.save()
#                 return redirect('login')
#         except:
#              context={'form1':UsuarioForm,
#                 'form2':ClienteForm,
#                 'error':'Algo salió mal'
#                 }
#         return render(request,'portal/registro.html', context)
#     else:
#         context={'form1':UsuarioForm,
#                 'form2':ClienteForm,
#                 'error':'no funciona'
#                 }
#         return render(request,'portal/registro.html', context)
        


    
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
    

    # def get_context_data(self, **kwargs):
    #     context = super(MascotasListView, self).get_context_data(**kwargs)
    #     queryset = Mascota.objects.filter(usuario=self.request.user)
    #     context['mascota'] = queryset
    #     return context
    
    # def get_queryset(self):
    #     if self.request.GET.get('mascota') is not None:
    #         return Mascota.objects.filter(
    #             hostname__startswith = self.request.GET['mascota']
    #         )

    #     return super().get_queryset()

# def MascotasListView(request):
#     mascotas=Mascota.objects.all()
#     return render(request, 'portal/mascotas_list.html', {'mascotas':mascotas})
    

#class ServicioListView(ListView):
#    model = Servicio
#    form_class = ServicioForm
#    template_name = 'portal/turnos.html'
#    success_url = reverse_lazy('mascotas_list')


class MascotasUpdateView(UpdateView):
    model = Mascota
    form_class = NuevaMascotaForm
    template_name = 'portal/mascotas.html'
    success_url = reverse_lazy('mascotas_list')


class MascotasDeleteView(DeleteView):
    model = Mascota
    template_name = 'portal/mascotas_eliminar.html'
    success_url = reverse_lazy('mascotas_list')

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'portal/nuevoCliente.html'
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
        
# def editarCliente(request, id_cliente):
#     if request.method=='GET':
#         cliente=Cliente.objects.get(pk=id_cliente)
#         form=ClienteForm(instance=cliente)
#         context = {'cliente':cliente, 'form':form}
#         return render(request, 'portal/editarCliente.html', context)
#     elif request.method=='POST':
#         try:
#             cliente=Cliente.objects.get(pk=id_cliente)
#             form=ClienteForm(request.POST, instance=cliente)
#             if form.is_valid():
#                 form.save()
#                 return redirect('mascotas_list')
#         except:
#             cliente=Cliente.objects.get(pk=id_cliente)
#             form=ClienteForm(instance=cliente)
#             context = {'cliente':cliente, 'form':form, 'error':'Algun dato es invalido'}
#             return render(request, 'portal/editarCliente.html', context)


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
    
def sacarTurno(request):
    context={'form1':ServicioForm}
    return render(request, 'portal/turnos.html', context)






