from rest_framework import serializers
from rest_framework.serializers import ValidationError

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser

from .models import (
    Card, 
    Terminal, 
    CardToCardTransaction, 
    CardToTerminalTransaction,
)


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


class CardToCardSerializer(serializers.ModelSerializer):
    """Serializer for card to card transaction."""

    class Meta:
        model = CardToCardTransaction
        fields = ('out_card', 'to_card', 'money',)


class CardToTerminalSerializer(serializers.ModelSerializer):
    """Serializer for card to terminal transaction."""

    class Meta:
        model = CardToTerminalTransaction
        fields = ('out_card', 'terminal', 'money',)

