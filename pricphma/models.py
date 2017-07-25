from django.db import models
from django.forms import forms


# Create your models here.


class Docente(models.Model):
    identidad = models.BigIntegerField(primary_key=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    numero_afiliacion = models.BigIntegerField()
    fecha_ini_servicio = models.DateField()
    
    def __str__(self):
        return self.nombres + " " + self.apellidos
    
class EstadoCuenta(models.Model):
    
    class Meta:
        verbose_name = 'Estado de Cuenta'
        verbose_name_plural = 'Estados de Cuenta'
     
    Docente = models.ForeignKey(Docente)
    anio = models.IntegerField(primary_key=True)
    enero = models.FloatField()
    febrero = models.FloatField()
    marzo = models.FloatField()
    abril = models.FloatField()
    mayo = models.FloatField()
    junio = models.FloatField()
    julio = models.FloatField()
    agosto = models.FloatField()
    septiembre = models.FloatField()
    octubre = models.FloatField()
    noviembre = models.FloatField()
    diciembre = models.FloatField()
    
    
    def __str__(self):
        return self.Docente.nombres + ' ' + self.Docente.apellidos

class Slider(models.Model):
    url_imagen = models.ImageField(upload_to = 'img/slider/') 
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    etiqueta = models.CharField(max_length=50)
    enlace = models.URLField(blank=True,null=True)
    estado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
    