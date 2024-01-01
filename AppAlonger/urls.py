

from django.urls import path

from AppAlonger.models import Alonger
from AppAlonger.views import show_html, lista_actividad, detalle_actividad, CrearActividad, actualizar_actividad, \
    ver_actividad, alonger, iluminacion, ver_iluminacion

urlpatterns = [
    path('ver_actividad/', ver_actividad),
    path('alonger/', alonger, name="alonger"),
    path('iluminacion/', iluminacion.as_view(), name="iluminacion"),
    path('show/', show_html, name="show"),
    path('actividad/lista', lista_actividad.as_view(), name="listas"),
    path('iluminacion/detalle', ver_iluminacion, name="iluminacion_detalle"),
    path('detalle/<int:pk>', detalle_actividad.as_view(), name="detalle"),
    path('crear/', CrearActividad.as_view(), name="crear"),
    path('actualizar/<int:pk>', actualizar_actividad.as_view(), name="actualizar"),
]
