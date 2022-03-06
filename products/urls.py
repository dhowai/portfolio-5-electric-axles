from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<slug:slug>/', views.product_detail, name="product_detail"),
    path('category/<slug:category_slug>', views.category_list, name="category_list"),
]
