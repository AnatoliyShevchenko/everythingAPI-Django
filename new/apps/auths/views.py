from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action

from django.contrib.auth import login, logout, authenticate

from typing import Optional

from lessons.models import Book
from .models import User
from .serializers import (
    UserSerializer, 
    UserBookSerializer,
    LoginSerializer,
    RegSerializer
)

# Create your views here.
class UserView(ViewSet):
    """User View."""

    queryset = User.objects.all()
    second_queryset = Book.objects.all()

    def list(self, request: Request, *args, **kwargs) -> Response:
        users = self.queryset.all()
        serializer: UserSerializer = \
        UserSerializer(
            users,
            many=True
        )
        return Response({
            "result" : serializer.data
        })

    def retrieve(self, request: Request, pk: str) -> Response:
        """GET Method. get some object."""

        user: Optional[User] = None
        try:
            user = self.queryset.get(
                id=pk
            )
            serializer: UserBookSerializer = \
            UserBookSerializer(user)
        except User.DoesNotExist:
            return Response({
                'message': 'error'
            })
        else:
            return Response({
                'user': serializer.data,
            })


class UserRegView(ViewSet):
    """Class for registration User."""

    queryset = User.objects.all()

    def create(self, request: Request) -> Response:
        serializer: RegSerializer = \
            RegSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'User' : 'registration success'
            })
        return Response({
            'error' : serializer.errors
        })


class LoginView(ViewSet):
    """Login User."""

    queryset = User.objects.all()

    def create(self, request: Request) -> Response:
        serializer: LoginSerializer = \
            LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'error' : serializer.errors
            })
        username = serializer.data['username']
        password = serializer.data['password']
        user = authenticate(
            username=username,
            password=password
        )
        login(request, user)
        return Response({
            'message' : 'autorization success'
        })


class LogoutView(ViewSet):
    """Logout User."""

    queryset = User.objects.all()

    def list(self, request) -> Response:
        if not request.user:
            return Response({
                'error' : 'not autorized'
            })

        logout(request)
        return Response({
            "message" : "kill"
        })
