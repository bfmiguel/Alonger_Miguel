from django.shortcuts import render
from django.template.context_processors import request
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from AppAlonger.models import Actividad


# Create your views here.


class lista_actividad(ListView):
    model = Actividad
    template_name = "AppAlonger/lista_actividad.html"


class detalle_actividad(DetailView):
    model = Actividad
    template_name = "AppAlonger/detalle_actividad.html"


# class CrearActividad(CreateView): debe estar en mayuscula
class CrearActividad(CreateView):
    model = Actividad
    success_url = "/app/actividad/lista"
    template_name = "AppAlonger/agregar_actividad.html"
    fields = "__all__"
    # fields = ["nombre", "tipo", "empresa"]


class actualizar_actividad(UpdateView):
    model = Actividad
    success_url = "/app/actividad/lista"
    template_name = "AppAlonger/agregar_actividad.html"
    fields = ["nombre", "tipo", "empresa"]





def ver_actividad(request):
    actividad = Actividad.objects.all()
    contexto = {
        "actividades": actividad
    }

    return render(request, "AppAlonger/actividades.html", contexto)


def show_html(request):
    actividades = Actividad.objects.all()
    contexto = {"actividades": actividades, }
    return render(request, 'index.html', contexto)
