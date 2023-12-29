

from django.urls import path
from AppAlonger.views import show_html, lista_actividad, detalle_actividad, CrearActividad, actualizar_actividad, \
    ver_actividad

urlpatterns = [
    path('ver_actividad/', ver_actividad),
    path('show/', show_html),
    path('actividad/lista', lista_actividad.as_view(), name="listas"),
    path('detalle/<int:pk>', detalle_actividad.as_view(), name="detalle"),
    path('crear/', CrearActividad.as_view(), name="crear"),
    path('actualizar/<int:pk>', actualizar_actividad.as_view(), name="actualizar"),
]
