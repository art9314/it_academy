from django.urls import path
from . import views


app_name = 'admin_portal'
urlpatterns = [
    path('', views.AdminPortalView.as_view(), name='admin_portal'),
]
