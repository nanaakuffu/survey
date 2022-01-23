from random import randint
from string import ascii_letters, digits


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def hash_string(self, length: int = 16) -> str:
    random_string = ''

    source_string = ascii_letters+digits
    size = len(source_string)-1

    while len(random_string) < length:
        random_string += source_string[randint(0, size)]

    return random_string
