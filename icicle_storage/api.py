from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from icicle_storage.models import JSONObject
from icicle_storage.serializers import JSONObjectSerializer


class JSONObjectListAPI(ListAPIView):
    """List for JSONObjects"""
    permission_classes = (AllowAny,)
    queryset = JSONObject.objects.all()
    serializer_class = JSONObjectSerializer


class JSONObjectCreateAPI(CreateAPIView):
    """API for creating JSONObjects"""
    permission_classes = (AllowAny,)
    queryset = JSONObject.objects.all()
    serializer_class = JSONObjectSerializer


class JSONObjectViewAPI(RetrieveAPIView):
    """API for getting a single Act"""
    permission_classes = (AllowAny,)
    serializer_class = JSONObjectSerializer
    queryset = JSONObject.objects.all()
    lookup_field = "uuid"
