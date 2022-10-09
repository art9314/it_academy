from msilib.schema import ServiceInstall
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 50)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name

            
class Series(models.Model):
    name = models.CharField(max_length = 50)
    number_series = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.name


class Genre(models.Model):        
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name


class Publishing(models.Model):             
   name = models.CharField(max_length = 50)
   def __str__(self):
        return self.name


   