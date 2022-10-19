from django import forms
from django.core.exceptions import ValidationError
from . import models 



def name_validator(value:str):
    if value.startswith('M'):
        raise ValidationError('Must not srart')
    return value

class AuthorForm(forms.ModelForm):
    class Meta:
        model=models.Author
        fields=['name','date_of_birth','date_of_death','description' ]
        
        
        def clean(self):
            cleaned_data=super().clean()
            date_of_birth=cleaned_data.get('date_of_birth')
            date_of_death=cleaned_data.get('date_of_death')
            if date_of_death<date_of_birth:
                self.add_error('date_of_birth','< than date_of_death')
                self.add_error('date_of_birth','> than date_of_birth')
            return cleaned_data