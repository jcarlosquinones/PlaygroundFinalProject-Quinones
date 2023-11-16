from django.shortcuts import render
from django.http import HttpResponse
from AppEntrega.models import *
from AppEntrega.forms import *

# Create your views here.

def inicio(request):
    return render(request, "AppEntrega/index.html")

def aboutme(request):
    return render(request, "AppEntrega/aboutme.html")

def grandespremios(request):
    return render(request, "AppCrud/grandespremios.html")

def pilotos(request):
    return render(request, "AppEntrega/pilotos.html")

def opcionespiloto(request):
    return render(request, "AppEntrega/opcionespiloto.html")

def buscarpiloto(request):
    return render(request, "AppEntrega/buscarpiloto.html")

def carreras(request):
    return render(request, "AppEntrega/carreras.html")

def opcionescarreras(request):
    return render(request, "AppEntrega/opcionescarreras.html")

def contacto(request):
    return render(request, "AppEntrega/contacto.html")

def ingreso(request):
    return render(request, "AppEntrega/ingreso.html")

#Vistas de los formularios

def pilotoForm(request):
    if request.method == 'POST':
        mi_Formulario = IngresoPiloto(request.POST)
        print(mi_Formulario)
        if mi_Formulario.is_valid():
            nuevopiloto = mi_Formulario.cleaned_data
            nuevopiloto = Piloto(nombre=nuevopiloto['nombre'], apellido=nuevopiloto['apellido'], escuderia=nuevopiloto['escuderia'])
            nuevopiloto.save()
            return render(request, "AppEntrega/index.html")
    else:
        mi_Formulario = IngresoPiloto()  
        return render(request, "AppEntrega/pilotos.html", {"mi_Formulario":mi_Formulario})

def carreraForm(request):
    if request.method == 'POST':
        mi_Formulario = NuevaCarrera(request.POST)
        print(mi_Formulario)
        if mi_Formulario.is_valid():
            nuevapista = mi_Formulario.cleaned_data
            nuevapista = Carreras(pista=nuevapista['pista'], pais=nuevapista['pais'], vueltas=nuevapista['vueltas'])
            nuevapista.save()
            return render(request, "AppEntrega/index.html")
    else:
        mi_Formulario = NuevaCarrera()
        return render(request, "AppEntrega/carreras.html", {"mi_Formulario":mi_Formulario})
    
def contactForm(request):
    if request.method == 'POST':
        mi_Formulario = contactoForm(request.POST)
        print(mi_Formulario)
        if mi_Formulario.is_valid():
            contactonuevo = mi_Formulario.cleaned_data
            contactonuevo = Contacto(nombre=contactonuevo['nombre'], apellido=contactonuevo['apellido'], correo=contactonuevo['correo'], comentario=contactonuevo['comentario'])
            contactonuevo.save()
            return render(request, "AppEntrega/index.html")
    else:
        mi_Formulario = contactoForm()
        return render(request, "AppEntrega/contacto.html", {"mi_Formulario":mi_Formulario})


#Vistas de la busqueda

def buscar(request):
    if request.GET["escuderia"]:
        escuderia=request.GET["escuderia"]
        busquedapilotos=Piloto.objects.filter(escuderia__icontains=escuderia)
        return render(request, "AppEntrega/mostrarpilotos.html", {"busquedapilotos":busquedapilotos, "escuderia":escuderia})
    else:
        return HttpResponse("No haz ingresado ninguna escuderia")    