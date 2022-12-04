import datetime
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from . import models,forms 
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
class ShowAuthors (LoginRequiredMixin, PermissionRequiredMixin,generic.ListView):
    model = models.Author
    template_name = 'reference_book/list_author.html'
    login_url = 'home_page:login'
    permission_required = 'reference.view_author'
    
class ShowAuthor (LoginRequiredMixin, PermissionRequiredMixin,generic.DetailView):
    model = models.Author
    template_name = 'reference_book/detail_author.html'
    login_url = 'home_page:login'
    permission_required = 'reference.view_author'

class CreateAuthor (LoginRequiredMixin, PermissionRequiredMixin,generic.CreateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'reference_book/edit_author.html' 
    login_url = 'home_page:login'
    permission_required = 'reference.add_author' 
    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args,**kwargs)
            context['crup_name'] = 'Create'
            return context

class UpdateAuthor (LoginRequiredMixin, PermissionRequiredMixin,generic.UpdateView):
    model=models.Author
    form_class = forms.AuthorForm
    template_name = 'reference_book/edit_author.html'
    login_url = 'home_page:login'
    permission_required = 'reference.change_author'
    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args,**kwargs)
            context['crup_name'] = 'Update'
            return context

class DeleteAuthor (LoginRequiredMixin, PermissionRequiredMixin,generic.DeleteView):
    model=models.Author
    template_name = 'reference_book/delete_author.html'
    login_url = 'home_page:login'
    permission_required = 'reference.delete_author'
    def get_success_url(self):
        return reverse_lazy('reference:authors_list')

class ShowSerie(LoginRequiredMixin, PermissionRequiredMixin,generic.ListView):
    model = models.Series
    template_name = 'reference_book/list_series.html'
    login_url = 'home_page:login'
    permission_required = 'reference.view_series'

class ShowSeries (LoginRequiredMixin, PermissionRequiredMixin,generic.DetailView):
    model = models.Series
    template_name = 'reference_book/detail_series.html'
    login_url = 'home_page:login'
    permission_required = 'reference.view_series'

class CreateSeries (LoginRequiredMixin, PermissionRequiredMixin,generic.CreateView):
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'reference_book/edit_series.html'
    login_url = 'home_page:login'
    permission_required = 'reference.add_series'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['crup_name'] = 'Create'
        return context  

class UpdateSeries (LoginRequiredMixin, PermissionRequiredMixin,generic.UpdateView):
    model=models.Series
    form_class = forms.SeriesForm
    template_name = 'reference_book/edit_series.html'
    login_url = 'home_page:login'
    permission_required = 'reference.change_series'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['crup_name'] = 'Update'
        return context

class DeleteSeries(LoginRequiredMixin, PermissionRequiredMixin,generic.DeleteView):
    model=models.Series
    form_class = forms.SeriesForm
    template_name = 'reference_book/delete_series.html'
    login_url = 'home_page:login'
    permission_required = 'reference.delete_series'
    def get_success_url(self):
        return reverse_lazy('reference:series_list')


class ShowGenres(LoginRequiredMixin, PermissionRequiredMixin,generic.ListView):
    model = models.Genre
    template_name = 'reference_book/list_genre.html'
    login_url = 'home_page:login'
    permission_required = 'reference.view_genre'

class ShowGenre (LoginRequiredMixin, PermissionRequiredMixin,generic.DetailView):
    model = models.Genre
    template_name = 'reference_book/detail_genre.html'
    login_url = 'home_page:login'
    permission_required = 'reference.view_genre'

class CreateGenre (LoginRequiredMixin, PermissionRequiredMixin,generic.CreateView):
    model = models.Genre
    form_class = forms.GenreForm
    template_name = 'reference_book/edit_genre.html'  
    login_url = 'home_page:login'
    permission_required = 'reference.add_genre'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['crup_name'] = 'Create'
        return context

class UpdateGenre (LoginRequiredMixin, PermissionRequiredMixin,generic.UpdateView):
    model=models.Genre
    form_class = forms.GenreForm
    template_name = 'reference_book/edit_genre.html'
    login_url = 'home_page:login'
    permission_required = 'reference.change_genre'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['crup_name'] = 'Update'
        return context

class DeleteGenre(LoginRequiredMixin, PermissionRequiredMixin,generic.DeleteView):
    model=models.Genre
    form_class = forms.GenreForm
    template_name = 'reference_book/delete_genre.html'
    login_url = 'home_page:login'
    permission_required = 'reference.delete_genre'
    def get_success_url(self):
        return reverse_lazy('reference:genres_list')

class ShowPublishings(LoginRequiredMixin, PermissionRequiredMixin,generic.ListView):
    model = models.Publishing
    template_name = 'reference_book/list_publishing.html'
    login_url = 'home_page:login'
    permission_required = 'reference.view_publishing'

class ShowPublishing (LoginRequiredMixin, PermissionRequiredMixin,generic.DetailView):
    model = models.Publishing
    template_name = 'reference_book/detail_publishing.html'
    login_url = 'home_page:login'
    permission_required = 'reference.view_publishing'

class CreatePublishing (LoginRequiredMixin, PermissionRequiredMixin,generic.CreateView):
    model = models.Publishing
    form_class = forms.PublishingForm
    template_name = 'reference_book/edit_publishing.html' 
    login_url = 'home_page:login'
    permission_required = 'reference.add_publishing'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['crup_name'] = 'Create'
        return context

class UpdatePublishing (LoginRequiredMixin, PermissionRequiredMixin,generic.UpdateView):
    model=models.Publishing
    form_class = forms.PublishingForm
    template_name = 'reference_book/edit_publishing.html'
    login_url = 'home_page:login'
    permission_required = 'reference.change_publishing'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['crup_name'] = 'Update'
        return context

class DeletePublishing(LoginRequiredMixin, PermissionRequiredMixin,generic.DeleteView):
    model=models.Publishing
    form_class = forms.PublishingForm
    template_name = 'reference_book/delete_publishing.html'
    login_url = 'home_page:login'
    permission_required = 'reference.delete_publishing'

    def get_success_url(self):
        return reverse_lazy('reference:publish_list')