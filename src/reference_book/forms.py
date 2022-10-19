from django import forms
from django.core.exceptions import ValidationError
from . import models 

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=50)
    date_of_birth = forms.DateField()
    date_of_death = forms.DateField()
    description = forms.CharField(widget=forms.Textarea, required = False)

