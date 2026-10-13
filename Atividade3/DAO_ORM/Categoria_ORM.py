from entidades import Categoria
from DAO_ORM.Conexao_ORM import ConexaoDB_ORM
from Interface.ICategoriaDAO import ICategoriaDAO
from tadsxandria_arquitetura.atividade3.models import CategoriaModel
from django.forms.models import model_to_dict
from dataclasses import asdict

class CategoriaDAO(ICategoriaDAO):
    def __init__(self, conexao: ConexaoDB_ORM):
        self._conexao = conexao
        self._conexao.obter_conexao()
        

    def incluir(self, categoria: Categoria) -> Categoria:
        model_instance = CategoriaModel(**asdict(categoria))
        model_instance.save(using=self._conexao.DB_ALIAS)
        return Categoria(**model_to_dict)
    
    def alterar(self, categoria: Categoria) -> Categoria:
        return self.incluir(categoria)
    
    def excluir(self, id: int):
        model_instance = CategoriaModel(id=id)
        model_instance.delete(using=self._conexao.DB_ALIAS)
    
    def obter_por_id(self, id) -> Categoria:
        registro = CategoriaModel.objects.using(self._conexao.DB_ALIAS).get(id=id)
        return Categoria(**model_to_dict(registro))
    
    def listar(self) -> list[Categoria]:
        registros = CategoriaModel.objects.using(self._conexao.DB_ALIAS).all()
        dados = [Categoria(**model_to_dict(registro)) for registro in registros]
        return dados