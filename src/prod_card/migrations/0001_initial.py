# Generated by Django 4.1.2 on 2022-11-09 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reference_book', '0004_alter_author_logo_alter_author_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Book name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='Book image')),
                ('price', models.DecimalField(decimal_places=2, help_text='Currency in BYN', max_digits=6, verbose_name='Price')),
                ('publishing_year', models.CharField(max_length=10, verbose_name='Publishing year')),
                ('pages', models.IntegerField(verbose_name='Pages')),
                ('binding', models.CharField(max_length=30, verbose_name='Binding')),
                ('format', models.CharField(max_length=8, verbose_name='Format')),
                ('isbn', models.CharField(max_length=25, verbose_name='ISBN')),
                ('weight', models.IntegerField(verbose_name='Weight')),
                ('age_restriction', models.IntegerField(verbose_name='Age restriction')),
                ('available_books', models.IntegerField(verbose_name='Quantity  of books available')),
                ('activity', models.CharField(max_length=3, verbose_name='In stock')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Rating')),
                ('date_of_addition', models.DateField(verbose_name='Date of addition')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Date the card was last modified')),
                ('description', models.TextField(blank=True, null=True)),
                ('author', models.ManyToManyField(to='reference_book.author')),
                ('genre', models.ManyToManyField(to='reference_book.genre')),
                ('publishing_house', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reference_book.publishing', verbose_name='Publishing')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reference_book.series', verbose_name='Series')),
            ],
        ),
    ]
