from django.shortcuts import render
from . import models, forms
from django.views import generic
from django.urls import reverse_lazy


class ShowProdCardList(generic.ListView):
    model = models.Books
    template_name = 'prod_card/list_pc.html'


class ShowProdCard(generic.DetailView):
    model = models.Books
    template_name = 'prod_card/detail_pc.html'


class CreateProdCard(generic.CreateView):
    model = models.Books
    form_class = forms.ProdCardForm
    template_name = 'prod_card/edit_pc.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['cu_name'] = 'Create'
        return context


class UpdateProdCard(generic.UpdateView):
    model = models.Books
    form_class = forms.ProdCardForm
    template_name = 'prod_card/edit_pc.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['cu_name'] = 'Update'
        return context


class DeleteProdCard(generic.DeleteView):
    model = models.Books
    template_name = 'prod_card/delete_pc.html'

    def get_success_url(self):
        return reverse_lazy('prod_card:prod_card_list')