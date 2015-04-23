# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    """
    Datos adicionales para un usuario
    """
    user = models.OneToOneField(User)
    # Any extra data
    about = models.CharField(max_length=200)
    hobbies = models.CharField(max_length=200)


    def __unicode__(self):
        return "<UserProfile: %s>" % (self.user.username)

class Skill(models.Model):
    skill_name = models.CharField(max_length=30)
    UserProfile = models.ForeignKey(UserProfile)

    def __unicode__(self):
        return "Habilidad : %s" % (self.skill_name)

class Grupo(models.Model):
    """
    Grupo de estudio de una tecnologia

    El Grupo deberia tener como relación opcional una lista de cursos que ver. 
    Por ejemplo el grupo de estudio de Django podria reunirse para el curso de Django de Coursera, suponiendo que haya uno.
    """
    #cursos = models.ForeignKey(Curso)
    name = models.CharField(max_length=50)
    pub_date = models.DateField()

    def __unicode__(self):
        return "<Grupo : %s" % (self.name)


class Curso(models.Model):
    """
    Curso que se realizará en el GDG (como curso de Django, por ejemplo ;) )
    Curso debería tener una relación con Grupo, ¿no?
    """
    name = models.CharField(max_length=50)
    pub_date = models.DateField()
    date_activity = models.DateField()
    location = models.CharField(max_length=10)
    information = models.CharField(max_length=200)
    grupo = models.ForeignKey(Grupo)

    def __unicode__(self):
        return "%s %s %s" % (self.name, self.date_activity, self.location)
