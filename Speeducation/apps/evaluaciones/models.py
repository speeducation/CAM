from django.db import models
from apps.alumnos.models import Alumno
from datetime import datetime
from .choices import EVALUATION_CHOICES

# Create your models here.
class Linea(models.Model):
    descripcion = models.TextField(max_length=100)

    def __unicode__(self):
        return self.descripcion[:20]

# Create your models here.
class Conducta(models.Model):
    linea = models.ForeignKey(Linea)
    descripcion = models.TextField(max_length=100)
    disponibilidad = models.BooleanField(default=False)

# Create your models here.
class Actividad(models.Model):
    linea = models.ForeignKey(Linea)
    descripcion = models.TextField(max_length=100)

    def __unicode__(self):
        return self.descripcion[:20]

# Create your models here.
class Evaluacion(models.Model):
    alumno = models.ForeignKey(Alumno)
    linea = models.ForeignKey(Linea)
    actividad = models.ForeignKey(Actividad)
    evaluacionInicial = models.IntegerField(default=1, choices=EVALUATION_CHOICES)
    evaluacionMedia = models.IntegerField(default=1, choices=EVALUATION_CHOICES)
    evaluacionFinal = models.IntegerField(default=1, choices=EVALUATION_CHOICES)
    fechaInicial = models.DateField( default=datetime.today())
    fechaFinal = models.DateField( default=datetime.today())