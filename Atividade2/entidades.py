from enum import Enum

class Perfil(Enum):
    comum = (1 , "Comum")
    orientador = (2, "Orientador")
    administrador = (3, "Administrador")

    def __init__(self, codigo, funcao):
        self.codigo = codigo
        self.funcao = funcao

class Categoria:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao
    
    def __str__(self):
        return self.descricao
    
# amamsabjsbasba  perfil = Perfil().funcao

class Usuario:
    def __init__(self, id, nome, perfil:Perfil):
        self.id = id
        self.nome = nome
        self.perfil = perfil
    
    def __str__(self):
        return f'{self.nome} - {self.perfil}'
    
class Projeto:
    def __init__(self, id, descricao, categoria, resumo, data_publicacao, orientador:Usuario):
        self.id = id
        self.descricao = descricao
        self.data_criacao = data_publicacao
        self.resumo = resumo
        self.categoria = categoria
        self.orientador = orientador

    def __str__(self):
        return self.descricao
