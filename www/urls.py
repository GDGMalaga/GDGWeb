from django.conf.urls import patterns, url

from . import views
from django.shortcuts import redirect

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
    url(r'^calendario', views.calendario, name='calendario'),
    url(r'^grupos', views.grupos, name='grupos'),
    url(r'^accede', views.accede, name='accede')
)



	