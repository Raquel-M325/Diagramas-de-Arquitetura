from Atividade2.Interface import IConexaoDB
import sqlite3


class ConexaoDB(IConexaoDB):

    __singleton = None

    def __new__(cls):
        if cls.__singleton is None:

            cls.__singleton = super().__new__(cls)

            cls.__singleton.conexao = sqlite3.connect('db_atividade2.sqlite3')

            cls.__singleton.conexao.execute("PRAGMA foreign_keys = ON")

            cprint(f'\n **Conectou ao banco de dados!**\n', "white", "on_light_red", attrs=["bold"])

        return cls.__singleton

    def obterConexao(self):
        return self.__singleton.conexao

    def executar_comando(self, tipo, acao, conexao):

        sql = f'''{acao}'''
        if tipo == 'insert' or tipo == 'update' or tipo == 'delete':
            conexao.cursor().execute(sql)
            conexao.commit()
        elif tipo == 'select':
            registro = conexao.cursor().execute(sql).fetchall()
            return registro
        else:
            raise ValueError('Instrução inválida')

        return None




    def executar_select(self, tabela, conexao):

        sql = f'SELECT * FROM {tabela}'
        registros = conexao.cursor().execute(sql).fetchall()
        return registros