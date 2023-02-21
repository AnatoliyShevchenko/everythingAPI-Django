from rest_framework import serializers

from auths.serializers import UserSerializer


class BookSerializer(serializers.Serializer):
    """Book Serializer."""

    id = serializers.IntegerField()
    title = serializers.CharField()
    author = UserSerializer()
    description = serializers.CharField()
    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2
    )
