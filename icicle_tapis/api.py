import requests
import json

from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from tapipy.tapis import Tapis


from icicle_tapis.serializers import TapisLoginSerializer
from icicle_tapis.utils import (
    is_logged_in,
    get_username,
    add_user_to_session,
    clear_session,
)

class TapisLoginAPI(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TapisLoginSerializer

    def post(self, request, *args, **kwargs):

        username = request.data["username"]
        password = request.data["password"]

        t=Tapis(
            base_url=settings.TAPIS_API_BASE,
            username=username,
            password=password,
        )
        t.get_tokens()
        token_str = str(t.access_token).split("\n")[1]
        token = token_str.split("access_token:")[1].strip()

        return Response({
            "token": token
        })


class TapisCallbackAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):lu4chei4
    
        try:
            code = request._data.get('code')
        if not code:
            raise Exception(f"Error: No code in request; debug: {request.args}")
        url = f"{settings.TAPIS_API_BASE}/v3/oauth2/tokens"
        data = {
            "code": code,
            "redirect_uri": "https://73f3-50-239-66-226.ngrok-free.app/api/tapis/callback",
            "grant_type": "authorization_code",
        }
        try:
            response = requests.post(url, data=data, auth=(config['client_id'], config['client_key']))
            response.raise_for_status()
            json_resp = response.json()
            token = json_resp['result']['access_token']['access_token']
        except Exception as e:
            raise Exception(f"Error generating Tapis token; debug: {e}")

        username = get_username(token)
        roles = add_user_to_session(username, token)
        return HttpResponse('OK')

class TapisUserInfoAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):

        if 'cookie' in request.COOKIES:
            value = request.COOKIES['cookie']
            response = HttpResponse('Works')
        else:
            response = HttpResponse('Does Not Works')
            response.set_cookie('cookie', 'MY COOKIE VALUE')

        import pdb; pdb.set_trace()
        return response
