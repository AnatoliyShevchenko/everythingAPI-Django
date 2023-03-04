from rest_framework import serializers
from rest_framework.serializers import ValidationError

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser

from .models import Card, Terminal, Transaction


User: AbstractBaseUser = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """User Serializer."""

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
        )


class CardSerializer(serializers.ModelSerializer):
    """Card Serializer."""

    user = UserSerializer()

    class Meta:
        model = Card
        fields = '__all__'


class SearchSerializer(serializers.Serializer):
    """Seek And Destroy."""

    number = serializers.CharField()
    cvv = serializers.CharField()
    date_expired = serializers.DateField()


class TerminalSerializer(serializers.ModelSerializer):
    """Serializer for terminals."""

    class Meta:
        model = Terminal
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    """Serializer for transactions."""
    out_card = serializers.CharField(required=True)
    to_card = serializers.CharField(required=False)
    terminal = serializers.CharField(required=False)
    money = serializers.DecimalField(
        required=True, 
        max_digits=10, 
        decimal_places=2
    )

    class Meta:
        model = Transaction
        fields = (
            'out_card',
            'to_card',
            'terminal',
            'money',
        )
