# Generated by Django 2.2.2 on 2019-06-11 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Excluído em')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('status', models.BooleanField(default=True, verbose_name='Ativo')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Celular')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['name'],
            },
        ),
    ]
