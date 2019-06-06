from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    search_fields = ['email', 'username']
    list_display = ('email', 'created_at')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            'Informações Pessoais', {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'avatar'
                )
            }
        ),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )


admin.site.register(User, UserAdmin)