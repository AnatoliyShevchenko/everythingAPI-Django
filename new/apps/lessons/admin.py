from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

from typing import Optional

from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    """Model admin."""

    model = Book
    list_display = [
        'title',
        'price',
        'author',
        'description'
    ]
    readonly_fields = (
        
    )

    def get_readonly_fields(
        self, 
        request: WSGIRequest, 
        obj: Optional[Book] = ...):
        if not obj:
            return self.readonly_fields
        return self.readonly_fields + ('price',)

admin.site.register(Book, BookAdmin)