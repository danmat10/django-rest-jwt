from django.urls import path

from .views import (
    CustomLoginView,
    CustomTokenVerifyView,
    CustomTokenRefreshView,
    CustomPasswordResetView,
    CustomPasswordResetConfirmView,
    CustomPasswordChangeView,
    RegisterView,
)

urlpatterns = [
    # Register
    path('register/', RegisterView.as_view(), name='register'),

    # Authentication
    path('login/', CustomLoginView.as_view(), name='token_obtain_pair'),

    # Token Management
    path('token-verify/', CustomTokenVerifyView.as_view(), name='token_verify'),
    path('token-refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),

    # Password Management
    path("password/reset/", CustomPasswordResetView.as_view(),
         name="rest_password_reset"),
    path("password/reset/confirm/<str:uidb64>/<str:token>/",
         CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password/change/", CustomPasswordChangeView.as_view(),
         name="rest_password_change"),
]
