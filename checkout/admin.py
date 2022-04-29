from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """Custom Admin for orderlineitems"""
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Custom Admin for orders"""
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                        'delivery_cost', 'order_total',
                        'grand_total', 'original_basket', 'stripe_pid',)

    fields = ('order_number', 'date', 'user_profile', 'full_name',
                'email', 'phone_number', 'country', 'postcode',
                'town_or_city', 'county', 'street_address1', 'street_address2',
                'delivery_cost', 'order_total', 'grand_total',
                'original_basket', 'stripe_pid',)

    list_display = ('order_number', 'date',
                    'full_name',
                    'delivery_cost', 'order_total', 'grand_total',)

    ordering = ('-date',)
