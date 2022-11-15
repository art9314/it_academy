# Generated by Django 4.1.2 on 2022-11-15 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod_card', '0002_rename_publishing_house_books_publishing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='image',
        ),
        migrations.AddField(
            model_name='books',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='Book logotip'),
        ),
    ]
