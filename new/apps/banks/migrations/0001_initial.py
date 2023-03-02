# Generated by Django 4.1.6 on 2023-03-01 15:04

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16, unique=True, validators=[django.core.validators.MinLengthValidator(16, message='must be 16 chars')], verbose_name='номер')),
                ('date_expired', models.DateField(default=datetime.date(2027, 2, 28), verbose_name='дата окончания')),
                ('cvv', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3, message='must be 3 chars')], verbose_name='cvv код')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'карта',
                'verbose_name_plural': 'карты',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50, unique=True, verbose_name='адрес терминала')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'терминал',
                'verbose_name_plural': 'терминалы',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='сумма перевода')),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='дата платежа')),
                ('out_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='откуда', to='banks.card')),
                ('terminal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.terminal')),
                ('to_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.card')),
            ],
            options={
                'verbose_name': 'транзакция',
                'verbose_name_plural': 'транзакции',
                'ordering': ('-id',),
            },
        ),
    ]