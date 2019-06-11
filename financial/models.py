from django.db import models
from core.models import StatusDate


class Bank(StatusDate):
    '''
    Classe que representa os bancos
    utilizados pelos usuários para recebimento
    de contratos de empréstimos de clientes diversos.

    Bancos Aceitos:           
    Itaú   
    Bradesco          
    Caixa Econômica
    Banco do Brasil
    Santander
    Banrisul
    Sicredi
    Sicoob
    Inter
    BRB
    '''

    BANK_CHOICES = (
        ('341', 'Itaú'),
        ('237', 'Bradesco'),
        ('104', 'Caixa Econômica'),
        ('001', 'Banco do Brasil'),
        ('033', 'Santander'),
        ('041', 'Banrisul'),
        ('748', 'Sicredi'),
        ('756', 'Sicoob'),
        ('077', 'Inter'),
        ('070', 'BRB'),
    )

    bank = models.CharField('Banco', max_length=5, choices=BANK_CHOICES)

    class Meta:
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'
        ordering = ['bank',]

    def __str__(self):
        return self.name

    @property
    def name(self):
        return dict(self.BANK_CHOICES)[self.bank]

