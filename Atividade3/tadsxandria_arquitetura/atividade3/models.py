from django.db import models


PERFIL = [
    ("comum", "Comum"),
    ("orientador", "Orientador"),
    ("administrador", "Administrador"),
]


class CategoriaModel(models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.TextField(max_length=255, null=False, unique=True)

    class Meta:
        db_table = "categorias"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.descricao


class UsuarioModel(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255, null=False)
    perfil = models.CharField(max_length=20, choices=PERFIL, default="comum", null=False)
    email = models.EmailField(max_length=255, null=False, unique=True)
    senha = models.CharField(max_length=128, null=False)

    class Meta:
        db_table = "usuarios"
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


    def __str__(self):
        return self.email


class ProjetoModel(models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.TextField(max_length=255, null=False)
    data_criacao = models.DateTimeField(null=False, auto_now_add=True)
    resumo = models.TextField(max_length=255, null=False)
    categoria = models.ForeignKey(CategoriaModel, related_name="projetos", on_delete=models.CASCADE)
    orientador = models.ForeignKey(UsuarioModel, related_name="projetos", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)


    class Meta:
        db_table = "projetos"
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __str__(self):
        return self.titulo
