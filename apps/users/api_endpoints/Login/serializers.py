from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers


class LoginSerializer(TokenObtainPairSerializer):
    username_field = 'email'
