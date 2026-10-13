from dataclasses import asdict
from datetime import date, datetime, time

from atividade3.models import ProjetoModel
from django.utils import timezone
from entidades import Categoria, Perfil, Projeto, Usuario
from Interface.IProjetoDAO import IProjetoDAO

from DAO_ORM.Conexao_ORM import ConexaoDB_ORM


class ProjetoDAO(IProjetoDAO):
    def __init__(self, conexao: ConexaoDB_ORM):
        self._conexao = conexao
        self._conexao.obter_conexao()

    @staticmethod
    def _converter_model_para_dominio(registro) -> Projeto:
        categoria = Categoria(registro.categoria_id, registro.categoria.descricao)
        orientador = Usuario(
            registro.orientador_id,
            registro.orientador.nome,
            Perfil[registro.orientador.perfil],
            registro.orientador.email,
            registro.orientador.senha,
        )
        return Projeto(
            registro.id,
            registro.descricao,
            categoria,
            registro.resumo,
            registro.data_criacao.date(),
            orientador,
        )

    def incluir(self, projeto: Projeto) -> Projeto:
        dados = asdict(projeto)
        dados.pop("categoria")
        dados.pop("orientador")
        if isinstance(dados["data_criacao"], date) and not isinstance(
            dados["data_criacao"], datetime
        ):
            dados["data_criacao"] = timezone.make_aware(
                datetime.combine(dados["data_criacao"], time.min)
            )
        dados["titulo"] = projeto.descricao
        model_instance = ProjetoModel(**dados)
        model_instance.categoria_id = projeto.categoria.id
        model_instance.orientador_id = projeto.orientador.id
        model_instance.save(using=self._conexao.DB_ALIAS)
        return self.obter_por_id(model_instance.id)

    def alterar(self, projeto: Projeto, alteracoes=None) -> Projeto:
        return self.incluir(projeto)

    def excluir(self, projeto):
        identificador = projeto.id if hasattr(projeto, "id") else projeto
        ProjetoModel(id=identificador).delete(using=self._conexao.DB_ALIAS)

    def obter_por_id(self, id) -> Projeto | None:
        registro = ProjetoModel.objects.using(self._conexao.DB_ALIAS).select_related(
            "categoria", "orientador"
        ).filter(id=id).first()
        return self._converter_model_para_dominio(registro) if registro else None

    def listar(self) -> list[Projeto]:
        registros = ProjetoModel.objects.using(self._conexao.DB_ALIAS).select_related(
            "categoria", "orientador"
        ).all().order_by("descricao")
        return [self._converter_model_para_dominio(registro) for registro in registros]
