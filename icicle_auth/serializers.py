from django.contrib.auth import authenticate
from rest_framework import serializers

from icicle_auth.models import ICICLEUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ICICLEUser
        fields = ('uuid', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ICICLEUser
        fields = ('uuid', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UmiUser.objects.create_user(
            validated_data['email'],
            validated_data['password'],
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Invalid Credentials')
