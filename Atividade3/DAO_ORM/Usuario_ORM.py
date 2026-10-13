from dataclasses import asdict

from django.forms.models import model_to_dict

from atividade3.models import UsuarioModel
from entidades import Perfil, Usuario
from Interface.IUsuarioDAO import IUsuarioDAO

from DAO_ORM.Conexao_ORM import ConexaoDB_ORM


class UsuarioDAO(IUsuarioDAO):
    def __init__(self, conexao: ConexaoDB_ORM):
        self._conexao = conexao
        self._conexao.obter_conexao()

    @staticmethod
    def _converter_model_para_dominio(registro) -> Usuario:
        dados = model_to_dict(registro)
        dados["perfil"] = Perfil[dados["perfil"]]
        return Usuario(**dados)

    def incluir(self, usuario: Usuario) -> Usuario:
        dados = asdict(usuario)
        dados["perfil"] = usuario.perfil.name
        model_instance = UsuarioModel(**dados)
        model_instance.save(using=self._conexao.DB_ALIAS)
        return self._converter_model_para_dominio(model_instance)

    def alterar(self, usuario: Usuario, alteracoes=None) -> Usuario:
        return self.incluir(usuario)

    def excluir(self, usuario):
        identificador = usuario.id if hasattr(usuario, "id") else usuario
        UsuarioModel(id=identificador).delete(using=self._conexao.DB_ALIAS)

    def obter_por_id(self, id) -> Usuario | None:
        registro = UsuarioModel.objects.using(self._conexao.DB_ALIAS).filter(id=id).first()
        return self._converter_model_para_dominio(registro) if registro else None

    def obter_por_email(self, email) -> Usuario | None:
        registro = UsuarioModel.objects.using(self._conexao.DB_ALIAS).filter(
            email__iexact=email
        ).first()
        return self._converter_model_para_dominio(registro) if registro else None

    def listar(self) -> list[Usuario]:
        registros = UsuarioModel.objects.using(self._conexao.DB_ALIAS).all().order_by("nome")
        return [self._converter_model_para_dominio(registro) for registro in registros]

    def listar_orientadores(self) -> list[Usuario]:
        registros = UsuarioModel.objects.using(self._conexao.DB_ALIAS).filter(
            perfil=Perfil.orientador.name
        ).order_by("nome")
        return [self._converter_model_para_dominio(registro) for registro in registros]
