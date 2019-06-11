from rest_framework import serializers

from contracts.models import LoanContract


class LoanContractSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LoanContract
        fields = (
            'id',
            'identifier',
            'amount',
            'interest_rate',
            'submission_date',
            'bank',
            'customer'
        )

    def __init__(self, *args, **kwargs):
        self.fields['identifier'].required = False
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        user = LoanContract(**validated_data)
        user.responsible = self.context['request'].user
        user.ip_address = self.context['request'].META.get('REMOTE_ADDR')
        user.save()
        return user
