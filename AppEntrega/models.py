from django.db import models

# Create your models here.

class Piloto(models.Model):
    nombre = models.CharField(max_length=40, verbose_name='Nombre')
    apellido = models.CharField(max_length=40, verbose_name='Apellido')
    escuderia = models.CharField(max_length=40, verbose_name='Escuderia')
    
class Carreras(models.Model):
    pista = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    vueltas = models.IntegerField()
    
    def __str__(self):
        return f'En {self.pais} se encuentra la pista {self.pista}, la cual se completa con {self.vueltas} vueltas'
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)    
    correo = models.EmailField()
    comentario = models.CharField(max_length=200)  
