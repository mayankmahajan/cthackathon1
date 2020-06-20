from builtins import range
from enum import Enum


class RequestType(Enum):
    GET, \
    POST, \
    PUT, \
    DELETE, \
    HEAD = range(5)
