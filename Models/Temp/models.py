from django.db import models

class Temp(models.Model):
    id_Alumnos = models.IntegerField()
    temp = models.IntegerField()
    fecha = models.DateTimeField()
