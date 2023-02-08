from django.db import models

# Create your models here.
class Productos(models.Model):

    nombre= models.CharField(max_length=40)
    precio= models.IntegerField()
    marca = models.CharField(max_length=40)

class Clientes(models.Model):

    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    mail = models.EmailField()

class Proveedores(models.Model):

    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    mail = models.EmailField()
