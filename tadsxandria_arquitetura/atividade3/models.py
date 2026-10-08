from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.contrib.auth.hashers import identify_hasher
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
# from enum import Enum

# class Perfil(Enum):
#     comum = (1 , "Comum")
#     orientador = (2, "Orientador")
#     administrador = (3, "Administrador")

#     def __init__(self, codigo, funcao):
#         codigo = codigo
#         funcao = funcao

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
    # senha = senha 
        
    class Meta:
        db_table = "usuarios"
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        try:
            identify_hasher(self.password)
        except Exception:
            self.set_password(self.password)
        super().save(*args, **kwargs)
    
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