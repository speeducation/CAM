from django.conf.urls import patterns, include, url
from .views import IndexView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),    #Cuando la aplicacion solicite la peticion https://127.0.0.1:8000/ o http://localhost:8000/
                                        #Desplegara la vista contenida en la clase IndexView el cual es base/index.html
)
