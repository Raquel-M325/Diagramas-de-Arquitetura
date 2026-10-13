from Interface.IConexaoDB import IConexaoDB
from django.db import connections


class ConexaoDB_ORM(IConexaoDB):
    DB_ALIAS = 'default'

    def obter_conexao(self):
        return connections[self.DB_ALIAS]

    def obterConexao(self):
        return self.obter_conexao()

    def executar_comando(self, tipo, acao=None, conexao=None):
        sql = acao if acao is not None else tipo
        return (conexao or self.obter_conexao()).cursor().execute(sql)

    def executar_select(self, tabela, conexao=None):
        return (conexao or self.obter_conexao()).cursor().execute(
            f'SELECT * FROM "{tabela}"'
        ).fetchall()
