import re

from DAO_ORM.Usuario_ORM import UsuarioDAO
from entidades import Perfil


class UsuarioRepository:
    regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    def __init__(self, dao: UsuarioDAO):
        self.dao = dao

    def validar(self, usuario):
        if usuario.id is None:
            raise ValueError("O ID do usuário é obrigatório.")
        if not usuario.nome:
            raise ValueError("O nome do usuário é obrigatório.")
        if usuario.perfil not in list(Perfil):
            raise ValueError("O perfil do usuário é inválido.")
        if not usuario.email or not re.match(self.regex, usuario.email):
            raise ValueError("O e-mail do usuário é inválido.")
        if not usuario.senha:
            raise ValueError("A senha do usuário é obrigatória.")

        existente = self.dao.obter_por_email(usuario.email)
        if existente is not None and existente.id != usuario.id:
            raise ValueError("Já existe um usuário com esse e-mail.")

    def incluir(self, usuario):
        self.validar(usuario)
        if self.dao.obter_por_id(usuario.id) is not None:
            raise ValueError("Já existe um usuário com esse ID.")
        return self.dao.incluir(usuario)

    def alterar(self, usuario, alteracoes=None):
        self.validar(usuario)
        if self.dao.obter_por_id(usuario.id) is None:
            raise ValueError("Usuário não encontrado.")
        return self.dao.alterar(usuario)

    def excluir(self, usuario):
        if self.dao.obter_por_id(usuario.id) is None:
            raise ValueError("Usuário não encontrado.")
        self.dao.excluir(usuario)

    def obter_por_id(self, id):
        return self.dao.obter_por_id(id)

    def listar(self):
        return self.dao.listar()

    def listar_orientadores(self):
        return self.dao.listar_orientadores()
