from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

from datetime import date, timedelta


User: AbstractBaseUser = get_user_model()


class Card(models.Model):
    """Card for user."""

    number = models.CharField(
        max_length=16,
        verbose_name='номер',
        unique=True,
        validators=[
            MinLengthValidator(16, message='must be 16 chars')
        ]
    )
    date_expired = models.DateField(
        verbose_name='дата окончания',
        default=date.today() + timedelta(days=365*4)
    )
    cvv = models.CharField(
        verbose_name='cvv код',
        max_length=3,
        validators=[
            MinLengthValidator(3, message='must be 3 chars')
        ]
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'карта'
        verbose_name_plural = 'карты'

    def __str__(self) -> str:
        return f'{self.user}'


class Terminal(models.Model):
    """Terminal to money."""

    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        unique=True
    )
    address = models.CharField(
        verbose_name='адрес терминала',
        max_length=50,
        unique=True
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'терминал'
        verbose_name_plural = 'терминалы'

    def __str__(self) -> str:
        return self.address


class Transaction(models.Model):
    """Transaction for money."""

    out_card = models.ForeignKey(
        to=Card,
        on_delete=models.CASCADE,
        related_name='откуда'
    )
    to_card = models.ForeignKey(
        to=Card,
        on_delete=models.CASCADE,
    )
    terminal = models.ForeignKey(
        to=Terminal,
        on_delete=models.CASCADE,
    )
    money = models.DecimalField(
        verbose_name='сумма перевода',
        max_digits=10,
        decimal_places=2
    )
    date_created = models.DateTimeField(
        auto_now=True,
        verbose_name='дата платежа'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'транзакция'
        verbose_name_plural = 'транзакции'

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)

    def clean(self) -> None:
        if self.money <= 0:
            raise ValidationError('Money must be more than zero.')
        elif self.to_card.DoesNotExist and self.terminal.DoesNotExist:
            raise ValidationError('Choose one of them.')
        elif self.to_card and self.terminal:
            raise ValidationError('Choose the only one.')
        return super().clean()