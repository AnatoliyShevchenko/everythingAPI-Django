from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAdminUser
)

from django.db.models import QuerySet

from .models import Card
from .serializers import CardSerializer

from typing import Type


class CardView(ViewSet):
    """Card View."""

    queryset: QuerySet[Card] = Card.objects.select_related('user')
    permission_classes: tuple = (
        IsAdminUser,
    )

    def list(self, request: Request, *args, **kwargs) -> Response:
        cards = self.queryset.all()
        serializer: Type = \
        CardSerializer(
            cards,
            many=True
        )
        return Response(serializer.data)