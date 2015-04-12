from django.db import models

# Create your models here.
class Curso(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateField()
    date_activity = models.DateField()
    location = models.CharField(max_length=10)
    information = models.CharField(max_length=200)

class Usuario(models.Model):
    name = models.CharField(max_length=20)

