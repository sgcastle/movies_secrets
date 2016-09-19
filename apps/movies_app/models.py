from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)

class Actor(models.Model):
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie)
