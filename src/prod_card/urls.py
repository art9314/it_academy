from django.urls import path
from . import views

app_name = "prod_card"
urlpatterns = [
    path('prod_card_detail/<int:pk>/', views.ShowProdCard.as_view(), name='prod_card_detail'),
    path('prod_card_create/', views.CreateProdCard.as_view(), name='prod_card_create'),
    path('prod_card_update/<int:pk>/', views.UpdateProdCard.as_view(), name='prod_card_update'),
    path('prod_card_delete/<int:pk>/', views.DeleteProdCard.as_view(), name='prod_card_delete'),
    path('prod_card_list/', views.ShowProdCardList.as_view(), name='prod_card_list')
]