from typing import List
from src.data.interfaces.aacc_avaliacao_repository import AaccParaAvaliacaoRepositoryInterface
from src.domain.models.aacc import Aacc
from src.domain.models.aacc_para_avaliacao import AaccParaAvaliacao
from src.domain.models.user import User
from models import Aacc as AACC_db
from models import AaccParaAvaliacao as AaccParaAvaliacao_db

class AaccParaAvaliacaoRepository(AaccParaAvaliacaoRepositoryInterface):

    @classmethod
    def select_pendentes_avaliador(cls, id_avaliador: str) -> List[Aacc]:
        try:
            query = AaccParaAvaliacao_db.objects.get(id_avaliador=id_avaliador)
            response : List[Aacc] = []
            for dado in query:
                aacc_registrada = Aacc(
                    id_aacc = dado.id_aacc,
                    aluno = dado.aluno,
                    doc = dado.doc,
                    data_envio = dado.data_envio,
                    status = dado.status
                )
                response.append(aacc_registrada)
            return response
        except:
            raise Exception(f"Erro ao procurar Aacc's para avaliação do avaliador {id_avaliador}!")

    @classmethod
    def select_aacc_para_avaliacao(cls, id_aacc: str) -> AaccParaAvaliacao:
        try:
            query = AACC_db.objects.filter(id_aacc=id_aacc)[0]
            response = AaccParaAvaliacao (
                id_aacc = id_aacc,
                id_avaliador = query.id_avaliador,
                comentarios = query.comentarios,
                status = query.status
            )
            return response
        except Exception:
            raise Exception(f"Não foi possível encontrar a aacc_para_avaliação buscada {id_aacc}!")
    
    @classmethod
    def register_aacc_para_avaliacao(cls, id_aacc: str, id_avaliador: str) -> None:
        try:
            novo_registro = AaccParaAvaliacao_db.objects.create(
                id_avaliador=User.objects.get(username=id_avaliador),
                id_aacc=AACC_db.objects.get(id_aacc= id_aacc)
            )
            novo_registro.save()
        except:
            raise Exception(f"Erro ao registra Aacc {id_aacc} "
                            f"para avaliação do avaliador {id_avaliador}!")
        
    @classmethod
    def register_avaliacao(cls, id_aacc: str, comentarios: str, status: int) -> None:
        try:
            query = AACC_db.objects.get(id_aacc= id_aacc)
    
            aacc_para_avaliacao = AaccParaAvaliacao_db.objects.get(id_aacc=query)
            aacc_para_avaliacao.status = status
            aacc_para_avaliacao.comentarios = comentarios
            aacc_para_avaliacao.save()
        except:
            raise Exception(f"Erro ao registra avaliação da AACC {id_aacc}!")
        