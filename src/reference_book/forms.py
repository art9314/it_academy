from django import forms
from django.core.exceptions import ValidationError
from . import models 



def name_validator(value:str):
    if value.startswith(' '):
        raise ValidationError('Must not srart with " "')
    return value

class AuthorForm(forms.ModelForm):
    class Meta:
        model=models.Author
        fields=['name', 'surname', 'description' ]    
      

#class SeriesForm(forms.Form):
    #name = forms.CharField(max_length=50)
    #number_series = forms.IntegerField()

class SeriesForm(forms.ModelForm):
    class Meta:
        model = models.Series
        fields = ['book_series','description']

 
class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = ['genre_name','description']

class PublishingForm(forms.ModelForm):
    class Meta:
        model = models.Publishing
        fields = ['publishing_name','description']