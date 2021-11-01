from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import EmpresaAPIView, AdministratorAPIView, EmpresasAPIView, AdministratorsAPIView
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi
from django.conf.urls import url

schema_view = get_schema_view(
    openapi.Info(
        title="API Portal",
        default_version='v1',
        description="Este docs explica como usar os endpoints criados.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="gabriel.silva@cgcontadores.com.br"),
        license=openapi.License(name="CG Contadores"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('empresas/', EmpresasAPIView.as_view(), name='empresas'),
    path('administrators/', AdministratorsAPIView.as_view(), name='administrators'),
    path('empresas/<int:pk>/', EmpresaAPIView.as_view(), name='empresa'),
    path('administrators/<int:pk>/', AdministratorAPIView.as_view(), name='administrator'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]


urlpatterns += [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
