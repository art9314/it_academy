
from django.urls import path
from . import views 

app_name = "home_page"
urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('logout/', views.logout_request, name= "logout"),
    path('', views.HomePage.as_view(), name='home_page')
]