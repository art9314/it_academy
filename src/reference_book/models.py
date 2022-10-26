
from tabnanny import verbose

from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 50,verbose_name ='Group name')
    logo = models.ImageField(verbose_name='Logotip',upload_to = 'uploads/%Y/%m/%d/')   
    

    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def get_absolute_url(self):
        return reverse_lazy('reference_book:author-detail', kwargs = {'pk': self.pk})
        #return f'/rb/{self.pk}/'
                
            
class Series(models.Model):
    name = models.CharField(max_length = 50)
    number_series = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def get_absolute_url(self):
        return reverse_lazy('reference_book:series-detail', kwargs = {'pk': self.pk})
           

class Genre(models.Model):        
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def get_absolute_url(self):
        return reverse_lazy('reference_book:genre-detail', kwargs = {'pk': self.pk})
          

class Publishing(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def get_absolute_url(self):
        return reverse_lazy('reference_book:publishing-detail', kwargs = {'pk': self.pk})
                  
   
    



   