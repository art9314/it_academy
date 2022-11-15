from django import forms
from . import models


class DateInput(forms.DateInput):
    input_type = 'date'


class ProdCardForm(forms.ModelForm):
    class Meta:
        model = models.Books
        fields = ['name', 'logo', 'author', 'price', 'series', 'genre', 'publishing_year', 'pages', 'binding','format', 'isbn', 'weight',
         'age_restriction', 'publishing', 'available_books', 'activity','rating', 'date_of_addition', 'description']
        widgets = {'date_of_addition' : DateInput()}
