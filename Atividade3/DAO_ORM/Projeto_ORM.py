from entidades import Projeto
from DAO_ORM.Categoria_ORM import ConexaoDB_ORM
from tadsxandria_arquitetura.atividade3.models import ProjetoModel
from Interface.IProjetoDAO import IProjetoDAO
from dataclasses import asdict
from django.forms.models import model_to_dict

class ProjetoDAO(IProjetoDAO):
    def __init__(self, conexao: ConexaoDB_ORM):
        self._conexao = conexao
        self._conexao.obter_conexao()
        

    def incluir(self, projeto: Projeto) -> Projeto:
        proj_asdict = asdict(projeto)
        proj_asdict.pop('categoria')
        proj_asdict.pop('orientador')

        model_instance = ProjetoModel(**proj_asdict)
        model_instance.categoria = projeto.categoria.id
        model_instance.orientador = projeto.orientador.id
        model_instance.save(using=self._conexao.DB_ALIAS)
        
        return Projeto(**model_to_dict(model_instance))
    
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