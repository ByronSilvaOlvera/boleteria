from django.db import models

# Create your models here.

class Cajero(models.Model):
    usuario        = models.CharField(max_length=50)    
    fechaconeccion = models.CharField(max_length=50)
    horasconectado = models.CharField(max_length=50)
    fechatermina   = models.DateTimeField('date pusblished')

class Cliente(models.Model):
    nombre   = models.CharField(max_length=200)
    identidad= models.CharField(max_length=200)
    correo   = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
    

class Boleto(models.Model):
    numero     = models.CharField(max_length=200)
    fecha      = models.DateTimeField('date pusblished')
    cliente    = models.CharField(max_length=200)
    horasalida = models.CharField(max_length=200)
    horallegada= models.CharField(max_length=200)
    cajero     = models.CharField(max_length=200)     
    #chofer     = models.CharField(max_length=200)
    asistente  = models.CharField(max_length=200)
    #usuario transporte viaje-ruta cliente cajero     
    vehiculo   = models.CharField(max_length=200)
    ruta       = models.CharField(max_length=200)

    
class Transporte(models.Model):     
    disco = models.CharField(max_length=200)
    placa = models.CharField(max_length=200)    
    anio  = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    modelo= models.CharField(max_length=200)

    def __str__(self):
        return self.disco

class ViajeRuta(models.Model):
    nombre  = models.CharField(max_length=200)
    inicio  = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    horas   = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('ruta-detail', kwargs={'pk' : self.pk } )
    
    



