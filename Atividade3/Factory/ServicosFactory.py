from DAO_ORM.Conexao_ORM import ConexaoDB_ORM
from DAO_ORM.Categoria_ORM import CategoriaDAO

class ServicosFactory:

    def obter_conexao_db(self):
        return ConexaoDB_ORM()
    
    def obter_categoria_dao(self):
        return CategoriaDAO(conexao = self.obter_conexao_db())