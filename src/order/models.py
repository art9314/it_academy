from django.db import models

# Create your models here.
from django.db import models
from django.contrib.sessions.models import Session
from carts.models import Cart

# Create your models here.

class CustomSession(Session):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
    )
    class Meta:
        app_label = 'cart_id'


class Status(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"


class Order(models.Model):
    cart = models.OneToOneField(
        Cart,
        on_delete=models.PROTECT,
        verbose_name="Order"
    )
    status = models.ForeignKey(Status,
    on_delete=models.PROTECT
    )
    contact_info = models.TextField(
        verbose_name="Contact info",
    )
    created = models.DateTimeField(
        verbose_name="Created",
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name="Updated",
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
        return self.contact_info

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"