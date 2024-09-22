from django.contrib import admin

from .models import CartItem, Card, Branch, Discount, DeliveryTariff, Order


admin.site.register(CartItem)
admin.site.register(Card)
admin.site.register(Branch)
admin.site.register(Discount)
admin.site.register(DeliveryTariff)
admin.site.register(Order)
