from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import WishList


@login_required
def wishlist(request):
    """
    A view to render the user wishlist
    """
    wishlist = None
    try:
        wishlist = WishList.objects.get(user=request.user)
    except WishList.DoesNotExist:
        pass

    return render(request, 'wishlist/wishlist.html', {'wishlist': wishlist})


@login_required
def add_to_wishlist(request, slug):
    """
    Add a product to the registered user wishlist
    """
    product = get_object_or_404(Product, slug=slug)

    wishlist, _ = WishList.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    messages.info(request, f'Added {product.name} to your Wishlist Successfully')

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_wishlist(request, slug):
    """
    Remove a product from the registered user wishlist
    """
    product = get_object_or_404(Product, slug=slug)
    wishlist = WishList.objects.get(user=request.user)

    wishlist.products.remove(product)
    messages.info(request, f'Removed {product.name} from your Wishlist Successfully')

    return redirect(request.META.get('HTTP_REFERER'))
