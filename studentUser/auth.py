import datetime
from django.utils.translation import ugettext_lazy
from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework.authtoken.models import Token
from rest_framework import HTTP_HEADER_ENCODING


def get_authorization_header(request):
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if isinstance(auth, type('')):
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth


