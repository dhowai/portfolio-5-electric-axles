from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """
    A view to show all products
    """
    products = Product.objects.all()

    return render(request, 'products/products.html', {'products': products})


def product_detail(request, slug):
    """
    A view to show the product detail on their own page
    """
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'products/product_detail.html', {'product': product})
