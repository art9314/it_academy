from django.contrib import admin
from prod_card.models import Books
# Register your models here.
class BooksAdmin(admin.ModelAdmin):   
    list_fields = ('name', 'author', 'price', 'series', 'genre', 'publishing_year', 'pages', 'binding','format', 'isbn', 'weight',
         'age_restriction', 'publishing', 'available_books', 'activity','rating', 'date_of_addition', 'description')

    def book_author(self, obj):        
            return ", ".join([s.name + " " + s.surname for s in obj.author.all()])

    def book_genre(self, obj):            
            return ", ".join([s.genre_name for s in obj.genre.all()])

admin.site.register(Books, BooksAdmin)