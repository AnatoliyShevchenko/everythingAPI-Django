from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAdminUser
)

from django.db.models import QuerySet

from .models import Card, Terminal, Transaction
from .serializers import (
    CardSerializer, 
    SearchSerializer, 
    TerminalSerializer,
    TransactionSerializer
)

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
    
    def create(self, request: Request) -> Response:
        serializer: SearchSerializer = \
            SearchSerializer(data=request.data)
        if serializer.is_valid():
            result = self.queryset.filter(
                number = serializer.data['number'],
                cvv = serializer.data['cvv'],
                date_expired = serializer.data['date_expired']
            )
            if result:
                count = result.count()
                return Response({
                    'data' : f'i found {count} cards'
                })
            return Response({
                'error' : 'not found'
            })
        return Response({
            'error' : serializer.errors
        })
    
    @action(
        methods=['GET'], 
        detail=False, 
        url_path='qwe',
        permission_classes = (AllowAny,)
        )
    def check_card(
            self, 
            request: Request, 
            *args, 
            **kwargs
        ) -> Response:
        return Response({
            'data' : 'ok'
        })
        

class TerminalView(ViewSet):
    """View for terminals."""

    queryset: QuerySet = Terminal.objects.all()

    def list(self, request: Request) -> Response:
        terminals = self.queryset.all()
        serializer: TerminalSerializer =\
            TerminalSerializer(terminals, many=True)
        return Response(serializer.data)
    
    @action(methods=["POST"], url_path='add', detail=False)
    def add_terminal(self, request: Request) -> Response:
        serializer: TerminalSerializer = \
            TerminalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'terminal' : 'added success'
            })
        return Response({
            'error' : serializer.errors
        })
    

class TransactionView(ViewSet):
    """View for Transaction."""

    queryset = Transaction.objects.all()

    def list(self, request: Request) -> Response:
        terminals = self.queryset.all()
        serializer: TransactionSerializer =\
            TransactionSerializer(terminals, many=True)
        return Response(serializer.data)
    
    @action(methods=["POST"], url_path='add', detail=False)
    def add_transaction(self, request: Request) -> Response:
        serializer: TransactionSerializer = \
            TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'transaction' : 'added success'
            })
        return Response({
            'error' : serializer.errors
        })
    