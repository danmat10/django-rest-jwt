from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password',  'is_active', 'is_staff',
                           'is_superuser', 'last_login', 'user_type', 'role', 'registration', 'name')}),
        (_('Permissions'), {'fields': ('groups', 'user_permissions')}),
    )
    list_display = ('email', 'is_staff')
    search_fields = ('email', 'name')
    ordering = ('email',)
