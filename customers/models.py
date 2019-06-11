from django.db import models
from core.models import StatusDate

from core.utils import CPF, Phone


class Customer(StatusDate):
    cpf = models.CharField('CPF', max_length=14)
    name = models.CharField('Nome', max_length=200)
    phone = models.CharField('Celular', max_length=15, blank=True)
    email = models.EmailField('E-mail')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['name']

    def __str__(self):
        return '{0}'.format(self.get_cpf())

    def get_cpf(self):
        return CPF().format(self.cpf)

    def get_phone(self):
        return 'Não informado' if not self.phone else Phone().mask(self.phone)

    def serialize(self):
        return {
            'cpf': self.get_cpf(),
            'name': self.name,
            'phone': self.get_phone(),
            'email': self.email
        }