from rest_framework import status, generics
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAdminUser

from .models import CustomUser
from .serializers import CustomUserSerializer
from .permissions import IsAdminOrSelf


@extend_schema(tags=['Usuários'], description="Operações de CRUD para Usuários")
class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminOrSelf]

    # No need to override get, put, patch, and delete methods
    # DRF handles them by default using the provided serializer_class and queryset

    # However, you can still override them if you have specific customizations


@extend_schema(tags=['Usuários'], description="Operações de CRUD para Usuários")
class UsersView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]

    # No need to override the get method, DRF handles it by default
