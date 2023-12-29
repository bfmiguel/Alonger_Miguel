from django.db import models

# Create your models here.



class Curso(models.Model):
    nombre= models.CharField(max_length=40)
    camada= models.IntegerField()

    """def __str__(self):
        return f"Actividad: {self.nombre}, tipo: {self.tipo}, tipo: {self.tipo}"
"""


class Actividad(models.Model):
    nombre= models.CharField(max_length=40)
    tipo= models.CharField(max_length=40)
    empresa = models.CharField(max_length=40)

    def __str__(self):
        return f"Actividad: {self.nombre}, tipo: {self.tipo}, tipo: {self.tipo}"


