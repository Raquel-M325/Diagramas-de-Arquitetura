from dataclasses import asdict

from django.forms.models import model_to_dict

from atividade3.models import CategoriaModel
from entidades import Categoria
from Interface.ICategoriaDAO import ICategoriaDAO

from DAO_ORM.Conexao_ORM import ConexaoDB_ORM


class CategoriaDAO(ICategoriaDAO):
    def __init__(self, conexao: ConexaoDB_ORM):
        self._conexao = conexao
        self._conexao.obter_conexao()

    def incluir(self, categoria: Categoria) -> Categoria:
        model_instance = CategoriaModel(**asdict(categoria))
        model_instance.save(using=self._conexao.DB_ALIAS)
        return Categoria(**model_to_dict(model_instance))

    def alterar(self, categoria: Categoria, alteracoes=None) -> Categoria:
        return self.incluir(categoria)

    def excluir(self, categoria):
        identificador = categoria.id if hasattr(categoria, "id") else categoria
        CategoriaModel(id=identificador).delete(using=self._conexao.DB_ALIAS)

    def obter_por_id(self, id) -> Categoria | None:
        registro = CategoriaModel.objects.using(self._conexao.DB_ALIAS).filter(id=id).first()
        return Categoria(**model_to_dict(registro)) if registro else None

    def obter_por_descricao(self, descricao) -> Categoria | None:
        registro = CategoriaModel.objects.using(self._conexao.DB_ALIAS).filter(
            descricao__iexact=descricao
        ).first()
        return Categoria(**model_to_dict(registro)) if registro else None

    def listar(self) -> list[Categoria]:
        registros = CategoriaModel.objects.using(self._conexao.DB_ALIAS).all().order_by("descricao")
        return [Categoria(**model_to_dict(registro)) for registro in registros]
