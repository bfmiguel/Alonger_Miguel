from django.shortcuts import render
from django.template.context_processors import request
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from AppAlonger.models import Actividad, Alonger, Iluminacion


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
    success_url = "/app/show/"
    template_name = "AppAlonger/agregar_actividad.html"
    fields = "__all__"
    # fields = ["nombre", "tipo", "mpresa"]

class iluminacion(CreateView):
    model = Iluminacion
    template_name = "AppAlonger/iluminacion.html"
    fields = "__all__"



def alonger(request):
    contexto = {"Ahola" : "Nuestros servicios se adaptan a las necesidades y tamaño de nuestros clientes. Podemos ofrecer llevar a cabo todas las funciones de un Departamento de Seguridad e Higiene en el Trabajo en forma externa, suministrar profesionales que logren incrementar la dotación de HST de una organización, o proveer el desarrollo de actividades puntuales que contribuyan a la gestión HST de sus departamentos internos"

}
    return render(request, "AppAlonger/alonger.html", contexto)



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
