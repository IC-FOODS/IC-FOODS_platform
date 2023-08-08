import jwt
from rest_framework import exceptions
from rest_framework.authentication import (
    BaseAuthentication, get_authorization_header,
)

from icicle_auth.models import ICICLEUser


class TapisAuthentication(BaseAuthentication):
    """Auth class that uses Tapis JWTs"""

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth:
            return None
        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = ('Invalid token header. '
                    'Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        token = auth[1]
        token_payload = jwt.decode(
            token,
            options={"verify_signature": False},
            algorithms=['HS256']
        )
        user_name = token_payload['tapis/username']
        # User = get_user_model()
        user, _ = ICICLEUser.objects.get_or_create(email=user_name)
        return (user, token)
