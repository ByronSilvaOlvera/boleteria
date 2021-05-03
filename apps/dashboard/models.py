from django.db import models

# Create your models here.

class Menu(models.Model):
    icon       = models.CharField(max_length=50)
    rutaName   = models.CharField(max_length=50) 
    nombre     = models.CharField(max_length=50) 

    def __str__(self):
        return self.nombre

    def icon_get(self):
        return self.icon
