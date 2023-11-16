from django.shortcuts import render
from django.http import HttpResponse
from AppEntrega.models import *
from AppEntrega.forms import *

#Vistas para mostrar todas las pistas

def mostrarpistas(request):
    grandespremios= Carreras.objects.all()
    contexto = {"grandespremios":grandespremios}
    return render(request, "AppCrud/grandespremios.html", contexto)