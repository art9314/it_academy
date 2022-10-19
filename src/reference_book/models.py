
from tabnanny import verbose

from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 50)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def get_absolute_url(self):
        return f'/rb/{self.pk}/'        
            
class Series(models.Model):
    name = models.CharField(max_length = 50)
    number_series = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def get_absolute_url(self):
        return f'/rb/{self.pk}/'    

class Genre(models.Model):        
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def get_absolute_url(self):
        return f'/rb/{self.pk}/'   

class Publishing(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def get_absolute_url(self):
        return f'/rb/{self.pk}/'           
   
    



   