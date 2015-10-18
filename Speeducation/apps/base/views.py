from django.shortcuts import render
from django.views.generic import TemplateView   #Clase Para Temlates Generecicos que ofrece Django

# Create your views here.
class IndexView(TemplateView):  #Se crea la clase IndexView, que hereda las caracteristicas de la clase TemplateView
    template_name = 'base/index.html'   #Se indica donde encontrara el template que la vista usara