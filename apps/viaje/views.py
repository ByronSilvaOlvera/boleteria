#from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView 

#from boleteria,forms import RutaForm


from .models import Cliente, Transporte, ViajeRuta
# Create your views here.

class ClienteListView(ListView):
    context_object_name = 'cliente_list'
    queryset  = Cliente.objects.all()
    template_name = 'clientes/cliente_list.html'

class TransporteListView(ListView):
    context_object_name = 'transporte_list'
    queryset  = Transporte.objects.all()
    template_name = 'transporte/transporte_list.html'

class RutaListView(ListView):
    context_object_name = 'ruta_list'
    queryset  = ViajeRuta.objects.all()
    template_name = 'ruta/rutas_list.html'

class RutaCreateView(CreateView):
    model = ViajeRuta
    fields = ['nombre','inicio','destino','horas']


