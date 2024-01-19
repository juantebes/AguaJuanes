from django.db import models

# Create your models here.

class Cliente(models.Model):
    
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    direccion=models.CharField(max_length=40)
    telefono=models.IntegerField()

class Productos(models.Model):
    nombre_producto=models.CharField(max_length=20)
    descripcion_producto=models.CharField(max_length=20)
    numero_producto=models.IntegerField()

class Proveedores(models.Model):
    nombre=models.CharField(max_length=20)
    direccion=models.CharField(max_length=40)
    condicion_iva=models.CharField(max_length=40)
    cuil_cuit=models.IntegerField()
    telefono=models.IntegerField()