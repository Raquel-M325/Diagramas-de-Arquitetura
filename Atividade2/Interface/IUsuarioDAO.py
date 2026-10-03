from abc import ABC, abstractmethod


class IUsuarioDAO(ABC):

    @abstractmethod
    def incluir(self, usuario):
        pass
    
    @abstractmethod
    def alterar(self, usuario, alteracoes):
        pass
    
    @abstractmethod
    def excluir(self, usuario):
        pass
    
    @abstractmethod
    def obter_por_id(self, id):
        pass
    
    @abstractmethod
    def listar(self):
        pass
