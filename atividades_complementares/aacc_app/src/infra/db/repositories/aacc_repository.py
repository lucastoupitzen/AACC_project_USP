from typing import List
from src.data.interfaces.aacc_repository import AaccRepositoryInterface
from src.domain.models.aacc import Aacc
from .....models import Aacc as AACC_db

class AaccRepository(AaccRepositoryInterface):

    @classmethod
    def select_aacc_by_id(cls, id_aacc: str) -> Aacc: 
        try:
            query = AACC_db.objects.filter(id_aacc=id_aacc)[0]
            response = Aacc (
                id_aacc = id_aacc,
                aluno = query.aluno,
                doc = query.doc,
                data_envio = query.data_envio,
                status = query.status
            )
            return response
        except Exception:
            raise Exception(f"Não foi possível encontrar a aacc buscada {id_aacc}!")
        
    @classmethod
    def select_aacc_by_status(cls, status: int) -> List[Aacc]:
        try:
            query = AACC_db.objects.filter(status=0)
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
            raise Exception(f"Erro ao buscar por AACC'S com status {status}!")
        
    @classmethod
    def update_status_aacc(cls, id_aacc: str, status: int) -> None:
        try: 
            query = AACC_db.objects.get(id_aacc=id_aacc)
            query.status = status
            query.save()
        except:
            raise Exception(f"Erro ao atualizar status da AACC {id_aacc}!")
