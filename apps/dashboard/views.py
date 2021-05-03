from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("mi dashboard")

def inicioSeccion(request , id_sec)
    return HttpResponse('Seccion %s.' % id_sec )    

# Create your views here.
