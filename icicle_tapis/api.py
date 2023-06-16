from django.conf import settings
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from tapipy.tapis import Tapis

from icicle_tapis.serializers import TapisLoginSerializer


class TapisLoginAPI(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TapisLoginSerializer

    def post(self, request, *args, **kwargs):

        username = request.data["username"]
        password = request.data["password"]

        t = Tapis(
            base_url= settings.TAPIS_API_BASE,
            username=username,
            password=password,
        )
        t.get_tokens()
        token_str = str(t.access_token).split("\n")[1]
        token = token_str.split("access_token:")[1].strip()

        return Response({
            "token": token
        })

class TapisUserInfoAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        if 'cookie' in request.COOKIES:
            value = request.COOKIES['cookie']
            response = HttpResponse('Works')
            return response
        else:
            response = HttpResponse('Does Not Works')
            response.set_cookie('cookie', 'MY COOKIE VALUE')
            return response
