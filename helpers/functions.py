import json
from random import randint
from string import ascii_letters, digits

from django.http import HttpRequest, HttpResponse, JsonResponse


def is_ajax(request: HttpRequest) -> bool:
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def hash_string(length: int = 16) -> str:
    random_string = ''

    source_string = ascii_letters+digits
    size = len(source_string)-1

    while len(random_string) < length:
        random_string += source_string[randint(0, size)]

    return random_string


def response_data(data=None, status=200, message=None) -> HttpResponse:
    response = {
        "status": status,
        "message": message,
        "data": data
    }

    return JsonResponse(data=response, status=status)
