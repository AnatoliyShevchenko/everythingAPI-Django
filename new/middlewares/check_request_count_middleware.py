from typing import Any
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse


class CountMiddleware:


    def __init__(self, get_response) -> None:
        self.get_response = get_response


    def __call__(self, request: WSGIRequest, 
                *args: tuple, **kwds: dict) -> Any:
        print("CUSTOM MIDDLEWARE IS WORK.")
        response = self.get_response(request)
        if request.user.is_anonymous:
            return HttpResponse('PLZ AUTH PLZ MAN PLZ')
        return response