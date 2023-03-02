from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from typing import Any


class UserManager(BaseUserManager):
    """ClientManager."""

    def create_user(
        self,
        email: str,
        first_name: str,
        last_name: str,
        username: str,
        password: str
    ) -> 'User':

        if not email:
            raise ValidationError('Email required')

        user: 'User' = self.model(
            email=self.normalize_email(email),
            # password=password
        )
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email: str,
        first_name: str,
        last_name: str,
        username: str,
        password: str
    ) -> 'User':

        user: 'User' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User."""

    email = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name='почта'
    )
    first_name = models.CharField(
        max_length=20,
        verbose_name='имя'
    )
    last_name = models.CharField(
        max_length=20,
        verbose_name='фамилия'
    )
    username = models.CharField(
        max_length=20,
        verbose_name='имя пользователя',
        unique=True
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='активность'
    )
    is_superuser = models.BooleanField(
        default=False,
        verbose_name='администратор'
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='менеджер'
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
        verbose_name='дата регистрации'
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = UserManager()

    class Meta:
        ordering = (
            '-date_joined',
        )
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def save(
        self,
        *args: Any,
        **kwargs: Any
    ) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'