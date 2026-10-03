from entidades import Usuario
from abc import ABC, abstractmethod
from ConexaoDB import ConexaoDB

import sqlite3
class IUsuarioDAO(ABC):
    def __init__(self)

    def incluir(self):
        pass
    
    def alterar(self):
        pass
    
    def excluir(self):
        pass
    
    def obter_por_id(self):
        pass
    
    def listar(self):
        pass

    
class UsuarioDAO(IUsuarioDAO):
    def __init__(self)
        self.conexao = ConexaoDB().obterConexao()
        

    def incluir(self, usuario:Usuario):
        sql = f'''insert into Usuario(
                nome,
                perfil,
                email,
                senha
                
        )
        values({usuario.nome}, {usuario.perfil}, {usuario.email}, {usuario.senha});
        '''
        self.conexao.executar_comando("insert", sql, self.conexao)
    
    def alterar(self, usuario:Usuario, alteracoes):
        sql = f'''
                update Usuario set{alteracoes}
                where id = {usuario.id};
        '''
        self.conexao.executar_comando("update", sql, self.conexao)
    
    def excluir(self, usuario:Usuario):
        sql = f''' delete from Usuario
                    where id = {usuario.id};
        
        '''
        self.conexao.executar_comando("delete", sql, self.conexao)
    
    def obter_por_id(self, usuario:Usuario):
        sql = f''' select * from Usuario
                    where id = {usuario.id};

        '''
        registro = self.conexao.executar_comando("select", sql, self.conexao)
        
        return Usuario(registro["id"], registro["nome"], registro["perfil"], registro["email"], registro["senha"])
    
    def listar(self):
        registros = self.conexao.executar_select("Usuario", self.conexao)
        
        usuarios = []
        for registro in registros:
            usuarios.append(Usuario(registro["id"], registro["nome"], registro["perfil"], registro["email"], registro["senha"]))

        return usuarios