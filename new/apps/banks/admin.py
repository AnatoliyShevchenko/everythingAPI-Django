from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

from .models import Card, Terminal, Transaction

# Register your models here.
class CardAdmin(admin.ModelAdmin):
    """Card admin."""

    model = Card
    list_display = (
        'number',
        'date_expired',
        'cvv',
        'user'
    )


class TerminalAdmin(admin.ModelAdmin):
    """Terminal Admin."""

    model = Terminal
    list_display = (
        'user',
        'address'
    )


class TransactionAdmin(admin.ModelAdmin):
    """Transaction admin."""

    model = Transaction
    list_display = (
        'out_card',
        'to_card',
        'terminal',
        'money',
        'date_created'
    )


admin.site.register(Card, CardAdmin)
admin.site.register(Terminal, TerminalAdmin)
admin.site.register(Transaction, TransactionAdmin)
