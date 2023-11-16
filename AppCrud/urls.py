from django.urls import path
from AppCrud.views import *
from AppEntrega.views import *

urlpatterns = [
    path('grandespremios/', grandespremios, name="grandespremios"),
]