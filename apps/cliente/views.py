
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse
from .models import Cliente

class ClienteListView(ListView):
    model = Cliente

class ClienteDetailView(DetailView):
    model = Cliente

class ClienteCreateView(CreateView):
    model = Cliente
    fields = '__all__'

class ClienteUpdateView(UpdateView):
    model         = Cliente
    fields        = '__all__'
    template_name =  'cliente/cliente_edit.html'

class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente-list')
