from django.shortcuts import render, redirect
from django.views.generic import ListView

from AppAlonger.models import Curso
from AppAlonger.forms import agregar_actividad, buscar_actividad_form
from django.http import HttpResponse
# Create your views here.


class lista_actividad(ListView):
    model = Curso
    template_name = "templates/lista_actividad.html"




def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        "cursos": cursos,
        "form": buscar_actividad_form(),
    }
    return render(request, "AppAlonger/cursos.html", contexto)

def crear_curso(request):
    curso = Curso(nombre= "python", camada="47785")
    curso.save()
    return redirect("/app/cursos/")

def agregar_actividad_form(request):

    if request.method == "POST":

        agregar_actividad_new = agregar_actividad(request.POST)
        if agregar_actividad_new.is_valid():
            datos_agregados = agregar_actividad_new.cleaned_data

            actividad = Curso(nombre = datos_agregados["nombre"], camada = datos_agregados["camada"])
            actividad.save()
            return redirect("/app/cursos/")

    formulario_agregar = agregar_actividad()
    contexto = {
        "form": formulario_agregar
    }

    return  render(request, "AppAlonger/agregar_actividad.html", contexto)


def buscar_actividad(request):
    nombre = request.Get["nombre"]
    cursos = Curso.objects.filter(nombre__icontains=nombre)
    contexto = {
        "cursos": cursos,
        "form": buscar_actividad_form(),
    }
    return render(request, "AppAlonger/cursos.html", contexto)


def show_html(request):
    curso = Curso.objects.all()
    contexto = {"curso": curso, "nombre": "Miguel"}
    return render(request, 'index.html', contexto)



