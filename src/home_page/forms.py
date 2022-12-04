from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from catalog.models import AppUser
from django.core.exceptions import ValidationError
from django.db import models

#Django Admin

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = AppUser
        fields = (
            "username",
            "email",
            "name",
            "surname",
            "phone",
            "country",
            "city",
            "index",
            "address",
            "reserve_address",
            "password",
            "additional_info"
        )


class MyUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = AppUser
        fields = (
            "username",
            "email",
            "name",
            "surname",
            "phone",
            "country",
            "city",
            "index",
            "address",
            "reserve_address",
            "password1",
            "password2",
            "additional_info"
            )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords is not the same")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

#Application

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    index = forms.IntegerField(required=True)
    name = forms.CharField(required=True, max_length=30)
    surname = forms.CharField(required=True, max_length=30)
    phone = forms.IntegerField(required=True, help_text="Enter the number.")
    country = forms.CharField(required=True)
    city = forms.CharField(required=True, max_length=30)
    address = forms.CharField(required=True, max_length=60)
    reserve_address = forms.CharField(required=False, max_length=60)
    additional_info = forms.CharField(required=False, max_length=150)



    class Meta:
        model = AppUser
        fields = (

            "username",
            "email",
            "name",
            "surname",
            "phone",
            "country",
            "city",
            "index",
            "address",
            "reserve_address",
            "password1",
            "password2",
            "additional_info",

            )

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.name = self.cleaned_data['name']
        user.surname = self.cleaned_data['surname']
        user.country = self.cleaned_data['country']
        user.city = self.cleaned_data['city']
        user.index = self.cleaned_data['index']
        user.address = self.cleaned_data['address']
        user.reserve_address = self.cleaned_data['reserve_address']
        user.additional_info = self.cleaned_data['additional_info']



        if commit:
            user.save()

        return user