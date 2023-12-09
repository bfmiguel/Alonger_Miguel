from django.shortcuts import render
from AppAlonger.models import Curso
from django.http import HttpResponse
# Create your views here.

def crear_curso(request):
    curso = Curso(nombre= "python", camada="47785")
    curso.save()


    return HttpResponse(f"Sr curso es {curso.nombre} camada {curso.camada}")

"""
tambien puedo hacer 
return HttpResponse(curso.nombre)

"""