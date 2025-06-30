from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Fields to display in list view
    list_display = ('username', 'email', 'is_admin', 'is_staff', 'is_active', 'last_login', 'date_joined')
    list_filter = ('is_admin', 'is_staff', 'is_active')

    # Search fields in admin search bar
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)

    # Fields to show in the user detail view
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields to use when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_admin', 'is_staff', 'is_active')}
        ),
    )

    # Enable readonly fields if needed
    readonly_fields = ('date_joined', 'last_login')

