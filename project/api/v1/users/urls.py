# users/urls.py

from django.urls import path
from dj_rest_auth.jwt_auth import get_refresh_view
from rest_framework_simplejwt.views import TokenVerifyView

from .views import UserView, UsersView

urlpatterns = [
    path('<int:pk>', UserView.as_view(), name='users'),
    path('', UsersView.as_view(), name='get-users'),
]
