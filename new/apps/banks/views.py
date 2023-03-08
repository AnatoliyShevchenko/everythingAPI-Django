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

from .models import (
    Card, 
    Terminal, 
    CardToCardTransaction, 
    CardToTerminalTransaction,
)
from .serializers import (
    CardSerializer, 
    SearchSerializer, 
    TerminalSerializer,
    CardToCardSerializer,
    CardToTerminalSerializer,
)

from typing import Type, Optional


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
    

class CardToCardView(ViewSet):
    """View for transaction card to card."""

    queryset: QuerySet = CardToCardTransaction.objects.all()

    def create(self, request: Request) -> Response:
        serializer: CardToCardSerializer = \
            CardToCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'transaction' : 'success'
            })
        return Response({
            'error' : serializer.errors
        })
    

class CardToTerminalView(ViewSet):
    """View for transaction card to terminal."""

    queryset: QuerySet = CardToTerminalTransaction.objects.all()

    def create(self, request: Request) -> Response:
        serializer: CardToTerminalSerializer = \
            CardToTerminalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'transaction' : 'success'
            })
        return Response({
            'error' : serializer.errors
        })
    

class TransactionView(ViewSet):
    """View for user's money."""

    queryset: QuerySet = CardToCardTransaction.objects.all()
    another_query: QuerySet = CardToTerminalTransaction.objects.all()

    def retrieve(self, request: Request, pk: str) -> Response:
        cash = self.queryset.filter(
                to_card_id=pk,
            )
        another_money = self.another_query.filter(
            terminal_id=pk,
        )
        sum = 0
        i: int
        for i in range(len(cash)):
            sum += cash[i].money
        j: int
        for j in range(len(another_money)):
            sum += another_money[j].money
        return Response({
            'money': sum,
        })