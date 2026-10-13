from DAO_ORM.Categoria_ORM import CategoriaDAO
from DAO_ORM.Conexao_ORM import ConexaoDB_ORM
from DAO_ORM.Projeto_ORM import ProjetoDAO
from DAO_ORM.Usuario_ORM import UsuarioDAO
from Repository.CategoriaRepository import CategoriaRepository
from Repository.ProjetoRepository import ProjetoRepository
from Repository.UsuarioRepository import UsuarioRepository


class ServicosFactory:
    def obter_conexao_db(self):
        return ConexaoDB_ORM()

    def obter_categoria_dao(self):
        return CategoriaDAO(self.obter_conexao_db())

    def obter_usuario_dao(self):
        return UsuarioDAO(self.obter_conexao_db())

    def obter_projeto_dao(self):
        return ProjetoDAO(self.obter_conexao_db())

    def obter_categoria_repository(self):
        return CategoriaRepository(self.obter_categoria_dao())

    def obter_usuario_repository(self):
        return UsuarioRepository(self.obter_usuario_dao())

    def obter_projeto_repository(self):
        return ProjetoRepository(self.obter_projeto_dao())
