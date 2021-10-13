from rest_framework import serializers

from .models import Empresa, Administrator


class AdministratorSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True},
            'senha': {'write_only': True}
        }
        model = Administrator
        fields = (
            'id',
            'empresa',
            'nome',
            'email',
            'usuario',
            'senha',
            'telefone',
            'criacao',
            'ativo'
        )


class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa
        fields = (
            'id',
            'razaosocial',
            'cnpj',
            'criacao',
            'ativo'
        )