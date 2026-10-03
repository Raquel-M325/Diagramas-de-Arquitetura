from entidades import Usuario
from DAO.ConexaoDB import ConexaoDB
from Interface.IUsuarioDAO import IUsuarioDAO

    
class UsuarioDAO(IUsuarioDAO):
    def __init__(self):
        self.db = ConexaoDB()
        self.conexao = self.db.obterConexao()
        

    def incluir(self, usuario:Usuario):
        sql = f'''insert into Usuario(
                nome,
                perfil,
                email,
                senha
                
        )
        values('{usuario.nome}', '{usuario.perfil}', '{usuario.email}', '{usuario.senha}');
        '''
        self.db.executar_comando("insert", sql, self.conexao)
    
    def alterar(self, usuario:Usuario, alteracoes):
        sql = f'''
                update Usuario set{alteracoes}
                where id = {usuario.id};
        '''
        self.db.executar_comando("update", sql, self.conexao)
    
    def excluir(self, usuario:Usuario):
        sql = f''' delete from Usuario
                    where id = {usuario.id};
        
        '''
        self.db.executar_comando("delete", sql, self.conexao)
    
    def obter_por_id(self, id):
        sql = f''' select * from Usuario
                    where id = {id};

        '''
        registro = self.db.executar_comando("select", sql, self.conexao)
        
        if not registro:
            return None
        return Usuario(registro[0]["id"], registro[0]["nome"], registro[0]["perfil"], registro[0]["email"], registro[0]["senha"])
    
    def listar(self):
        registros = self.db.executar_select("Usuario", self.conexao)
        
        usuarios = []
        for registro in registros:
            usuarios.append(Usuario(registro["id"], registro["nome"], registro["perfil"], registro["email"], registro["senha"]))

        return usuarios