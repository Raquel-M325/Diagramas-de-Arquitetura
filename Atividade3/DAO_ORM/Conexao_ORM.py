from Interface.IConexaoDB import IConexaoDB
from django.db import connections


class ConexaoDB_ORM(IConexaoDB):
    DB_ALIAS = 'db_tadsxandria'

    def obter_conexao(self):
        if self.DB_ALIAS not in connections.databases:
            connections.databases[self.DB_ALIAS] = {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'db_tadsxandria.sqlite3',
                'ATOMIC_REQUESTS': False,
                'TIME_ZONE': 'America/Fortaleza',
                'CONN_HEALTH_CHECKS': True, 
                'CONN_MAX_AGE': 60,
                'AUTOCOMMIT': True,
                'OPTIONS': {},
            }

        return connections[self.DB_ALIAS]
    
    def executar_comando(self, acao, commit=False):
        sql = f'''{acao}'''
        conexao = self.obter_conexao()
        result = conexao.cursor().execute(sql)
        return result