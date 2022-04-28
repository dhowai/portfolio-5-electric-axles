from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('add/', views.add_product, name="add_product"),
    path('edit/<slug:slug>/', views.edit_product, name="edit_product"),
    path('delete/<slug:slug>/', views.delete_product, name="delete_product"),
    path('<slug:slug>/', views.product_detail, name="product_detail"),
    path('add_review/<slug:slug>/', views.add_review, name='add_review'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review')
]
