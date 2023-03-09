from django.db import models


class Station(models.Model):
    """Station model."""

    radio_id: int = models.IntegerField(
        verbose_name='радио айди'
    )
    radio_name: str = models.CharField(
        verbose_name='название радио',
        max_length=30,
        unique=True
    )
    radio_image: str = models.CharField(
        verbose_name='картинка радио',
        max_length=50
    )
    radio_url: str = models.URLField(
        verbose_name='юрл радио',
        max_length=50
    )
    genre: str = models.CharField(
        verbose_name='жанр',
        max_length=30
    )
    country_name: str = models.CharField(
        verbose_name='название страны',
        max_length=65
    )
    country_id: int = models.IntegerField(
        verbose_name='айди страны'
    )