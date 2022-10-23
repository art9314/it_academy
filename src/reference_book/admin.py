from django.contrib import admin
from . import models
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'date_of_birth', 'date_of_birth', 'description')
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'number_series')
class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
class PublishingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Series, SeriesAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Publishing, PublishingAdmin)