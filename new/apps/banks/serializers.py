from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser

from .models import Card


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
