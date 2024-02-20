from abc import ABC, abstractmethod

class CadastrarUserInterface(ABC):

    @abstractmethod
    def cadastrar(self, 
                username: str, email: str, first_name: str, 
                last_name: str, password: str) -> None: pass
    