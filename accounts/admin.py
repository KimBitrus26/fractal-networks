from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_active', 
                    'is_superuser',)
    list_filter = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'middle_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser')}),
    )   
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'password1', 'password2', 'first_name', 'middle_name', 'last_name', ),
    }),
) 
    search_fields = ('email',)
    ordering = ("-created_at",)

admin.site.register(User, CustomUserAdmin)
