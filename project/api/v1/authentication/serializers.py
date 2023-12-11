from rest_framework import serializers
from django.contrib.auth import authenticate

from api.v1.users.serializers import CustomUserSerializer


class CustomLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(email=attrs.get('email'),
                            password=attrs.get('password'))
        if not user:
            raise serializers.ValidationError('Incorrect credentials')

        return {'user': user}
