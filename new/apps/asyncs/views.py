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

from .tasks import check_region
from banks.models import Card
from .models import Station

import asyncio


class AsyncViewSet(ViewSet):
    """Test async."""

    queryset = Card.objects.all()
    @action(
        methods=['post'],
        detail=False,
        url_path='retry',
    )
    def start_async(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        async def main():
            tasks: list[asyncio.Task] = []
            for i in range(13, 23):
                task = asyncio.create_task(
                    check_region(title=request.data.get('region'))
                )
                tasks.append(task)
            asyncio.gather(*tasks)
        asyncio.run(main())        
        return Response("BAD", status=204)