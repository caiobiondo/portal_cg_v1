from rest_framework import generics

from .models import Empresa, Administrator
from .serializers import AdministratorSerializer, EmpresaSerializer


class AdministratorsAPIView(generics.ListCreateAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer


class AdministratorAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer


class EmpresasAPIView(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class EmpresaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer