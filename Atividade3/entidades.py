from dataclasses import dataclass
from enum import Enum

class Perfil(Enum):
    comum = (1 , "Comum")
    orientador = (2, "Orientador")
    administrador = (3, "Administrador")

    def __init__(self, codigo, funcao):
        self.codigo = codigo
        self.funcao = funcao

@dataclass
class Categoria:
    id: int
    descricao: str
    
    def __str__(self):
        return self.descricao
    

@dataclass
class Usuario:
    id: int
    nome: str
    perfil: Perfil
    email: str
    senha: str
        

    def __str__(self):
        return f'{self.nome} - {self.perfil}'
    
@dataclass(init=False)
class Projeto:
    id: int
    descricao: str
    categoria: Categoria
    resumo: str
    data_criacao: object
    orientador: Usuario

    def __init__(self, id, descricao, categoria, resumo, data_publicacao, orientador:Usuario):
        self.id = id
        self.descricao = descricao
        self.data_criacao = data_publicacao
        self.resumo = resumo
        self.categoria = categoria
        self.orientador = orientador

    def __str__(self):
        return self.descricao
