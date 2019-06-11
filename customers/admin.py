from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'cpf', 'name', 'created_at', 'status']
    search_fields = ('cpf', 'name', 'email', 'phone')
    list_filter = ['status']


admin.site.register(Customer, CustomerAdmin)