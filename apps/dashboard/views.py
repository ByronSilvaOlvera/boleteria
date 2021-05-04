from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Menu


def index(request):
    menu = Menu.objects.all()
    template = loader.get_template('index.html')    
    context = {
        'menu': menu,
    }
    return HttpResponse(template.render(context, request))

def inicioSeccion(request , id_sec):
    return HttpResponse('Seccion %s.' % id_sec )    

# Create your views here.
