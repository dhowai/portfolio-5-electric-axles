from django import forms
from .models import Product, ProductReview


class ProductForm(forms.ModelForm):
    """Form to add/edit products"""
    class Meta:
        """Form data"""
        model = Product
        fields = (
            'category', 'name', 'slug', 'description', 'price',
            'rating', 'image', 'has_sizes', 'in_stock')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control mb-3'


class ReviewForm(forms.ModelForm):
    """Form to add/edit products"""
    class Meta:
        """Form data"""
        model = ProductReview
        fields = ('title', 'body', 'rating', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'body': 'Write Something about the product',
            'rating': 'rating',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = 'form-control mb-3'
