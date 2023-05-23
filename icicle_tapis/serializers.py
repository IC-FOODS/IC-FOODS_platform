from rest_framework import serializers


class TapisLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
