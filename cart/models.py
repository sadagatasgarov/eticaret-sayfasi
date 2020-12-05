from django.db import models
from product.models import Product
from django.contrib.auth.models import User
# Create your models here.


STATUS = [
    ('waiting', 'Bekleniyor'),
    ['buyed', 'Satin alindi'],
    ('deleted', 'silindi'),
]


# CartItem - > Product


class ShoppingCartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"{self.product.title}-{self.product.price} TL"
    


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    items = models.ManyToManyField(ShoppingCartItem, blank=True, null=True)
    total_price = models.FloatField()
    status = models.CharField(
        default='waiting',
        choices=STATUS,
        max_length=10
    )
