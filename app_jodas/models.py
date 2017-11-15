# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime



# Create your models here.


class Userprofile(models.Model):
    user=models.OneToOneField(User)
    celular = models.CharField(max_length= 10)
    direccion = models.CharField(max_length= 60)
    telefono = models.CharField(max_length= 10)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
       return self.user.username

class Evento(models.Model):
    nombre= models.CharField(max_length= 200)
    edad_min=models.IntegerField(default= None)
    tipo_fiesta = models.CharField(max_length=15)
    precio = models.IntegerField(default=None)
    capacidad = models.IntegerField(default=None)
    ubicacion = models.CharField(max_length= 60)
    comentario = models.CharField(max_length= 250)
    creador = models.ForeignKey(User)
    foto = models.ImageField(upload_to='fotos')  
    fecha = models.DateTimeField()  
    telefono = models.CharField(max_length= 10)
    def count_asist(self):
        return Asist.objects.filter(asist=self).count()

    def __unicode__(self):
       return self.nombre 

class Asist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    asist = models.ForeignKey(Evento)
    def __unicode__(self):
       return 'Asiste: ' + self.user.username + ' al evento ' + self.asist.nombre 

class Choice(models.Model):
    evento = models.ForeignKey(Evento)

    def __str__(self):
        return self.choice_text
