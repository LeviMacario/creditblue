from django.contrib import admin
from .models import Bank


class BankAdmin(admin.ModelAdmin):
    list_display = ['id', 'bank', 'created_at', 'status']
    search_fields = ('bank',)
    list_filter = ['status']


admin.site.register(Bank, BankAdmin)