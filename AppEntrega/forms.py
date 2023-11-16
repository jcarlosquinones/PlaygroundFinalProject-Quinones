from django import forms
from AppEntrega.models import *
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm

class IngresoPiloto(forms.Form):
    nombre = forms.CharField(max_length=20, label="Nombre del Piloto", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese un nombre', "autocomplete":"off", 'required':'true' }))
    apellido = forms.CharField(max_length=20, label= "Apellido del Piloto", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el apellido', "autocomplete":"off", 'required':'true' }))
    escuderia = forms.CharField(max_length=20, label="Escuderia del Piloto", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese la escuderia', "autocomplete":"off", 'required':'true' }))
    
class NuevaCarrera(forms.Form):
    pista = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el nombre de la pista', "autocomplete":"off", 'required':'true'}))
    pais = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el pais donde estara ubicada', "autocomplete":"off", 'required':'true'}))
    vueltas = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'type': 'number', 'placeholder': 'Ingrese el numero de vueltas', "autocomplete":"off", 'required':'true'}))

class contactoForm(forms.Form):
    nombre = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese tu nombre', "autocomplete":"off", 'required':'true'}))
    apellido = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese tu apellido', "autocomplete":"off", 'required':'true'}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Ingresa tu direccion de correo electronico', "autocomplete":"off", 'required':'true'}))
    comentario = forms.CharField(max_length=200,widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Dejanos aqui tu comentario', "autocomplete":"off", 'required':'true'}))