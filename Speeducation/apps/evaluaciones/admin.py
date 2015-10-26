from django.contrib import admin

# Register your models here.
from .models import Evaluacion, Linea, Actividad, Conducta

admin.site.register(Evaluacion)
admin.site.register(Linea)
admin.site.register(Actividad)
admin.site.register(Conducta)