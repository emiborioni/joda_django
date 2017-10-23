from django.forms import ModelForm
from .models import *


class EventoForm(ModelForm):

    class Meta:
        model = Evento
        fields = ['nombre', 'edad_min', 'tipo_fiesta', 'precio','capacidad','ubicacion','comentario','foto','fecha','telefono']
