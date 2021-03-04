from django.db import models

class Alumnos(models.Model):
    nombre = models.CharField(max_length=75)
    apellido = models.CharField(max_length=75)
    sede = models.CharField(max_length=15)
    edad = models.IntegerField()
