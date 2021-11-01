from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Empresa, Administrator
from .serializers import EmpresaSerializer, AdministratorSerializer


class EmpresaAPIView(APIView):
    """
    API das empresas cadastradas
    """
    def get(self, request):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmpresaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AdministratorAPIView(APIView):
    """
    API de ADmins relacionados
    """
    def get(self, request):
        administrators = Administrator.objects.all()
        serializer = AdministratorSerializer(administrators, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdministratorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

