from django.db import models

# Create your models here.
class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, null=True, blank=True)
    dni = models.CharField(max_length=10, null=True, blank=True)
    sexo = models.CharField(max_length=1, null=True, blank=True)
    nacimiento = models.DateField(null=True, blank=True)
    nacionalidad = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)
    correo = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nombre
