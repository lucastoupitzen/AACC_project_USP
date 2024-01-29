class AaccParaAvaliacao():

    def __init__(self, id_avaliador: str, id_aacc: str, status: int, comentarios: str) -> None:


        # STATUS_CHOICES = [
        #     (0, 'Aguardando'),
        #     (1, 'Deferida'),
        #     (2, 'Indeferida')
        # ]

        self.id_avaliador = id_avaliador
        self.id_aacc = id_aacc
        self.status = status
        self.comentarios = comentarios
