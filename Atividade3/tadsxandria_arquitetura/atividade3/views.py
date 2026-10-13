from datetime import date

from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from entidades import Categoria, Perfil, Projeto, Usuario
from Factory.ServicosFactory import ServicosFactory

from .forms import CategoriaForm, ProjetoForm, UsuarioForm


def _servicos():
    factory = ServicosFactory()
    return (
        factory.obter_categoria_repository(),
        factory.obter_usuario_repository(),
        factory.obter_projeto_repository(),
    )


def _obter_ou_404(servico, identificador, nome):
    entidade = servico.obter_por_id(identificador)
    if entidade is None:
        raise Http404(f"{nome} não encontrado.")
    return entidade


def home(request):
    categorias, usuarios, projetos = _servicos()
    lista_projetos = projetos.listar()
    return render(
        request,
        "atividade3/home.html",
        {
            "total_categorias": len(categorias.listar()),
            "total_usuarios": len(usuarios.listar()),
            "total_projetos": len(lista_projetos),
            "projetos_recentes": lista_projetos[:5],
        },
    )


def categoria_lista(request):
    categorias, _, _ = _servicos()
    return render(request, "atividade3/crud/lista_categorias.html", {"categorias": categorias.listar()})


def categoria_detalhe(request, pk):
    categorias, _, _ = _servicos()
    categoria = _obter_ou_404(categorias, pk, "Categoria")
    return render(request, "atividade3/crud/detalhe_categoria.html", {"categoria": categoria})


def categoria_criar(request):
    categorias, _, _ = _servicos()
    form = CategoriaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        entidade = Categoria(form.cleaned_data["id"], form.cleaned_data["descricao"])
        try:
            categoria = categorias.incluir(entidade)
        except ValueError as erro:
            form.add_error(None, str(erro))
        else:
            messages.success(request, "Categoria cadastrada com sucesso.")
            return redirect("atividade3:categoria_detalhe", pk=categoria.id)
    return render(
        request,
        "atividade3/crud/formulario.html",
        {"form": form, "titulo": "Nova categoria", "voltar": "atividade3:categoria_lista"},
    )


def categoria_editar(request, pk):
    categorias, _, _ = _servicos()
    categoria = _obter_ou_404(categorias, pk, "Categoria")
    form = CategoriaForm(
        request.POST or None,
        edicao=True,
        initial={"id": categoria.id, "descricao": categoria.descricao},
    )
    if request.method == "POST" and form.is_valid():
        categoria.descricao = form.cleaned_data["descricao"]
        try:
            categorias.alterar(categoria)
        except ValueError as erro:
            form.add_error(None, str(erro))
        else:
            messages.success(request, "Categoria atualizada com sucesso.")
            return redirect("atividade3:categoria_detalhe", pk=pk)
    return render(
        request,
        "atividade3/crud/formulario.html",
        {"form": form, "titulo": "Editar categoria", "voltar": "atividade3:categoria_detalhe", "pk": pk},
    )


def categoria_excluir(request, pk):
    categorias, _, _ = _servicos()
    categoria = _obter_ou_404(categorias, pk, "Categoria")
    if request.method == "POST":
        categorias.excluir(categoria)
        messages.success(request, "Categoria excluída com sucesso.")
        return redirect("atividade3:categoria_lista")
    return render(
        request,
        "atividade3/crud/confirmar_exclusao.html",
        {"objeto": categoria, "tipo": "a categoria", "voltar": "atividade3:categoria_detalhe", "pk": pk},
    )


def usuario_lista(request):
    _, usuarios, _ = _servicos()
    return render(request, "atividade3/crud/lista_usuarios.html", {"usuarios": usuarios.listar()})


def usuario_detalhe(request, pk):
    _, usuarios, _ = _servicos()
    usuario = _obter_ou_404(usuarios, pk, "Usuário")
    return render(request, "atividade3/crud/detalhe_usuario.html", {"usuario": usuario})


def usuario_criar(request):
    _, usuarios, _ = _servicos()
    form = UsuarioForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        entidade = Usuario(
            form.cleaned_data["id"],
            form.cleaned_data["nome"],
            Perfil[form.cleaned_data["perfil"]],
            form.cleaned_data["email"],
            form.cleaned_data["senha"],
        )
        try:
            usuario = usuarios.incluir(entidade)
        except ValueError as erro:
            form.add_error(None, str(erro))
        else:
            messages.success(request, "Usuário cadastrado com sucesso.")
            return redirect("atividade3:usuario_detalhe", pk=usuario.id)
    return render(
        request,
        "atividade3/crud/formulario.html",
        {"form": form, "titulo": "Novo usuário", "voltar": "atividade3:usuario_lista"},
    )


