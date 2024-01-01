from django.db import models

# Create your models here.


"""
class Curso(models.Model):
    nombre= models.CharField(max_length=40)
    camada= models.IntegerField()

    def __str__(self):
        return f"Actividad: {self.nombre}, tipo: {self.tipo}, tipo: {self.tipo}"
"""
class Iluminacion(models.Model):
    operacion= models.CharField(max_length=40)
    cliente= models.CharField(max_length=40)
    yacimiento= models.CharField(max_length=40)
    equipo= models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)


    def __str__(self):
        return f"operacion: {self.operacion}, cliente: {self.cliente}, yacimiento: {self.yacimiento}, equipo: {self.equipo}, tipo: {self.tipo}"

class Actividad(models.Model):
    nombre= models.CharField(max_length=40)
    tipo= models.CharField(max_length=40)
    empresa = models.CharField(max_length=40)

class Alonger(models.Model):
    informacion = {"ALONGER es Seguridad Industrial. Contamos con más de 13 años de trayectoria brindando soporte en la Prevención y Control de Riesgos Laborales. Prestamos atención a las necesidades de nuestros clientes y ofrecemos soluciones integrales a medida."

"Porque nos apasiona lo que hacemos hemos logrado conformar un equipo de Técnicos, Licenciados e Ingenieros de gran solidez y potencial. Nos llena de orgullo ser convocados para brindar asesoramiento o soporte de seguridad en las operaciones; más aún cuando el resultado son clientes operando con integridad, en circunstancias de trabajos seguros, evitando accidentes y preservando el medio ambiente."

"Con sede en la Ciudad Neuquén, nuestros servicios tienen alcance en todo el territorio de la República Argentina"

}

    def __str__(self):
        return f"Actividad: {self.nombre}, tipo: {self.tipo}, tipo: {self.tipo}"


