import requests
import json

from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from tapipy.tapis import Tapis

from icicle_tapis.auth import TapisAuthentication
from icicle_tapis.serializers import TapisLoginSerializer
from icicle_tapis.utils import (
    is_logged_in,
    get_username,
    add_user_to_session,
    clear_session,
)


class TapisCallbackAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
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
            raise Exception(f"Error generating Tapis token; debug: {e}")

        return HttpResponse(token)


class TapisProtectedView(APIView):
    """Test class for Tapis Auth"""
    authentication_classes = (TapisAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """Verify that the JWT auth works"""
        return HttpResponse("Works!")
