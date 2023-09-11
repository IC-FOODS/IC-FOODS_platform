from rest_framework import serializers

from icicle_storage.models import JSONObject


class JSONObjectSerializer(serializers.ModelSerializer):
    """JSONObject Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = JSONObject
        fields = ["uuid", "title", "owner", "json_data"]
        extra_kwargs = {"uuid": {"read_only": True}}


class JSONObjectCreateSerializer(serializers.ModelSerializer):
    """JSONObject Create Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = JSONObject
        fields = ["uuid", "title", "owner", "json_data"]
        extra_kwargs = {"uuid": {"read_only": True}}

    def create(self, validated_data):
        """Lookup owner from Tapis identity and add to validated_data"""
        owner = self.context["owner"]
        validated_data["owner"] = owner
        return super(JSONObjectCreateSerializer, self).create(validated_data)


class JSONObjectMinSerializer(serializers.ModelSerializer):
    """JSONObject Minimalist Serializer"""

    class Meta(object):
        """Meta class for field info"""

        model = JSONObject
        fields = ["uuid", "title", "owner"]
        extra_kwargs = {"uuid": {"read_only": True}}
