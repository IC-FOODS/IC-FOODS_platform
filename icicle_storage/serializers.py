from rest_framework import serializers

from icicle_storage.models import JSONObject


class JSONObjectSerializer(serializers.ModelSerializer):
    """JSONObject Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = JSONObject
        fields = ["uuid", "title", "owner", "json_data"]
        extra_kwargs = {"uuid": {"read_only": True}}
