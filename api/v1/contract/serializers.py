from rest_framework import serializers

from contracts.models import LoanContract, LoanContractPayment
from financial.models import Bank
from customers.models import Customer


class BankSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bank
        fields = ('id', 'bank', 'name')


class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = (
            'id',
            'cpf',
            'name',
            'phone',
            'email'
        )


class LoanContractSerializer(serializers.ModelSerializer):

    bank = BankSerializer()
    customer = CustomerSerializer()
    
    class Meta:
        model = LoanContract
        fields = (
            'id',
            'identifier',
            'amount',
            'interest_rate',
            'submission_date',
            'bank',
            'customer',
            'amount_due',
        )

    def __init__(self, *args, **kwargs):
        self.fields['identifier'].required = False
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        data = validated_data
        bank, created = Bank.objects.get_or_create(bank=data['bank']['bank'])
        try:
            customer = Customer.objects.get(cpf=data['customer']['cpf'])
        except Customer.DoesNotExist:
            customer = Customer(
                cpf=data['customer']['cpf'],
                name=data['customer']['name'],
                email=data['customer']['email'],
                phone=data['customer']['phone']
            )
            customer.save()

        contract = LoanContract(
            amount=data['amount'],
            interest_rate=data['interest_rate'],
            bank=bank,
            customer=customer
        )
        contract.responsible = self.context['request'].user
        contract.ip_address = self.context['request'].META.get('REMOTE_ADDR')
        contract.save()
        return contract


class LoanContractPaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LoanContractPayment
        fields = (
            'id',
            'loan_contract',
            'payment_amount',
            'payment_date'
        )
