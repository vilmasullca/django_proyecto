from django.db import models

# Create your models here.

class Turno(models.Model):
    Dni = models.CharField(max_length = 10)
    Especialidad = models.CharField(max_length = 50)
    Fecha = models.DateField()
    Hora = models.TimeField()