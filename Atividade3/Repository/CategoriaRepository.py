from DAO_ORM.Categoria_ORM import CategoriaDAO


class CategoriaRepository:
    def __init__(self, dao: CategoriaDAO):
        self.dao = dao

    def validar(self, categoria):
        if categoria.id is None:
            raise ValueError("O ID da categoria é obrigatório.")
        if not categoria.descricao:
            raise ValueError("A descrição da categoria é obrigatória.")

    def incluir(self, categoria):
        self.validar(categoria)
        if self.dao.obter_por_id(categoria.id) is not None:
            raise ValueError("Já existe uma categoria com esse ID.")
        return self.dao.incluir(categoria)

    def alterar(self, categoria, alteracoes=None):
        self.validar(categoria)
        if self.dao.obter_por_id(categoria.id) is None:
            raise ValueError("Categoria não encontrada.")
        return self.dao.alterar(categoria)

    def excluir(self, categoria):
        if self.dao.obter_por_id(categoria.id) is None:
            raise ValueError("Categoria não encontrada.")
        self.dao.excluir(categoria)

    def obter_por_id(self, id):
        return self.dao.obter_por_id(id)

    def listar(self):
        return self.dao.listar()
