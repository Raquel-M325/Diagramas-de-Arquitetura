from abc import ABC, abstractmethod


class IProjetoDAO(ABC):

    @abstractmethod
    def incluir(self, projeto):
        pass
    
    @abstractmethod
    def alterar(self, projeto, alteracoes):
        pass
    
    @abstractmethod
    def excluir(self, projeto):
        pass
    
    @abstractmethod
    def obter_por_id(self, id):
        pass
    
    @abstractmethod
    def listar(self):
        pass
