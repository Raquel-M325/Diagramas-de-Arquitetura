from entidades import Categoria
from DAO.ConexaoDB import ConexaoDB
from Interface.ICategoriaDAO import ICategoriaDAO


class CategoriaDAO(ICategoriaDAO):
    def __init__(self):
        self.db = ConexaoDB()
        self.conexao = self.db.obterConexao()
        

    def incluir(self, categoria:Categoria):
        sql = f'''insert into Categoria(
                descricao
        )
        values('{categoria.descricao}');
        '''
        self.db.executar_comando("insert", sql, self.conexao)
    
    def alterar(self, categoria:Categoria, alteracoes):
        sql = f'''
                update Categoria set{alteracoes}
                where id = {categoria.id};
        '''
        self.db.executar_comando("update", sql, self.conexao)
    
    def excluir(self, categoria:Categoria):
        sql = f''' delete from Categoria
                    where id = {categoria.id};
        
        '''
        self.db.executar_comando("delete", sql, self.conexao)
    
    def obter_por_id(self, id):
        sql = f''' select * from Categoria
                    where id = {id};

        '''
        registro = self.db.executar_comando("select", sql, self.conexao)
        
        if not registro:
            return None
        return Categoria(registro[0]["id"], registro[0]["descricao"])
    
    def listar(self):
        registros = self.db.executar_select("Categoria", self.conexao)
        
        categorias = []
        for registro in registros:
            categorias.append(Categoria(registro["id"], registro["descricao"]))

        return categorias