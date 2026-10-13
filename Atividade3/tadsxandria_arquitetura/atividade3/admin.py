from django.contrib import admin

from .models import CategoriaModel, ProjetoModel, UsuarioModel


admin.site.register(CategoriaModel)
admin.site.register(UsuarioModel)
admin.site.register(ProjetoModel)
