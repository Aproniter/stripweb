from django.contrib import admin

from .models import Order, Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'currency')
    search_fields = ('name', 'price', 'order__payer')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('payer', 'created_at')


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
