from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from icicle_tapis.auth import TapisAuthentication
from icicle_storage.models import JSONObject
from icicle_storage.serializers import JSONObjectSerializer, JSONObjectMinSerializer


class JSONObjectListAPI(ListAPIView):
    """List for JSONObjects"""
    permission_classes = (AllowAny,)
    queryset = JSONObject.objects.all()
    serializer_class = JSONObjectMinSerializer

    def get_queryset(self):
        """Show only a users own data sets"""
        user_objects = JSONObject.objects.filter(owner=self.request.user.email)
        return user_objects


class JSONObjectCreateAPI(CreateAPIView):
    """API for creating JSONObjects"""
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TapisAuthentication,)
    queryset = JSONObject.objects.all()
    serializer_class = JSONObjectSerializer


class JSONObjectViewAPI(RetrieveAPIView):
    """API for getting a single Act"""
    permission_classes = (AllowAny,)
    serializer_class = JSONObjectSerializer
    queryset = JSONObject.objects.all()
    lookup_field = "uuid"
