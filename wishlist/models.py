from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class WishList(models.Model):
    """
    Model that shows products in a users wishlist
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="WishListLineItems", related_name="product_wishlist")

    def __str__(self):
        return f'Wishlist for {self.user}'


class WishListLineItems(models.Model):
    """
    A model thats lets users add products
    to their wishlist
    """
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(WishList, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
