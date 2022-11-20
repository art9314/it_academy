from django.db import models
from django.contrib.auth.models import User
from prod_card.models import Books
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.utils import timezone


class AppUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        unique=True,
        max_length=30,
    )
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    email = models.EmailField()
    index = models.IntegerField()
    phone = models.IntegerField(help_text="Enter the number.")
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    reserve_address = models.CharField(blank=True, null=True, max_length=50)
    additional_info = models.CharField(blank=True, null=True, max_length=200)

    is_staff = models.BooleanField(default=False,)
    is_active = models.BooleanField(default=True,)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'username'
        verbose_name_plural = 'usernames'
        abstract = False

class Comment(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE,related_name='comments')
    username = models.ForeignKey('AppUser', on_delete=models.CASCADE, related_name='user_name')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

        def __str__(self):
            return self.text
    