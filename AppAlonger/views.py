from django.shortcuts import render
from AppAlonger.models import Curso
from django.http import HttpResponse
# Create your views here.

def crear_curso(request):
    curso = Curso(nombre= "python", camada="47785")
    curso.save()
    contexto= {"curso": curso}
    return render(request, 'index.html', contexto)

def show_html(request):
    curso = Curso.objects.all()
    contexto = {"curso": curso}
    return render(request, 'index.html', contexto)



"""
tambien puedo hacer 
return HttpResponse(curso.nombre)

"""