class Aacc():

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
