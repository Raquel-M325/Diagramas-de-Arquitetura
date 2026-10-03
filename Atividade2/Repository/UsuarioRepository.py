import regex

from entidades import Perfil, Usuario
import re
from DAO.UsuarioDAO import *

class UsuarioRepository:

    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    def __init__(self):
           self.dao = UsuarioDAO()   
   
    def validar(self, usuario):
        if usuario.id is None:
            raise ValueError("O ID da usuario é obrigatório.")  

        if not usuario.nome:  
            raise ValueError("O nome do usuario é obrigatória.")  

        if not usuario.perfil: 
            raise ValueError("O perfil do usuario é obrigatória.")

        if not usuario.email:
            raise ValueError("O email do usuario é obrigatória.")

        if not usuario.senha:
            raise ValueError("A senha do usuario é obrigatória.")

        if usuario.perfil not in [perfil for perfil in Perfil]:
            raise ValueError("O perfil do usuario é inválido.")

        if usuario.senha and len(usuario.senha) < 10:
            raise ValueError("A senha do usuario deve ter pelo menos 10 caracteres.")

        if usuario.email and not re.match(self.regex, usuario.email):
            raise ValueError("O email do usuario é inválido.")

        if usuario.email and self.dao.obter_por_email(usuario.email) is not None:
            raise ValueError("Já existe um usuario com esse email.")

        if usuario.senha and not re.search(r'[A-Z]', usuario.senha):
            raise ValueError("A senha do usuario deve conter pelo menos uma letra maiúscula.")

        if usuario.senha and not re.search(r'[a-z]', usuario.senha):
            raise ValueError("A senha do usuario deve conter pelo menos uma letra minúscula.")

        if usuario.senha and not re.search(r'\d', usuario.senha):
            raise ValueError("A senha do usuario deve conter pelo menos um número.")

        if usuario.senha and not re.search(r'[!@#$%^&*(),.?":{}|<>]', usuario.senha):
            raise ValueError("A senha do usuario deve conter pelo menos um caractere especial.")

        if usuario.senha and re.search(r'\s', usuario.senha):
            raise ValueError("A senha do usuario não deve conter espaços em branco.")

        if usuario.senha and re.search(r'(.)\1\1', usuario.senha):
            raise ValueError("A senha do usuario não deve conter três ou mais caracteres repetidos consecutivos.")

        if usuario and re.search(r'(012|123|234|345|456|567|678|789|890)', usuario.senha):
            raise ValueError("A senha do usuario não deve conter sequências numéricas.")

        if usuario and re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', usuario.senha, re.IGNORECASE):
            raise ValueError("A senha do usuario não deve conter sequências alfabéticas.")

        if usuario and re.search(r'(0123456789|9876543210|abcdefghijklmnopqrstuvwxyz|zyxwvutsrqponmlkjihgfedcba)', usuario.senha, re.IGNORECASE):
            raise ValueError("A senha do usuario não deve conter sequências numéricas ou alfabéticas completas.")

        if usuario and re.search(r'(.)\1{2,}', usuario.senha):
            raise ValueError("A senha do usuario não deve conter três ou mais caracteres repetidos consecutivos.")
        


    def incluir(self, usuario):
        self.validar(usuario)

        if self.dao.obter_por_id(usuario.id) is not None:
            raise ValueError("Já existe uma usuario com esse ID.")

        self.dao.incluir(usuario)

    def alterar(self, usuario, alteracoes):
        self.validar(usuario)

        if self.dao.obter_por_id(usuario.id) is None:
            raise ValueError("usuario não encontrada.")

        self.dao.alterar(usuario, alteracoes)

    def excluir(self, usuario):
        if self.dao.obter_por_id(usuario.id) is None:
            raise ValueError("usuario não encontrada.")

        self.dao.excluir(usuario)

    def obter_por_id(self, id):
        return self.dao.obter_por_id(id) 