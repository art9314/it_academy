from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    name = forms.CharField(required=True, max_length=40)
    surname = forms.CharField(required=True, max_length=40)
    email = forms.EmailField(required=True)
    country = forms.CharField(required=True)
    city = forms.CharField(required=True, max_length=40)
    address = forms.CharField(required=True, max_length=50)
    index = forms.IntegerField(required=True)      
    phone = forms.IntegerField(required=True, help_text="Enter the number.")
    reserve_address = forms.CharField(required=False, max_length=50)
    additional_info = forms.CharField(required=False, max_length=200)

    class Meta:
        model = User
        fields = ("username", "email", "name", "surname", "phone", "country", "city", "index", "address", "reserve_address",  "password1", "password2", "additional_info")

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.name = self.cleaned_data['name']
        user.surname = self.cleaned_data['surname']
        user.email = self.cleaned_data['email']
        user.country = self.cleaned_data['country']
        user.city = self.cleaned_data['city']
        user.address = self.cleaned_data['address']
        user.index = self.cleaned_data['index']
        user.reserve_address = self.cleaned_data['reserve_address']
        user.additional_info = self.cleaned_data['additional_info']
        if commit:
            user.save()
        return user