from entidades import Projeto
from DAO.ConexaoDB import ConexaoDB
from Interface.IProjetoDAO import IProjetoDAO



class ProjetoDAO(IProjetoDAO):
    def __init__(self):
        self.db = ConexaoDB()
        self.conexao = self.db.obterConexao()

    def incluir(self, projeto:Projeto):
        sql = f'''insert into Projeto(
                descricao,
                data_criacao,
                resumo,
                categoria_id,
                orientador_id
        )
        values('{projeto.descricao}', '{projeto.data_criacao}', '{projeto.resumo}', {projeto.categoria.id}, {projeto.orientador.id});
        '''
        self.db.executar_comando("insert", sql, self.conexao)
    
    def alterar(self, projeto:Projeto, alteracoes):
        sql = f'''
                update Projeto set{alteracoes}
                where id = {projeto.id};
        '''
        self.db.executar_comando("update", sql, self.conexao)
    
    def excluir(self, projeto:Projeto):
        sql = f''' delete from Projeto
                    where id = {projeto.id};
        
        '''
        self.db.executar_comando("delete", sql, self.conexao)
    
    def obter_por_id(self, id):
        sql = f''' select * from Projeto
                    where id = {id};

        '''
        registro = self.db.executar_comando("select", sql, self.conexao)
        
        if not registro:
            return None
        return Projeto(registro[0]["id"], registro[0]["descricao"], registro[0]["categoria_id"], registro[0]["resumo"], registro[0]["data_criacao"], registro[0]["orientador_id"])
    
    def listar(self):
        registros = self.db.executar_select("Projeto", self.conexao)
        
        projetos = []
        for registro in registros:
            projetos.append(Projeto(registro["id"], registro["descricao"], registro["categoria_id"], registro["resumo"], registro["data_criacao"], registro["orientador_id"]))

        return projetos