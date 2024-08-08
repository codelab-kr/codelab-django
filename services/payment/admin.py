from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Payment._meta.fields]
    # list_filter = ['paid', 'created', 'updated']
