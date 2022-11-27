
from tabnanny import verbose

from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 50,verbose_name ='Author')
    surname = models.CharField(max_length=30,verbose_name="Author's surname",)    
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name + ' ' + self.surname
    
    def get_absolute_url(self):
        return reverse_lazy('reference_book:author-detail', kwargs = {'pk': self.pk})
        #return f'/rb/{self.pk}/'
                
            
class Series(models.Model):
    book_series = models.CharField(max_length = 50)
    description = models.TextField(blank = True,null = True)
    def __str__(self):
        return self.book_series  
    def get_absolute_url(self):
        return reverse_lazy('reference_book:series-detail', kwargs = {'pk': self.pk})
           

class Genre(models.Model):        
    genre_name = models.CharField(max_length = 50)
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.genre_name

    def get_absolute_url(self):
        return reverse_lazy('reference_book:genre-detail', kwargs = {'pk': self.pk})
          

class Publishing(models.Model):
    publishing_name = models.CharField(max_length = 50)
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.publishing_name 
    def get_absolute_url(self):
        return reverse_lazy('reference_book:publishing-detail', kwargs = {'pk': self.pk})
                  
   
    



   