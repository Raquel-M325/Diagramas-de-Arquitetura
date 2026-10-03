from abc import ABC, abstractmethod


class ICategoriaDAO(ABC):

    @abstractmethod
    def incluir(self, categoria):
        pass
    
    @abstractmethod
    def alterar(self, categoria, alteracoes):
        pass
    
    @abstractmethod
    def excluir(self, categoria):
        pass
    
    @abstractmethod
    def obter_por_id(self, id):
        pass
    
    @abstractmethod
    def listar(self):
        pass
