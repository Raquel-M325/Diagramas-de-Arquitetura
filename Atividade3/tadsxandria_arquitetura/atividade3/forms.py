from django import forms

from entidades import Perfil
from Factory.ServicosFactory import ServicosFactory


class FormularioBase(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            campo.widget.attrs.setdefault("class", "campo")

    def configurar_id(self, edicao):
        if edicao:
            self.fields["id"].disabled = True


class CategoriaForm(FormularioBase):
    id = forms.IntegerField(label="ID", min_value=1)
    descricao = forms.CharField(label="Descrição", max_length=255)

    def __init__(self, *args, edicao=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.configurar_id(edicao)


class UsuarioForm(FormularioBase):
    id = forms.IntegerField(label="ID", min_value=1)
    nome = forms.CharField(label="Nome", max_length=255)
    perfil = forms.ChoiceField(
        label="Perfil", choices=[(perfil.name, perfil.funcao) for perfil in Perfil]
    )
    email = forms.EmailField(label="E-mail", max_length=255)
    senha = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(render_value=False),
    )

    def __init__(self, *args, edicao=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.configurar_id(edicao)


class ProjetoForm(FormularioBase):
    id = forms.IntegerField(label="ID", min_value=1)
    descricao = forms.CharField(label="Descrição", max_length=255)
    resumo = forms.CharField(label="Resumo", widget=forms.Textarea(attrs={"rows": 5}))
    categoria_id = forms.ChoiceField(label="Categoria")
    orientador_id = forms.ChoiceField(label="Orientador")

    def __init__(self, *args, edicao=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.configurar_id(edicao)
        factory = ServicosFactory()
        categorias = factory.obter_categoria_repository().listar()
        orientadores = factory.obter_usuario_repository().listar_orientadores()
        self.fields["categoria_id"].choices = [
            (item.id, item.descricao) for item in categorias
        ] or [("", "Cadastre uma categoria primeiro")]
        self.fields["orientador_id"].choices = [
            (item.id, item.nome) for item in orientadores
        ] or [("", "Cadastre um orientador primeiro")]
