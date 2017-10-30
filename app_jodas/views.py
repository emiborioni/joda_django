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
from .forms import *
# Create your views here.

def iniciador (request):
    return render(request,'iniciador.html')

def mostrar (request):
    return render(request,'register.html')

def my_logout(request):
    logout(request)
    return redirect ('main')

def my_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('main') 
    else:
        print redirect('main')

def main(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            post = form.instance
            post.user = request.user
            post.save() 
            print "evento guardado"
        return redirect('main')
    else:
         form = EventoForm()
         joda = Evento.objects.all()
         print "evento no guarda"
    return render(request,'main.html', {'todos_los_eventos':joda, 'form':form})
    
def register (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        celular = request.POST['celular']
        direccion = request.POST['direccion']

        userprofile = Userprofile(celular=celular, direccion=direccion)
        userprofile.save()
               
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return render(request, 'main')

def buscador(request):
    if request.method == 'POST':
        edad_min = request.POST['edad_min']
        precio = request.POST['precio']
        tipo_fiesta = request.POST['tipo_fiesta']
        fecha = request.POST['fecha']
        return redirect('main')


def mkasist(request, evento_id):
    total = Evento.objects.get(id=evento_id)
    asistencia = total.count_asist()
    print asistencia
    ev = Evento.objects.get(id=evento_id)
    new_asist, new = Asist.objects.get_or_create(asist=ev, user=request.user)
    if new:
        if asistencia >= total.capacidad:
            return HttpResponse("El evento esta lleno")
        else:
            new_asist.save()
            print "Estas en la joda"
    else:
        new_asist.delete()
        print "Chau"
    
    return redirect('main')

def delete_evento(request, evento_id):
    tw = Evento.objects.get(id=evento_id)
    if request.user == tw.creador:
        tw.delete()
    return redirect('main')
