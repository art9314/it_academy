from django.urls import path
from . import views

app_name = "catalog"
urlpatterns = [
    path('', views.CatalogView.as_view(), name='catalog'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
]