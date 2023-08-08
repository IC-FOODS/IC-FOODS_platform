from django.contrib.auth import login
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from icicle_auth.serializers import (
    LoginSerializer,
    RegisterSerializer,
    UserSerializer,
)


class SignUpAPI(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)
        return Response({
            "users": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token[1]
        })


class LoginAPI(KnoxLoginView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class ActiveUserAPI(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