def usuario_editar(request, pk):
    _, usuarios, _ = _servicos()
    usuario = _obter_ou_404(usuarios, pk, "Usuário")
    form = UsuarioForm(
        request.POST or None,
        edicao=True,
        initial={
            "id": usuario.id,
            "nome": usuario.nome,
            "perfil": usuario.perfil.name,
            "email": usuario.email,
        },
    )
    if request.method == "POST" and form.is_valid():
        usuario.nome = form.cleaned_data["nome"]
        usuario.perfil = Perfil[form.cleaned_data["perfil"]]
        usuario.email = form.cleaned_data["email"]
        usuario.senha = form.cleaned_data["senha"]
        try:
            usuarios.alterar(usuario)
        except ValueError as erro:
            form.add_error(None, str(erro))
        else:
            messages.success(request, "Usuário atualizado com sucesso.")
            return redirect("atividade3:usuario_detalhe", pk=pk)
    return render(
        request,
        "atividade3/crud/formulario.html",
        {"form": form, "titulo": "Editar usuário", "voltar": "atividade3:usuario_detalhe", "pk": pk},
    )


def usuario_excluir(request, pk):
    _, usuarios, _ = _servicos()
    usuario = _obter_ou_404(usuarios, pk, "Usuário")
    if request.method == "POST":
        usuarios.excluir(usuario)
        messages.success(request, "Usuário excluído com sucesso.")
        return redirect("atividade3:usuario_lista")
    return render(
        request,
        "atividade3/crud/confirmar_exclusao.html",
        {"objeto": usuario, "tipo": "o usuário", "voltar": "atividade3:usuario_detalhe", "pk": pk},
    )


def projeto_lista(request):
    _, _, projetos = _servicos()
    return render(request, "atividade3/crud/lista_projetos.html", {"projetos": projetos.listar()})


def projeto_detalhe(request, pk):
    _, _, projetos = _servicos()
    projeto = _obter_ou_404(projetos, pk, "Projeto")
    return render(request, "atividade3/crud/detalhe_projeto.html", {"projeto": projeto})


def _projeto_do_form(form, data_criacao=None):
    categorias, usuarios, _ = _servicos()
    return Projeto(
        form.cleaned_data["id"],
        form.cleaned_data["descricao"],
        categorias.obter_por_id(int(form.cleaned_data["categoria_id"])),
        form.cleaned_data["resumo"],
        data_criacao or date.today(),
        usuarios.obter_por_id(int(form.cleaned_data["orientador_id"])),
    )


def projeto_criar(request):
    _, _, projetos = _servicos()
    form = ProjetoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        try:
            projeto = projetos.incluir(_projeto_do_form(form))
        except ValueError as erro:
            form.add_error(None, str(erro))
        else:
            messages.success(request, "Projeto cadastrado com sucesso.")
            return redirect("atividade3:projeto_detalhe", pk=projeto.id)
    return render(
        request,
        "atividade3/crud/formulario.html",
        {"form": form, "titulo": "Novo projeto", "voltar": "atividade3:projeto_lista"},
    )


def projeto_editar(request, pk):
    _, _, projetos = _servicos()
    projeto = _obter_ou_404(projetos, pk, "Projeto")
    form = ProjetoForm(
        request.POST or None,
        edicao=True,
        initial={
            "id": projeto.id,
            "descricao": projeto.descricao,
            "resumo": projeto.resumo,
            "categoria_id": projeto.categoria.id,
            "orientador_id": projeto.orientador.id,
        },
    )
    if request.method == "POST" and form.is_valid():
        try:
            projetos.alterar(_projeto_do_form(form, data_criacao=projeto.data_criacao))
        except ValueError as erro:
            form.add_error(None, str(erro))
        else:
            messages.success(request, "Projeto atualizado com sucesso.")
            return redirect("atividade3:projeto_detalhe", pk=pk)
    return render(
        request,
        "atividade3/crud/formulario.html",
        {"form": form, "titulo": "Editar projeto", "voltar": "atividade3:projeto_detalhe", "pk": pk},
    )


def projeto_excluir(request, pk):
    _, _, projetos = _servicos()
    projeto = _obter_ou_404(projetos, pk, "Projeto")
    if request.method == "POST":
        projetos.excluir(projeto)
        messages.success(request, "Projeto excluído com sucesso.")
        return redirect("atividade3:projeto_lista")
    return render(
        request,
        "atividade3/crud/confirmar_exclusao.html",
        {"objeto": projeto, "tipo": "o projeto", "voltar": "atividade3:projeto_detalhe", "pk": pk},
    )
