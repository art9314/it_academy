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
    template_name = 'reference_book/list.html'
    login_url = 'home_page:login'
    permission_required = 'references.view_bookauthor'
    
class ShowAuthor (LoginRequiredMixin, PermissionRequiredMixin,generic.DetailView):
    model = models.Author
    template_name = 'reference_book/detail.html'
    login_url = 'home_page:login'
    permission_required = 'references.view_bookauthor'

class CreateAuthor (LoginRequiredMixin, PermissionRequiredMixin,generic.CreateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'reference_book/edit.html' 
    login_url = 'home_page:login'
    permission_required = 'references.add_bookauthor' 
    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args,**kwargs)
            context['crup_name'] = 'Create'
            return context

class UpdateAuthor (LoginRequiredMixin, PermissionRequiredMixin,generic.UpdateView):
    model=models.Author
    form_class = forms.AuthorForm
    template_name = 'reference_book/edit.html'
    login_url = 'home_page:login'
    permission_required = 'references.change_bookauthor'
    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args,**kwargs)
            context['crup_name'] = 'Update'
            return context

class DeleteAuthor (LoginRequiredMixin, PermissionRequiredMixin,generic.DeleteView):
    model=models.Author
    template_name = 'reference_book/delete.html'
    login_url = 'home_page:login'
    permission_required = 'references.delete_bookauthor'
    def get_success_url(self):
        return reverse_lazy('references:authors_list')

class ShowSerie(LoginRequiredMixin, PermissionRequiredMixin,generic.ListView):
    model = models.Series
    template_name = 'reference_book/list_series.html'
    login_url = 'home_page:login'
    permission_required = 'references.view_bookseries'

class ShowSeries (LoginRequiredMixin, PermissionRequiredMixin,generic.DetailView):
    model = models.Series
    template_name = 'reference_book/detail.html'
    login_url = 'home_page:login'
    permission_required = 'references.view_bookseries'

class CreateSeries (LoginRequiredMixin, PermissionRequiredMixin,generic.CreateView):
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'reference_book/edit.html'
    login_url = 'home_page:login'
    permission_required = 'references.add_bookseries'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['crup_name'] = 'Create'
        return context  

class UpdateSeries (LoginRequiredMixin, PermissionRequiredMixin,generic.UpdateView):
    model=models.Series
    form_class = forms.SeriesForm
    template_name = 'reference_book/edit.html'
    login_url = 'home_page:login'
    permission_required = 'references.change_bookseries'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['crup_name'] = 'Update'
        return context

class DeleteSeries(LoginRequiredMixin, PermissionRequiredMixin,generic.DeleteView):
    model=models.Series
    form_class = forms.SeriesForm
    template_name = 'reference_book/delete.html'
    login_url = 'home_page:login'
    permission_required = 'references.delete_bookseries'
    def get_success_url(self):
        return reverse_lazy('references:series_list')


class ShowGenres(LoginRequiredMixin, PermissionRequiredMixin,generic.ListView):
    model = models.Genre
    template_name = 'reference_book/list_genre.html'
    login_url = 'home_page:login'
    permission_required = 'references.view_bookgenre'

class ShowGenre (LoginRequiredMixin, PermissionRequiredMixin,generic.DetailView):
    model = models.Genre
    template_name = 'reference_book/detail.html'
    login_url = 'home_page:login'
    permission_required = 'references.view_bookgenre'

class CreateGenre (LoginRequiredMixin, PermissionRequiredMixin,generic.CreateView):
    model = models.Genre
    form_class = forms.GenreForm
    template_name = 'reference_book/edit.html'  
    login_url = 'home_page:login'
    permission_required = 'references.add_bookgenre'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['crup_name'] = 'Create'
        return context

class UpdateGenre (LoginRequiredMixin, PermissionRequiredMixin,generic.UpdateView):
    model=models.Genre
    form_class = forms.GenreForm
    template_name = 'reference_book/edit.html'
    login_url = 'home_page:login'
    permission_required = 'references.change_bookgenre'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['crup_name'] = 'Update'
        return context

class DeleteGenre(LoginRequiredMixin, PermissionRequiredMixin,generic.DeleteView):
    model=models.Genre
    form_class = forms.GenreForm
    template_name = 'reference_book/delete.html'
    login_url = 'home_page:login'
    permission_required = 'references.delete_bookgenre'
    def get_success_url(self):
        return reverse_lazy('references:genres_list')

class ShowPublishings(LoginRequiredMixin, PermissionRequiredMixin,generic.ListView):
    model = models.Publishing
    template_name = 'reference_book/list_genre.html'
    login_url = 'home_page:login'
    permission_required = 'references.view_bookpublishing'

class ShowPublishing (LoginRequiredMixin, PermissionRequiredMixin,generic.DetailView):
    model = models.Publishing
    template_name = 'reference_book/detail.html'
    login_url = 'home_page:login'
    permission_required = 'references.view_bookpublishing'

class CreatePublishing (LoginRequiredMixin, PermissionRequiredMixin,generic.CreateView):
    model = models.Publishing
    form_class = forms.PublishingForm
    template_name = 'reference_book/edit.html' 
    login_url = 'home_page:login'
    permission_required = 'references.add_bookpublishing'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['crup_name'] = 'Create'
        return context

class UpdatePublishing (LoginRequiredMixin, PermissionRequiredMixin,generic.UpdateView):
    model=models.Publishing
    form_class = forms.PublishingForm
    template_name = 'reference_book/edit.html'
    login_url = 'home_page:login'
    permission_required = 'references.change_bookpublishing'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['crup_name'] = 'Update'
        return context

class DeletePublishing(LoginRequiredMixin, PermissionRequiredMixin,generic.DeleteView):
    model=models.Publishing
    form_class = forms.PublishingForm
    template_name = 'reference_book/delete.html'
    login_url = 'home_page:login'
    permission_required = 'references.delete_bookpublishing'

    def get_success_url(self):
        return reverse_lazy('references:publish_list')