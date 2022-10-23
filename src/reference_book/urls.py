from django.urls import path
from . import views 
app_name = 'reference_book'
urlpatterns = [
    path('rb/<int:pk>/', views.ShowAuthor.as_view(), name = 'author-detail'),
    path('rb-create/', views.CreateAuthor.as_view(), name = 'author-create'),
    path('rb-update/<int:pk>/', views.UpdateAuthor.as_view(), name = 'author-update'),
    path('rb-delete/<int:pk>/', views.DeleteAuthor.as_view(), name = 'author-delete'),
    path('rb/', views.ShowAuthors.as_view(), name = 'author-list'),

    path('rb-seies/<int:pk>/', views.ShowSeries.as_view(), name = 'series-detail'),
    path('rb-create-seies/', views.CreateSeries.as_view(), name = 'series-create'),
    path('rb-update-seies/<int:pk>/', views.UpdateSeries.as_view(), name = 'series-update'),
    path('rb-delete-seies/<int:pk>/', views.DeleteSeries.as_view(), name = 'series-delete'),
    path('rb-seies/', views.ShowSerie.as_view(), name = 'series-list'),
   
    path('rb-genre/<int:pk>/', views.ShowGenre.as_view(), name = 'genre-detail'),
    path('rb-create-genre/', views.CreateGenre.as_view(), name = 'genre-create'),
    path('rb-update-genre/<int:pk>/', views.UpdateGenre.as_view(), name = 'genre-update'),
    path('rb-delete-genre/<int:pk>/', views.DeleteGenre.as_view(), name = 'genre-delete' ),
    path('rb-genre/', views.ShowGenres.as_view(),name = 'genre-list'),

    path('rb-Publishing/<int:pk>/', views.ShowPublishing.as_view(), name = 'publishing-detail'),
    path('rb-create-Publishing/', views.CreatePublishing.as_view(), name = 'publishing-create'),
    path('rb-update-Publishing/<int:pk>/', views.UpdatePublishing.as_view(), name = 'publishing-update'),
    path('rb-delete-Publishing/<int:pk>/', views.DeletePublishing.as_view(), name = 'publishing-delete'),
    path('rb-Publishing/', views.ShowPublishings.as_view(), name = 'publishing-list'),
    
    ]