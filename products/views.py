from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm, ReviewForm


def all_products(request):
    """
    A view to show all products
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    return render(request, 'products/products.html', {'products': products, 'search_term': query, 'current_categories': categories, 'current_sorting': current_sorting})


def product_detail(request, slug):
    """
    A view to show the product detail on their own page
    """
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    form = ReviewForm()
    return render(request, 'products/product_detail.html', {'product': product, 'form': form})


def categories(request):
    """
    A view to show all categories, for now
    """
    return {
        'categories': Category.objects.all()
    }


@login_required
def add_product(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store management can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.slug]))
        else:
            messages.error(request, 'Failed to add product due to invalid form.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, slug):
    """Edit a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store management can do that.')
        return redirect(reverse('home'))

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


@login_required
def delete_product(request, slug):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store management can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, slug=slug)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, slug):
    """
    A view for the user to create a review for a product
    """
    product = get_object_or_404(Product, slug=slug)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.user = request.user
                review.save()
                messages.success(request, 'Your review was successfully posted')
                return redirect(reverse('product_detail', args=[product.slug]))
            else:
                messages.error(request, 'Failed to post Review, please try again later')

    return render(request, {'form': form})
