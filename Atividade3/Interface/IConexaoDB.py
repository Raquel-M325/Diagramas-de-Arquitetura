from abc import ABC, abstractmethod


class IConexaoDB(ABC):

    @abstractmethod
    def obterConexao(self):
        pass

    @abstractmethod
    def executar_comando(self, tipo, acao, conexao):
        pass

    @abstractmethod
    def executar_select(self, tabela, conexao):
        pass
