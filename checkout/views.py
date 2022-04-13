from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """
    View that checkouts sdfgs
    """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing here at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KI7n9AU0zMtBiIVWbusfvgWUxLdzI210ctXel9fEtGSaYm2S9jZW9b2RuOqnx3oA5A7r7PnQBtQH309GlW197l400agaNc7GU',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)
