# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required 
from django.core.urlresolvers import reverse 
from django.shortcuts import render_to_response, render, redirect 
from django.template import RequestContext 
from django.conf import settings 
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse 
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.models import AnonymousUser 
from django.contrib import messages 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.db.models import Q 
from datetime import datetime, timedelta 
from django.utils import timezone
from .models import *
# Create your views here.

def iniciador (request):
    return render(request,'iniciador.html')

def registrar (request):
    return render(request,'register.html')

def login (request):
    return render(request,'login.html')

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
        foto = request.fileToUpload['fileToUpload']
        new_evento = Evento(nombre=text, creador=user, edad_min=edad_min,precio=precio, capacidad=capacidad,ubicacion=ubicacion,comentario=comentario, foto=foto )
        new_evento.save()
        return redirect('main.html')
    return HttpResponse('HOLA <b style="color: red">no puedes tweetear de esta forma</b>')

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