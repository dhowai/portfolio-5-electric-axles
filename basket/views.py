from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product


def view_basket(request):
    """ A view that renders the basket content page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specific product to the shopping basket,
    checks if item is already in the basket and if it has sizes."""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request, f'Updated size {size.upper()} {product.name}  quantity to \
                    {basket[item_id]["items_by_size"][size]}')
            else:
                basket[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request, f'Added size \
                         {size.upper()} {product.name} to your Basket')
        else:
            basket[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size \
                 {size.upper()} {product.name} to your Basket')
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to \
                 {basket[item_id]}')
        else:
            basket[item_id] = quantity
            messages.success(
                request, f'Added {product.name} to your basket Successfully')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Adjust the quantity of the specifc product and amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if quantity > 0:
            basket[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity \
                 to {basket[item_id]["items_by_size"][size]}')
        else:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
            messages.success(request, f'Removed size \
                 {size.upper()} {product.name} from your Basket')
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to \
                {basket[item_id]}')
        else:
            basket.pop(item_id)
            messages.success(
                request, f'Removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove item from basket"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        basket = request.session.get('basket', {})

        if size:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
            messages.success(
                request, f"Removed size {size.upper()} {product.name} \
                     from your basket")
        else:
            basket.pop(item_id)
            messages.success(
                request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as error:
        messages.error(request, f'Error removing item: {error}')
        return HttpResponse(status=500)
