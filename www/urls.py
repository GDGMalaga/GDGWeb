from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
                       url(r'^$', views.home, name='home'),
                       url(r'^calendario/', views.calendario, name='calendario'),
                       url(r'^grupos/', views.grupos, name='grupos'),
)
