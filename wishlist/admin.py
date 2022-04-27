from django.contrib import admin
from .models import WishList, WishListLineItems


admin.site.register(WishList)
admin.site.register(WishListLineItems)
