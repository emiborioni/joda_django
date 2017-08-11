# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Userprofile(models.Model):
    user=models.OneToOneField(User)
    dni = models.CharField(max_length= 8)
    direccion = models.CharField(max_length= 60)
    telefono = models.CharField(max_length= 9)


class Evento(models.Model):
    nombre= models.CharField(max_length= 200)
    fecha = models.DateTimeField()
    precio = models.IntegerField(max_length=4)
    capacidad = models.IntegerField(max_length=6)
    celular = models.CharField(max_length= 9)
    ubicacion = models.CharField(max_length= 60)
    comentario = models.CharField(max_length= 250)
    creador = models.ForeignKey(User)
    foto = models.ImageField(upload_to='fotos')    
        

class Imagenjoda(models.Model):
    evento = models.ForeignKey(Evento, related_name= 'images')
    tittle= models.CharField(max_length= 200)
    imagen= models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)










