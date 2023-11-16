from django.urls import path
from AppEntrega.views import *

urlpatterns = [
    path('', inicio,name= "home"),
    path('pilotos/', pilotos, name="pilotos"),
    path('carreras/', carreras, name="carreras"),
    path('contacto/', contactForm, name="contacto"),
    path('ingreso/', ingreso, name="ingreso"),
    path('nuevopiloto/', pilotoForm, name="nuevopiloto"),
    path('nuevacarrera/', carreraForm, name="nuevacarrera"),
    path('opcionespiloto/', opcionespiloto, name="opcionespiloto"),
    path('buscarpiloto/', buscarpiloto, name="buscarpiloto"),
    path('buscarpiloto/mostrarpilotos/',buscar),
    path('opcionescarreras/', opcionescarreras, name="opcionescarreras"),
    path('aboutme/', aboutme, name="aboutme"),
]