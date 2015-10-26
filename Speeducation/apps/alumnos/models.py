from django.db import models
from django.utils import timezone

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nombre + ' '+ self.apellidos