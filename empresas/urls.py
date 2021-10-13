from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import EmpresaAPIView, AdministratorAPIView

urlpatterns = [
    path('empresas/', EmpresaAPIView.as_view(), name='empresas'),
    path('administrators/', AdministratorAPIView.as_view(), name='administrators'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
