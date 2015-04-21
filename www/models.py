from django.db import models

# Create your models here.

class Grupo(models.Model):
#   cursos = models.ForeignKey(Curso)
    name = models.CharField(max_length=50)
    pub_date = models.DateField()


class Curso(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateField()
    date_activity = models.DateField()
    location = models.CharField(max_length=10)
    information = models.CharField(max_length=200)
    grupo = models.ForeignKey(Grupo)

    def __unicode__(self):
        return "%s %s %s" % (self.name, self.date_activity, self.location)

# TODO: Deberia usarse django.contrib.auth.models.User
class Usuario(models.Model):
    name = models.CharField(max_length=20)
