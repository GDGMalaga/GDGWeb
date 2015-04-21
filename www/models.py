from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    """
    Datos adicionales para un usuario
    """
    user = models.OneToOneField(User)
    # Any extra data

    def __unicode__(self):
        return "<UserProfile: %s>" % (self.user.username)


class Grupo(models.Model):
    """
    Grupo (?) 
    """
#   cursos = models.ForeignKey(Curso)
    name = models.CharField(max_length=50)
    pub_date = models.DateField()


class Curso(models.Model):
    """
    Curso (?)
    """
    name = models.CharField(max_length=50)
    pub_date = models.DateField()
    date_activity = models.DateField()
    location = models.CharField(max_length=10)
    information = models.CharField(max_length=200)
    grupo = models.ForeignKey(Grupo)

    def __unicode__(self):
        return "%s %s %s" % (self.name, self.date_activity, self.location)
