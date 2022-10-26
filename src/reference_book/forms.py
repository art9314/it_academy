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
        fields=['name','logo','date_of_birth','date_of_death','description' ]
        
        
    def clean(self):
        cleaned_data=super().clean()
        date_of_birth=cleaned_data.get('date_of_birth')
        date_of_death=cleaned_data.get('date_of_death')
        if date_of_death<date_of_birth:
            self.add_error('date_of_birth','< than date_of_death')
            self.add_error('date_of_death','> than date_of_birth')
        return cleaned_data

#class SeriesForm(forms.Form):
    #name = forms.CharField(max_length=50)
    #number_series = forms.IntegerField()

class SeriesForm(forms.ModelForm):
    class Meta:
        model = models.Series
        fields = ['name', 'number_series']

    def clean(self):
        cleaned_number_series = super().clean()
        number_series= cleaned_number_series.get(number_series)
        return cleaned_number_series

class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = ['name']

    def clean(self):
        cleaned_number_Genre = super().clean()
        number_Genre= cleaned_number_Genre.get(number_Genre)
        return cleaned_number_Genre

class PublishingForm(forms.ModelForm):
    class Meta:
        model = models.Publishing
        fields = ['name']

    def clean(self):
        cleaned_number_Publishing = super().clean()
        number_Publishing= cleaned_number_Publishing.get(number_Publishing)
        return cleaned_number_Publishing

        