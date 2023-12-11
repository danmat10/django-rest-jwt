# users/serializers.py

from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password


class CustomUserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    role = serializers.CharField(required=True)
    registration = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'name', 'password',
                  'role', 'registration', 'is_active', 'user_type')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            role=validated_data['role'],
            registration=validated_data['registration']
        )
        return user

    def validate_password(self, value):
        validate_password(value)
        return value
