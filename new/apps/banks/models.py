from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MinLengthValidator

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