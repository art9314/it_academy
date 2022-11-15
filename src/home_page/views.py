from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm
from reference_book.models import Author


def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}.")
                return HttpResponseRedirect('/')
            else:
                messages.error(request,"The username or password you entered is incorrect.")
        else:
            messages.error(request,"The username or password you entered is incorrect.")
    form = AuthenticationForm()
    return render(request=request, template_name="home_page/login.html", context={"login_form":form})

#Create 
def register_request(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration was successful.")
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Registration failed.Enter correct data.")
    form = UserForm()
    return render (request=request, template_name="home_page/register.html", context={"register_form":form})

def logout_request(request):    
	logout(request)
	messages.info(request, "You are logged out.") 
	return HttpResponseRedirect('/')

class HomePage(generic.TemplateView):
    template_name = 'home_page/home_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)               
        context['books'] = Author.objects.get(pk=4)
        context['books1'] = Author.objects.get(pk=5)
        context['books2'] = Author.objects.get(pk=3)

        return context
 
 




