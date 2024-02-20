from ....src.domain.interfaces.json_serializible import JsonSerializableInterface

class Aacc(JsonSerializableInterface):

    def __init__(self, id_aacc: str, aluno: str, doc, data_envio: str, status: int) -> None:

        # STATUS_CHOICES = [
        #     (0, 'Aguardando'),
        #     (1, 'Enviada'),
        #     (2, 'Avaliada'),
        #     (3, 'Confirmada'),
        # ]
        self.id_aacc = id_aacc
        self.aluno = aluno
        self.doc = doc
        self.data_envio = data_envio
        self.status = status

    def to_json(self):
        return {
            "id_aacc": self.id_aacc,
            "aluno": self.aluno,
            "doc": str(self.doc),
            "data_envio": self.data_envio,
            "status": self.status
        }
    
    def identificador(self) -> str:
        return str(self.id_aacc)
    