from django.contrib.auth.models import AnonymousUser
from .models import User, UserToken
from django.utils import timezone


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if "HTTP_AUTHORIZATION" in request.META:
            token = request.META["HTTP_AUTHORIZATION"]
            try:
                found = UserToken.objects.get(token=token, expires__gt=timezone.now())
                request.user = found.user
            except UserToken.DoesNotExist:
                pass

        return self.get_response(request)
