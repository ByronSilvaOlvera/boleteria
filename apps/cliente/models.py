from django.db import models
from django.urls import reverse

class Cliente(models.Model):
    nombres         = models.CharField(max_length=50)
    apellidos       = models.CharField(max_length=50) 
    correo          = models.CharField(max_length=50) 
    identificacion  = models.CharField(max_length=50) 
    fechaNacimiento = models.DateField(auto_now=False,auto_now_add=False, default='2021-05-05')

    def __str__(self):
        return self.nombres

    def get_absolute_url(self):
        return reverse('cliente-detail', kwargs={'pk': self.pk})