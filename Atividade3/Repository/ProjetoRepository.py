from datetime import date

from DAO_ORM.Projeto_ORM import ProjetoDAO
from entidades import Perfil


class ProjetoRepository:
    def __init__(self, dao: ProjetoDAO):
        self.dao = dao

    def validar(self, projeto):
        if projeto.id is None:
            raise ValueError("O ID do projeto é obrigatório.")
        if not projeto.descricao:
            raise ValueError("A descrição do projeto é obrigatória.")
        if not projeto.categoria:
            raise ValueError("A categoria do projeto é obrigatória.")
        if not projeto.resumo:
            raise ValueError("O resumo do projeto é obrigatório.")
        if not projeto.data_criacao:
            raise ValueError("A data de criação do projeto é obrigatória.")
        if not projeto.orientador:
            raise ValueError("O orientador do projeto é obrigatório.")
        if projeto.data_criacao > date.today():
            raise ValueError("A data de criação do projeto não pode ser futura.")
        if projeto.orientador.perfil != Perfil.orientador:
            raise ValueError("O orientador do projeto deve ter o perfil de orientador.")
        if projeto.data_criacao < date(1900, 1, 1):
            raise ValueError("A data de criação do projeto não pode ser anterior a 01/01/1900.")

    def incluir(self, projeto):
        self.validar(projeto)
        if self.dao.obter_por_id(projeto.id) is not None:
            raise ValueError("Já existe um projeto com esse ID.")
        return self.dao.incluir(projeto)

    def alterar(self, projeto, alteracoes=None):
        self.validar(projeto)
        if self.dao.obter_por_id(projeto.id) is None:
            raise ValueError("Projeto não encontrado.")
        return self.dao.alterar(projeto)

    def excluir(self, projeto):
        if self.dao.obter_por_id(projeto.id) is None:
            raise ValueError("Projeto não encontrado.")
        self.dao.excluir(projeto)

    def obter_por_id(self, id):
        return self.dao.obter_por_id(id)

    def listar(self):
        return self.dao.listar()
