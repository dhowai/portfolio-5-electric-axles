from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """
    A view to show all products
    """
    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    return render(request, 'products/products.html', {'products': products, 'search_term': query})


def product_detail(request, slug):
    """
    A view to show the product detail on their own page
    """
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'products/product_detail.html', {'product': product})


def categories(request):
    """
    A view to show all categories, for now
    """
    return {
        'categories': Category.objects.all()
    }


def category_list(request, category_slug):
    """
     A view to show the category list
    """
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'products/category.html', {'category': category, 'products': products})


def add_product(request):
    """Add a product to the store"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product due to invalid form.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, slug):
    """Edit a product from the store"""
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the product!')
            return redirect(reverse('product_detail', args=[product.slug]))
        else:
            messages.error(request, 'Failed to edit product due to invalid form.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are Editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
