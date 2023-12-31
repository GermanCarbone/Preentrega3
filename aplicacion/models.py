from django.db import models

# Create your models here.

class Fiscal(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField()
    telefono=models.IntegerField()
    distrito=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Establecimiento(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    localidad=models.CharField(max_length=50)
    mesas=models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre}"

class Distrito(models.Model):
    nombre=models.CharField(max_length=50)
    seccion=models.PositiveSmallIntegerField()
    establecimientos=models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre}"

