from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        'username',
        'email',
        'phone_number',
        'is_staff',
        'is_active',
    )
    list_filter = (
        'is_staff',
        'is_active',
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('email', 'phone_number')
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide', ),
                'fields': ('username', 'email', 'phone_number', 'password1', 'password2', 'is_staff', 'is_active')
            }
        ),
    )
    search_fields = (
        'username',
        'email',
    )
    ordering = ('username', )


admin.site.register(CustomUser, CustomUserAdmin)
