from django.urls import path, include

urlpatterns = [
    path('users/', include('api.v1.users.urls')),
    path('auth/', include('api.v1.authentication.urls')),
]
