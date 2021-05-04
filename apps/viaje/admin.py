from django.contrib import admin

# Register your models here.

from .models import Cajero, Boleto, Cliente, Transporte, ViajeRuta

admin.site.register(Cajero)
admin.site.register(Boleto)
admin.site.register(Cliente)
admin.site.register(Transporte)
admin.site.register(ViajeRuta)