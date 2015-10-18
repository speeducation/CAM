from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Speeducation.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('apps.base.urls')), #Se indica que se utilizara el archivo de urls.py de la aplicacion home

    url(r'^admin/', include(admin.site.urls)),
)
