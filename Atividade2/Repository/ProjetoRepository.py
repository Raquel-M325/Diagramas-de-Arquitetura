from datetime import date

from entidades import Projeto
from DAO.ProjetoDAO import *
from entidades import Perfil

class ProjetoRepository:

    def __init__(self):
        self.dao = ProjetoDAO()   #

    def validar(self, projeto): 
        if projeto.id is None:
            raise ValueError("O ID da projeto é obrigatório.")  

        if not projeto.descricao:
            raise ValueError("A descrição da projeto é obrigatória.")  

        if not projeto.categoria:
            raise ValueError("A categoria da projeto é obrigatória.")

        if not projeto.resumo:
            raise ValueError("O resumo da projeto é obrigatória.")

        if not projeto.data_criacao:
            raise ValueError("A data de criação da projeto é obrigatória.")

        if not projeto.orientador:
            raise ValueError("O orientador da projeto é obrigatória.")

        if projeto.data_criacao > date.today():
            raise ValueError("A data de criação da projeto não pode ser futura.")

        if projeto.orientador.perfil != Perfil.orientador:
            raise ValueError("O orientador da projeto deve ter o perfil de orientador.")

        if projeto.data_criacao < date(1900, 1, 1): 
            raise ValueError("A data de criação da projeto não pode ser anterior a 01/01/1900.")

    
    def incluir(self, projeto):
        self.validar(projeto)

        if self.dao.obter_por_id(projeto.id) is not None:
            raise ValueError("Já existe uma projeto com esse ID.")

        self.dao.incluir(projeto)

    def alterar(self, projeto, alteracoes):
        self.validar(projeto)

        if self.dao.obter_por_id(projeto.id) is None:
            raise ValueError("projeto não encontrada.")

        self.dao.alterar(projeto, alteracoes)

    def excluir(self, projeto):
        if self.dao.obter_por_id(projeto.id) is None:
            raise ValueError("projeto não encontrada.")

        self.dao.excluir(projeto)

    def obter_por_id(self, id):
        return self.dao.obter_por_id(id)