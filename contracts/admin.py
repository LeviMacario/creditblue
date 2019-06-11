from django.contrib import admin
from .models import LoanContract, LoanContractPayment


class LoanContractPaymentInline(admin.StackedInline):
    model = LoanContractPayment


class LoanContractAdmin(admin.ModelAdmin):
    list_display = [
        'identifier',
        'customer',
        'amount',
        'interest_rate',
        'bank',
        'submission_date',
        'status'
    ]
    search_fields = (
        'identifier',
        'customer__name',
        'customer__email',
        'customer__phone'
    )
    list_filter = ['status']
    inlines = (LoanContractPaymentInline,)


class LoanContractPaymentAdmin(admin.ModelAdmin):
    list_display = [
        'loan_contract',
        'payment_amount',
        'payment_date',
        'created_at'
    ]
    search_fields = ('loan_contract__identifier',)


admin.site.register(LoanContract, LoanContractAdmin)
admin.site.register(LoanContractPayment, LoanContractPaymentAdmin)