from decimal import Decimal
from django.db import models
from django.db.models import Sum
from core.models import StatusDate, TimeStampedModel

from django.db.models.signals import pre_save
from .signals import generate_contract_identifier


DECIMAL_OPTS = {
    'max_digits': 20,
    'decimal_places': 2,
    'help_text': 'Ex: 1000.00',
    'default': 0.0,
}

DECIMAL_NULL_OPTS = {
    'max_digits': 20,
    'decimal_places': 2,
    'help_text': 'Ex: 1000.00',
    'blank': True,
    'null': True,
}


class LoanContract(StatusDate):
    '''
    Responsible for representing
    the loan contracts sent
    by users and belonging to a bank
    and to a customer.
    '''
    identifier = models.CharField('Identificador', max_length=10, unique=True)
    amount = models.DecimalField('Valor', **DECIMAL_OPTS)
    interest_rate = models.DecimalField('Taxa de juros', **DECIMAL_OPTS)
    ip_address = models.GenericIPAddressField('Endereço IP')
    submission_date = models.DateField('Data de submissão', auto_now_add=True)
    responsible = models.ForeignKey(
        'users.User',
        on_delete=models.PROTECT,
        verbose_name='Responsável'
    )
    bank = models.ForeignKey(
        'financial.Bank',
        on_delete=models.PROTECT,
        verbose_name='Banco'
    )
    customer = models.ForeignKey(
        'customers.Customer',
        on_delete=models.PROTECT,
        verbose_name='Cliente'
    )

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        ordering = ['submission_date']

    def __str__(self):
        params = {
            'id': self.identifier,
            'customer': self.customer
        }
        return 'Contrato {id} do cliente {customer}'.format(**params)

    @property
    def amount_due(self):
        amount_total = self._amount_total()
        amount_str = 'R$ {0:.2f}'.format(amount_total)
        return amount_str.replace('.', ',')

    def _amount_total(self):
        amount_rate = self.amount * (self.interest_rate / Decimal('100.0'))
        return self.amount + amount_rate - self._sum_payments()

    def _sum_payments(self):
        payments = self.loancontractpayment_set.all()
        if not payments.exists():
            return Decimal('0.0')
        total = payments.aggregate(sum_payment_amount=Sum('payment_amount'))
        return total['sum_payment_amount']


class LoanContractPayment(TimeStampedModel):
    '''
    Responsible for representing
    the loan contracts payments sent by users.
    '''
    loan_contract = models.ForeignKey(
        'contracts.LoanContract',
        on_delete=models.PROTECT,
        verbose_name='Contrato'
    )
    payment_amount = models.DecimalField('Valor do pagamento', **DECIMAL_OPTS)
    payment_date = models.DateField('Data do pagamento')

    class Meta:
        verbose_name = 'Pagamento de Contrato'
        verbose_name_plural = 'Pagamentos de Contratos'
        ordering = ['payment_date']

    def __str__(self):
        params = {
            'id': self.loan_contract.identifier,
            'amount': '{0:.2f}'.format(self.payment_amount)
        }
        return 'Pagamento: Contrato {id} | Valor R$ {amount}'.format(**params)


# Signals connect
pre_save.connect(generate_contract_identifier, sender=LoanContract)
