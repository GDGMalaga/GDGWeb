from django.conf.urls import patterns, url

from . import views
from django.shortcuts import redirect

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
)



	