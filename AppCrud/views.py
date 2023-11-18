from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCrud.forms import *
from AppEntrega.models import *
from AppEntrega.forms import *
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator

#Vistas para Registrar y Cerrar Sesion

class Registro(View):
    
    def get(self,request):
        form=UserCreationForm()
        return render(request, "AppCrud/registro.html", {"form":form})
    
    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "AppCrud/registro.html", {"form":form})
        
@login_required 
def cerrar_sesion(request):
    logout(request)
    return redirect('home')
      
#Vistas para mostrar todas las pistas
@login_required
def mostrarpistas(request):
    carreras = Carreras.objects.all()
    contexto = {"carreras":carreras}
    return render(request, "AppCrud/grandespremios.html", contexto)

#Vistas para mostrar perfil y editar

# def perfil(request):
#     return render(request, "AppCrud/perfil.html")


class PerfilView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = PerfilForm
    template_name = "AppCrud/perfil.html"
    success_url = reverse_lazy("AppEntrega/index.html")

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return render(request,"AppEntrega/index.html",{'data':data})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Perfil'
        context['entity'] = 'Perfil'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context