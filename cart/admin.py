from django.contrib import admin
from cart.models  import ShoppingCartItem, ShoppingCart
# Register your models here.






admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartItem)