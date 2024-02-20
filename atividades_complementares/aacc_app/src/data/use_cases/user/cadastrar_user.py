from .....src.domain.use_cases.user.cadastrar_user import CadastrarUserInterface
from .....src.data.interfaces.user_repository import UserRepositoryInterface

class CadastrarUser(CadastrarUserInterface):

    def __init__(self, user_repository : UserRepositoryInterface) -> None:

        self.__user_repository = user_repository

    def cadastrar(self, username: str, email: str, first_name: str, 
                  last_name: str, password: str) -> None:
        
        response = self.__user_repository.register_user(
            username= username,
            email= email,
            first_name= first_name,
            last_name= last_name,
            password= password
        )

        return response
