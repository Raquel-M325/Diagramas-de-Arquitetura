from entidades import Categoria
from DAO.CategoriaDAO import *

class CategoriaRepository:

    def __init__(self):
        self.dao = CategoriaDAO()   

    def validar(self, categoria):
        if categoria.id is None:
            raise ValueError("O ID da categoria é obrigatório.")  

        if not categoria.descricao:
            raise ValueError("A descrição da categoria é obrigatória.")  

    def incluir(self, categoria):
        self.validar(categoria)

        if self.dao.obter_por_id(categoria.id) is not None:
            raise ValueError("Já existe uma categoria com esse ID.")

        self.dao.incluir(categoria)

    def alterar(self, categoria, alteracoes):
        self.validar(categoria)

        if self.dao.obter_por_id(categoria.id) is None:
            raise ValueError("Categoria não encontrada.")

        self.dao.alterar(categoria, alteracoes)

    def excluir(self, categoria):
        if self.dao.obter_por_id(categoria.id) is None:
            raise ValueError("Categoria não encontrada.")

        self.dao.excluir(categoria)

    def obter_por_id(self, id):
        return self.dao.obter_por_id(id)