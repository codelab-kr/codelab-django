from django.contrib import admin

from services.shop.apps.orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
