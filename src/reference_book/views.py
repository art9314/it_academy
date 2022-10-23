import datetime
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from . import models,forms 
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.
class ShowAuthors (generic.ListView):
    model = models.Author
    template_name = 'reference_book/list.html'
    
class ShowAuthor (generic.DetailView):
    model = models.Author
    template_name = 'reference_book/detail.html'

class CreateAuthor (generic.CreateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'reference_book/edit.html'  
    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args,**kwargs)
            context['crup_name'] = 'Create'
            return context

class UpdateAuthor (generic.UpdateView):
    model=models.Author
    form_class = forms.AuthorForm
    template_name = 'reference_book/edit.html'
    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args,**kwargs)
            context['crup_name'] = 'Update'
            return context

class DeleteAuthor (generic.DeleteView):
    model=models.Author
    template_name = 'reference_book/delete.html'

class ShowSerie(generic.ListView):
    model = models.Series
    template_name = 'reference_book/list_series.html'

class ShowSeries (generic.DetailView):
    model = models.Series
    template_name = 'reference_book/detail.html'

class CreateSeries (generic.CreateView):
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'reference_book/edit.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['crup_name'] = 'Create'
        return context  

class UpdateSeries (generic.UpdateView):
    model=models.Series
    form_class = forms.SeriesForm
    template_name = 'reference_book/edit.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['crup_name'] = 'Update'
        return context

class DeleteSeries(generic.DeleteView):
    model=models.Series
    form_class = forms.SeriesForm
    template_name = 'reference_book/delete.html'


class ShowGenres(generic.ListView):
    model = models.Genre
    template_name = 'reference_book/list_genre.html'

class ShowGenre (generic.DetailView):
    model = models.Genre
    template_name = 'reference_book/detail.html'

class CreateGenre (generic.CreateView):
    model = models.Genre
    form_class = forms.GenreForm
    template_name = 'reference_book/edit.html'  
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['crup_name'] = 'Create'
        return context

class UpdateGenre (generic.UpdateView):
    model=models.Genre
    form_class = forms.GenreForm
    template_name = 'reference_book/edit.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['crup_name'] = 'Update'
        return context

class DeleteGenre(generic.DeleteView):
    model=models.Genre
    form_class = forms.GenreForm
    template_name = 'reference_book/delete.html'

class ShowPublishings(generic.ListView):
    model = models.Publishing
    template_name = 'reference_book/list_genre.html'

class ShowPublishing (generic.DetailView):
    model = models.Publishing
    template_name = 'reference_book/detail.html'

class CreatePublishing (generic.CreateView):
    model = models.Publishing
    form_class = forms.PublishingForm
    template_name = 'reference_book/edit.html' 
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['crup_name'] = 'Create'
        return context

class UpdatePublishing (generic.UpdateView):
    model=models.Publishing
    form_class = forms.PublishingForm
    template_name = 'reference_book/edit.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['crup_name'] = 'Update'
        return context

class DeletePublishing(generic.DeleteView):
    model=models.Publishing
    form_class = forms.PublishingForm
    template_name = 'reference_book/delete.html'