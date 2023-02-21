from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request

from typing import Optional

from lessons.models import Book
from .models import User
from .serializers import (
    UserSerializer, 
    UserBookSerializer
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
