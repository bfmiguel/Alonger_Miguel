from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre= models.CharField(max_length=40)
    camada= models.IntegerField()

    def __str__(self):
        return f"Curso: {self.nombre}, Camada: {self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email= models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email= models.EmailField()
    profesion= models.CharField(max_length=40)

    def __str__(self):
        return f"Profesor: {self.nombre} {self.apellido}"

class entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_de_entrega = models.DateField()
    enregado = models.BooleanField()
