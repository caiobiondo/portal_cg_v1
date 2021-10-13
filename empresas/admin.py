from django.contrib import admin

from .models import Empresa, Administrator


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('razaosocial', 'cnpj', 'criacao', 'atualizacao', 'ativo')


@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'nome', 'email', 'usuario', 'senha', 'telefone', 'criacao', 'atualizacao', 'ativo')
