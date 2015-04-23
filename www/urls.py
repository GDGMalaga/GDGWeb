from django.conf.urls import patterns, url

from . import views
from django.shortcuts import redirect

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^login', views.login, name='login'),
	url(r'^logout', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}),
    url(r'^calendario', views.calendario, name='calendario'),
    url(r'^grupos', views.grupos, name='grupos'),
    url(r'^accede', views.accede, name='accede')
)



	