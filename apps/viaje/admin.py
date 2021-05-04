from django.contrib import admin

# Register your models here.

from .models import Cajero, Boleto

admin.site.register(Cajero)
admin.site.register(Boleto)