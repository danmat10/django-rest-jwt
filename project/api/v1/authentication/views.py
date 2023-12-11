from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView
from rest_framework.permissions import IsAdminUser
from dj_rest_auth.views import (
    LoginView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordChangeView,
)
from drf_spectacular.utils import extend_schema

from .serializers import CustomLoginSerializer
from api.v1.users.models import CustomUser
from api.v1.users.serializers import CustomUserSerializer


@extend_schema(tags=['Authentication'], description="User Login")
class CustomLoginView(LoginView):
    serializer_class = CustomLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            user_data = CustomUserSerializer(user).data

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user_data,
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['Authentication'], description="User Token Verification")
class CustomTokenVerifyView(TokenVerifyView):
    pass


@extend_schema(tags=['Authentication'], description="User Token Refresh")
class CustomTokenRefreshView(TokenRefreshView):
    pass


@extend_schema(tags=['Authentication'], description="User Password Reset")
class CustomPasswordResetView(PasswordResetView):
    pass


@extend_schema(tags=['Authentication'], description="User Password Reset Confirmation")
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    pass


@extend_schema(tags=['Authentication'], description="User Password Change")
class CustomPasswordChangeView(PasswordChangeView):
    pass


@extend_schema(tags=['Authentication'], description="Operações de CRUD para Usuários")
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = []
