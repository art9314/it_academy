

# Create your views here.
from django.shortcuts import render
from django.views import generic, View
from prod_card.models import Books
from .forms import CommentForm
from django.core.paginator import Paginator
from .models import Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import get_object_or_404, render


class CatalogView(View):

    def get(self, request, *args, **kwargs):
        book = Books.objects.all()
        paginator = Paginator(book, 12)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'catalog/catalog.html',
            context={
                'page_obj': page_obj
            }
        )

class BookDetail(generic.DetailView):
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Books, pk=kwargs['pk'])
        last_posts = Books.objects.all().order_by('-id')[:3]
        comment_form = CommentForm()
        return render(request, 'catalog/book_detail.html', context={
            'book': book,
            'last_posts': last_posts,
            'comment_form': comment_form,
        })


    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            book = get_object_or_404(Books, pk=kwargs['pk'])
            comment = Comment.objects.create(book=book, username=username,
                                             text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, 'catalog/book_detail.html', context={
            'comment_form': comment_form
        })


class SearchResultView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        results = ''
        if query:
            results = Books.objects.filter(
                Q(author__name__icontains=query) | Q(name__icontains=query) | Q(author__surname__icontains=query) | Q(genre__genre_name__icontains=query) | Q(series__book_series__icontains=query)
            ).distinct()
        paginator = Paginator(results, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'catalog/search.html', context={
            'title': 'Search',
            'results': page_obj,
            'count': paginator.count,
        })