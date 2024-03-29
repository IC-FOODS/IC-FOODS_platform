import requests
import json

from django.conf import settings
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from icicle_tapis.auth import TapisAuthentication


class TapisCallbackAPI(APIView):
    """
    Login callback API

    Receives a one-time code from the post-login callback URL
    and exchanges it for a JWT token.
    """
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        """HTTP GET method"""
        try:
            code = request.GET.get('code')
        except:
            code = None
        if not code:
            raise Exception(f"Error: No code in request")
        url = f"{settings.TAPIS_API_BASE}/v3/oauth2/tokens"
        data = {
            "code": code,
            "redirect_uri": "https://icfoods.o18s.com/api/tapis/callback",
            "grant_type": "authorization_code",
        }
        try:
            response = requests.post(
                url,
                data=data,
                auth=(
                    settings.TAPIS_CLIENT_ID,
                    settings.TAPIS_CLIENT_KEY,
                ),
            )
            response.raise_for_status()
            json_resp = response.json()
            token = json_resp['result']['access_token']['access_token']
        except Exception as e:
            raise Exception(f"Error generating Tapis token: {e}")

        return HttpResponse(token)


class TapisProtectedView(APIView):
    """Test class for Tapis Auth"""
    authentication_classes = (TapisAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """Verify that the JWT auth works"""
        return HttpResponse("Works!")
