from entidades import Categoria
from abc import ABC, abstractmethod

import sqllite
class ICategoriaDAO(ABC):
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

class CategoriaDAO(ICategoriaDAO):
    def __init__(self)
        self.conexao = ConexaoDB().obterConexao()
        

    def incluir(self, categoria:Categoria):
        sql = f'''insert into Categoria(
                descricao
        )
        values({categoria.descricao});
        '''
        self.conexao.executar_comando("insert", sql, self.conexao)
    
    def alterar(self, categoria:Categoria, alteracoes):
        sql = f'''
                update Categoria set{alteracoes}
                where id = {categoria.id};
        '''
        self.conexao.executar_comando("update", sql, self.conexao)
    
    def excluir(self, categoria:Categoria):
        sql = f''' delete from Categoria
                    where id = {categoria.id};
        
        '''
        self.conexao.executar_comando("delete", sql, self.conexao)
    
    def obter_por_id(self, categoria:Categoria):
        sql = f''' select * from Categoria
                    where id = {categoria.id};

        '''
        registro = self.conexao.executar_comando("select", sql, self.conexao)
        
        return Categoria(registro["id"], registro["descricao"])
    
    def listar(self):
        registros = self.conexao.executar_select("Categoria", self.conexao)
        
        categorias = []
        for registro in registros:
            categorias.append(Categoria(registro["id"], registro["descricao"]))

        return categorias