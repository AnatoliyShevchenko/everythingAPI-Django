from django.db import models
from django.core.exceptions import ValidationError

from auths.models import User

# Create your models here.
class Book(models.Model):
    """Book model for project."""

    title = models.CharField(
        verbose_name='book',
        max_length=200
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    description = models.TextField(
        verbose_name='description'
    )
    price = models.DecimalField(
        verbose_name='price',
        max_digits=10, 
        decimal_places=2
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __str__(self) -> str:
        return f"{self.title} | {self.author.first_name} | {self.price}"
    
    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)

    def clean(self) -> None:
        if (self.price <= 0) and (not self.price):
            raise ValidationError('Price lte zero')
        return super().clean()