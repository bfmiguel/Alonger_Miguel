from django import forms


class agregar_actividad(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()


class buscar_actividad_form(forms.Form):
    nombre = forms.CharField()
