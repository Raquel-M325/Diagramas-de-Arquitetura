from django.urls import path

from . import views

app_name = "atividade3"

urlpatterns = [
    path("", views.home, name="home"),
    path("categorias/", views.categoria_lista, name="categoria_lista"),
    path("categorias/nova/", views.categoria_criar, name="categoria_criar"),
    path("categorias/<int:pk>/", views.categoria_detalhe, name="categoria_detalhe"),
    path("categorias/<int:pk>/editar/", views.categoria_editar, name="categoria_editar"),
    path("categorias/<int:pk>/excluir/", views.categoria_excluir, name="categoria_excluir"),
    path("usuarios/", views.usuario_lista, name="usuario_lista"),
    path("usuarios/novo/", views.usuario_criar, name="usuario_criar"),
    path("usuarios/<int:pk>/", views.usuario_detalhe, name="usuario_detalhe"),
    path("usuarios/<int:pk>/editar/", views.usuario_editar, name="usuario_editar"),
    path("usuarios/<int:pk>/excluir/", views.usuario_excluir, name="usuario_excluir"),
    path("projetos/", views.projeto_lista, name="projeto_lista"),
    path("projetos/novo/", views.projeto_criar, name="projeto_criar"),
    path("projetos/<int:pk>/", views.projeto_detalhe, name="projeto_detalhe"),
    path("projetos/<int:pk>/editar/", views.projeto_editar, name="projeto_editar"),
    path("projetos/<int:pk>/excluir/", views.projeto_excluir, name="projeto_excluir"),
]
