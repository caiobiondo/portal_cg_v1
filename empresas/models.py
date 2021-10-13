from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Empresa(Base):
    razaosocial = models.CharField(max_length=255)
    cnpj = models.DecimalField(max_digits=14, decimal_places=0, unique=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.razaosocial


class Administrator(Base):
    empresa = models.ForeignKey(Empresa, related_name='administrator', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    usuario = models.CharField(max_length=255)
    senha = models.CharField(max_length=255, default="")
    telefone = models.CharField(max_length=11, default="")

    class Meta:
        verbose_name = 'Administrator'
        verbose_name_plural = 'Administrators'
        unique_together = ['usuario', 'empresa']

    def __str__(self):
        return f'{self.nome} registrado na empresa {self.empresa} com user {self.usuario}'
