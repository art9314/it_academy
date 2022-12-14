# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from prod_card.models import Books

User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        User, null=True, blank=True,
        related_name="Customer",
        verbose_name="Customer",
        on_delete=models.PROTECT)        

    @property
    def total_price_cart(self):
        goods = self.goods.all()
        total_price_cart = 0
        for good in goods:
            total_price_cart += good.total_price
        return total_price_cart

class BooksInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        related_name="goods",
        on_delete=models.CASCADE,
        verbose_name="Cart"
        )
    book = models.ForeignKey(
        Books,
        on_delete=models.PROTECT,
        verbose_name='Book',)

    quantity = models.IntegerField(
        verbose_name="Quantity",
        default=1)

    price = models.DecimalField(
        verbose_name='Price',
        max_digits=5,
        decimal_places=2, )

    @property
    def total_price(self):
        return self.price * self.quantity
