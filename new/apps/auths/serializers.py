from rest_framework import serializers

from django.contrib.auth.hashers import make_password, check_password

from lessons.models import Book
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """User Serializer."""

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
        )


class RegSerializer(serializers.ModelSerializer):
    """Reg Serializer."""

    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password2'
        )

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError(
                'passwords not match'
            )
        return super().validate(attrs)

    def save(self, **kwargs):
        user = User.objects.create(
            username = self.data.get('username'),
            email = self.data.get('email'),
            first_name = self.data.get('first_name'),
            last_name = self.data.get('last_name'),
            password = make_password(self.data.get('password'))
        )
        return user


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


class LoginSerializer(serializers.Serializer):
    """Login Serializer."""

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = User.objects.filter(username=attrs.get('username'))
        if not user:
            raise serializers.ValidationError(
                'user not found'
            )
        elif not check_password(
            attrs.get('password'), 
            user[0].password
        ):
            raise serializers.ValidationError(
                'invalid password'
            )
        return super().validate(attrs)