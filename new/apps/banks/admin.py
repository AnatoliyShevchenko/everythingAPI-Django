from django.contrib import admin

from .models import (
    Card, 
    Terminal, 
    CardToCardTransaction, 
    CardToTerminalTransaction,
)

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


class CardToCardAdmin(admin.ModelAdmin):
    """Card to card trasaction admin."""

    model = CardToCardTransaction
    list_display = (
        'out_card',
        'to_card',
        'money',
        'date_created'
    )


class CardToTerminalAdmin(admin.ModelAdmin):
    """Card to terminal transaction."""

    model = CardToTerminalTransaction
    list_display = (
        'out_card', 
        'terminal',
        'money',
        'date_created'
    )


admin.site.register(Card, CardAdmin)
admin.site.register(Terminal, TerminalAdmin)
admin.site.register(CardToCardTransaction, CardToCardAdmin)
admin.site.register(CardToTerminalTransaction, CardToTerminalAdmin)
