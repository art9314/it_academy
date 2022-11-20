from django.shortcuts import render
from . import models, forms
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy


class ShowProdCardList(LoginRequiredMixin, PermissionRequiredMixin,generic.ListView):
    model = models.Books
    template_name = 'prod_card/list_pc.html'
    login_url = 'home_page:login'
    permission_required = 'product_card.view_book'


class ShowProdCard(LoginRequiredMixin, PermissionRequiredMixin,generic.DetailView):
    model = models.Books
    template_name = 'prod_card/detail_pc.html'
    login_url = 'home_page:login'
    permission_required = 'product_card.view_book'


class CreateProdCard(LoginRequiredMixin, PermissionRequiredMixin,generic.CreateView):
    model = models.Books
    form_class = forms.ProdCardForm
    template_name = 'prod_card/edit_pc.html'
    login_url = 'home_page:login'
    permission_required = 'product_card.add_book'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['crup_name'] = 'Create'
        return context


class UpdateProdCard(LoginRequiredMixin, PermissionRequiredMixin,generic.UpdateView):
    model = models.Books
    form_class = forms.ProdCardForm
    template_name = 'prod_card/edit_pc.html'
    login_url = 'home_page:login'
    permission_required = 'product_card.change_book'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['crup_name'] = 'Update'
        return context


class DeleteProdCard(LoginRequiredMixin, PermissionRequiredMixin,generic.DeleteView):
    model = models.Books
    template_name = 'prod_card/delete_pc.html'
    login_url = 'home_page:login'
    permission_required = 'product_card.delete_book'

    def get_success_url(self):
        return reverse_lazy('prod_card:prod_card_list')