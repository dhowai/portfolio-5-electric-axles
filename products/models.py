from django.db import models


class Category(models.Model):
    """A model for product categories"""
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        """ Correct plural for category in admin"""
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    """A model for the products"""
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Order by product created"""
        ordering = ('-created',)

    def __str__(self):
        return self.name