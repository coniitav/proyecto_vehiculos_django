from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    marca = models.CharField(max_length=20, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, default='Particular')
    precio = models.DecimalField(decimal_places=0, max_digits=10)
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()