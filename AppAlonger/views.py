from django.shortcuts import render, redirect
from AppAlonger.models import Curso
from django.http import HttpResponse
# Create your views here.


def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        "cursos" : cursos
    }
    return render(request, "AppAlonger/cursos.html", contexto)

def crear_curso(request):
    curso = Curso(nombre= "python", camada="47785")
    curso.save()
    return redirect("/app/cursos/")

def show_html(request):
    curso = Curso.objects.all()
    contexto = {"curso": curso, "nombre": "Miguel"}
    return render(request, 'index.html', contexto)



