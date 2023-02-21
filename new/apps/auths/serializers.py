from rest_framework import serializers

from lessons.models import Book


class UserSerializer(serializers.Serializer):
    """User Serializer."""

    id = serializers.IntegerField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
    is_active = serializers.BooleanField()
    date_joined = serializers.DateTimeField()


class UserBookSerializer(serializers.Serializer):
    """User Book Serializer."""

    id = serializers.IntegerField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
    is_active = serializers.BooleanField()
    date_joined = serializers.DateTimeField()
    books = serializers.SerializerMethodField(
        method_name='get_books'
    )


    def get_books(self, pk):
        result = []
        books = Book.objects.filter(author=pk)
        for i in range(len(books)):
            result.append(books[i].title)
        return result
