from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)

    def create(self, validated_data):
        try:
            user = User.objects.create_user(**validated_data)
        except:
            raise serializers.ValidationError({'error': 'Usuario con este username ya existe'})
        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)