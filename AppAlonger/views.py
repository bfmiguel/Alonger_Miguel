from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from AppAlonger.models import  Actividad

# Create your views here.


class lista_actividad(ListView):
    model = Actividad
    template_name = "AppAlonger/lista_actividad.html"


class detalle_actividad(DetailView):
    model = Actividad
    template_name = "AppAlonger/detalle_actividad.html"

class crear_actividad(CreateView):
    model = Actividad
    success_url = "/app/actividad/lista"
    template_name = "/app/agregar_actividad.html"
    fields = ["nombre", "tipo", "empresa"]


class actualizar_actividad(UpdateView):
    model = Actividad
    success_url = "/app/actividad/lista"
    template_name = "/app/agregar_actividad.html"
    fields = ["nombre", "tipo", "empresa"]


def ver_actividad(request):
    actividad = Actividad.objects.all
    contexto = {
        "actividades": actividad
    }

    return render(request, "AppAlonger/actividades.html", contexto)


def show_html(request):
    actividad = Actividad.objects.all()
    contexto = {"Actividad": actividad,}
    return render(request, 'index.html', contexto)



