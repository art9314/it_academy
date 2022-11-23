from django.db import models
from reference_book.models import Author
from reference_book.models import Series
from reference_book.models import Genre
from reference_book.models  import Publishing
from django.urls import reverse_lazy
from django.utils.datetime_safe import date
from django.core.exceptions import ValidationError

# Create your models here.

class Books(models.Model):
    name = models.CharField(
       max_length=60,
       verbose_name="Book name")

    logo = models.ImageField(
        verbose_name="Book logotip",
        upload_to='uploads/%Y/%m/%d/',
        blank=True,
        null=True)

    author = models.ManyToManyField(
        Author)

    price = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        verbose_name="Price",
        help_text="Currency in BYN")

    series = models.ForeignKey(
        Series,
        verbose_name="Series",
        on_delete=models.PROTECT)

    genre = models.ManyToManyField(
        Genre)

    publishing_year=models.CharField(
        max_length=10,
        verbose_name="Publishing year")

    pages = models.IntegerField(
        verbose_name="Pages")

    binding = models.CharField(
        max_length=30,
        verbose_name="Binding")

    format = models.CharField(
        max_length=8,
        verbose_name="Format")

    isbn = models.CharField(
        max_length=25,
        verbose_name="ISBN")

    weight = models.IntegerField(
        verbose_name="Weight")

    age_restriction = models.IntegerField( 
        verbose_name="Age restriction")

    publishing = models.ForeignKey(
        Publishing,
        verbose_name="Publishing",
        on_delete=models.PROTECT)

    available_books = models.IntegerField(
        verbose_name="Quantity  of books available")

    activity = models.CharField(
        max_length = 3,
        verbose_name="In stock")

    rating = models.DecimalField(
        max_digits=2, 
        decimal_places=1,
        verbose_name="Rating")

    date_of_addition = models.DateField(
        verbose_name="Date of addition")

    modification_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Date the card was last modified")

    description = models.TextField(
        blank = True,
        null = True )
    

    def get_absolute_url(self):
        return reverse_lazy('prod_card:prod_card_detail', kwargs={'pk': self.pk})

    def clean(self):
        if str(self.date_of_addition) > str(date.today()):
            raise ValidationError({'date_of_addition': 'Must not be later than today!'})
        
    
