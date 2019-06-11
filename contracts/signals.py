import random
import string


def generate_contract_identifier(sender, **kwargs):
    loan_contract = kwargs['instance']
    if not loan_contract.identifier:
        from .models import LoanContract
        unique_control = True
        while unique_control:
            size = 10
            chars = string.digits
            chars = chars.replace('0', '')
            identifier = ''.join(random.choice(chars) for _ in range(size))
            qs = LoanContract.objects.filter(
                identifier=identifier
            ).exclude(pk=loan_contract.pk)
            if not qs.exists():
                loan_contract.identifier = identifier
                loan_contract.save()
                unique_control = False
