from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppEntrega.models import *
from AppEntrega.forms import *
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

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
        
def cerrar_sesion(request):
    logout(request)
    return redirect('home')
      
#Vistas para mostrar todas las pistas

def mostrarpistas(request):
    carreras = Carreras.objects.all()
    contexto = {"carreras":carreras}
    return render(request, "AppCrud/grandespremios.html", contexto)