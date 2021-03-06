# Generated by Django 2.2.2 on 2019-06-11 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanContractPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Excluído em')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('payment_amount', models.DecimalField(decimal_places=2, default=0.0, help_text='Ex: 1000.00', max_digits=20, verbose_name='Valor do pagamento')),
                ('payment_date', models.DateField(verbose_name='Data do pagamento')),
                ('loan_contract', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contracts.LoanContract', verbose_name='Contrato')),
            ],
            options={
                'verbose_name': 'Pagamento de Contrato',
                'verbose_name_plural': 'Pagamentos de Contratos',
                'ordering': ['payment_date'],
            },
        ),
    ]
