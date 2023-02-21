from django.db.models import QuerySet

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request

from typing import Optional

from .models import Book
from .serializers import (
    BookSerializer, 
)


class BookView(ViewSet):
    """Book View."""

    queryset: QuerySet[Book] = Book.objects.all()

    def list(self, request: Request, *args, **kwargs) -> Response:
        books = self.queryset.all()
        serializer: BookSerializer = \
        BookSerializer(
            books,
            many=True
        )
        return Response({
            "result" : serializer.data
        })

    def retrieve(self, request: Request, pk: str) -> Response:
        """GET Method. get some object."""

        book: Optional[Book] = None
        try:
            book = self.queryset.get(
                id=pk
            )
            serializer: BookSerializer = \
            BookSerializer(book)
            return Response({
                    'book': serializer.data
            })
        except Book.DoesNotExist:
            return Response({
                'message': 'error'
            })


