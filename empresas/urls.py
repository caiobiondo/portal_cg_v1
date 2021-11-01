from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import EmpresaAPIView, AdministratorAPIView, EmpresasAPIView, AdministratorsAPIView

urlpatterns = [
    path('empresas/', EmpresasAPIView.as_view(), name='empresas'),
    path('administrators/', AdministratorsAPIView.as_view(), name='administrators'),
    path('empresas/<int:pk>/', EmpresaAPIView.as_view(), name='empresa'),
    path('administrators/<int:pk>/', AdministratorAPIView.as_view(), name='administrator'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
