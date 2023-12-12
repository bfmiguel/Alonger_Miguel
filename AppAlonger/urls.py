

from django.urls import path
from AppAlonger.views import crear_curso, show_html, mostrar_cursos, agregar_actividad_form, buscar_actividad, \
    lista_actividad

urlpatterns = [
    path('agregar_curso/', crear_curso),
    path('show/', show_html),
    path('cursos/', mostrar_cursos),
    path('buscar/', buscar_actividad),
    path('agregar_actividad/', agregar_actividad_form),
    path('lista_actividad/', lista_actividad.as_view(), name="listas"),

]
