# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required 
from django.core.urlresolvers import reverse 
from django.shortcuts import render_to_response, render, redirect 
from django.template import RequestContext 
from django.conf import settings 
from django.http import HttpResponseRedirect, HttpResponse 
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.models import AnonymousUser 
from django.contrib import messages 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.db.models import Q 
from datetime import datetime, timedelta 
from django.utils import timezone
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
# Create your views here.

def iniciador (request):
    return render(request,'iniciador.html')


def my_logout(request):
    logout(request)
    return redirect ('index')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    return redirect('main') 


def main(request):
    joda = Evento.objects.all()
    return render(request,'main.html', {'todos_los_eventos':joda})

def mkevento(request):
    if request.method == 'POST':
        user = request.user
        text = request.POST['Ttext']
        edad_min = request.POST['edad_min']
        precio = request.POST['precio']
        capacidad = request.POST['capacidad']
        ubicacion = request.POST['ubicacion']
        comentario = request.POST['comentario']
        foto = request.POST['foto']
        fecha = request.POST['fecha']
        new_evento = Evento(nombre=text, creador=user, edad_min=edad_min,precio=precio, capacidad=capacidad,ubicacion=ubicacion,comentario=comentario, foto=foto )
        new_evento.save()
        return redirect('main')
    return HttpResponse('HOLA <b style="color: red">no no no</b>')

def mkasist(request, evento_id):
    ev = Evento.objects.get(id=evento_id)
    new_asist, new = Asist.objects.get_or_create(asist=ev, user=request.user)
    if new:
        new_asist.save()
    else:
        new_asist.delete()
    return redirect('main')


def delete_evento(request, evento_id):
    tw = Evento.objects.get(id=evento_id)
    if request.user == tw.creador:
        tw.delete()
    return redirect('main')