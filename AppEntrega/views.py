from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppEntrega.models import *
from AppEntrega.forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#Vistas Generales
def inicio(request):
    return render(request, "AppEntrega/index.html")

def aboutme(request):
    return render(request, "AppEntrega/aboutme.html")

@login_required
def grandespremios(request):
    return render(request, "AppCrud/grandespremios.html")

@login_required
def pilotos(request):
    return render(request, "AppEntrega/pilotos.html")

@login_required
def opcionespiloto(request):
    return render(request, "AppEntrega/opcionespiloto.html")

@login_required
def buscarpiloto(request):
    return render(request, "AppEntrega/buscarpiloto.html")

@login_required
def carreras(request):
    return render(request, "AppEntrega/carreras.html")

@login_required
def opcionescarreras(request):
    return render(request, "AppEntrega/opcionescarreras.html")

@login_required
def contacto(request):
    return render(request, "AppEntrega/contacto.html")

#Vistas para Iniciar Sesion
def ingreso(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contrasena=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contrasena)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request,"Usuario Incorrecto") 
        else:
            messages.error(request,"Usuario Incorrecto")  
    form=AuthenticationForm()
    return render(request, "AppEntrega/ingreso.html", {"form":form})

#Vistas de los formularios

@login_required
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

@login_required
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
 
@login_required   
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

@login_required
def buscar(request):
    if request.GET["escuderia"]:
        escuderia=request.GET["escuderia"]
        busquedapilotos=Piloto.objects.filter(escuderia__icontains=escuderia)
        return render(request, "AppEntrega/mostrarpilotos.html", {"busquedapilotos":busquedapilotos, "escuderia":escuderia})
    else:
        return HttpResponse("No haz ingresado ninguna escuderia")    