# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'user_type', 'is_staff')
    list_filter = ('user_type', 'is_staff', 'is_superuser')
    ordering = ('email',)
    search_fields = ('email','first_name','last_name')

    fieldsets = (
        (None, {'fields': ('email','password')}),
        ('Personal info', {'fields': ('first_name','last_name','phone','user_type')}),
        ('Permissions', {'fields': ('is_active','is_staff','is_superuser','groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','password1','password2','user_type'),
        }),
    )

admin.site.register(User, UserAdmin)
