from django.urls import path
from AppCrud.views import *
from AppEntrega.views import *

urlpatterns = [
    path('grandespremios/', mostrarpistas, name="grandespremios"),
    path('registro/', Registro.as_view(), name="registro"),
    path('cerrarsesion/', cerrar_sesion, name="cerrar_sesion"),
    path('perfil/', perfil, name="perfil"),
]