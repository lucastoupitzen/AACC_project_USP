from django.contrib.auth.models import AbstractBaseUser
from .....src.domain.use_cases.user.autenticar_user import AutenticarUserInterface
from .....src.data.interfaces.user_repository import UserRepositoryInterface

class AutenticarUser(AutenticarUserInterface):

    def __init__(self, user_repository : UserRepositoryInterface) -> None:

        self.__user_repository = user_repository

    def autenticar(self, username: str, password: str) -> (AbstractBaseUser | None):
        
        response = self.__user_repository.authenticate_user(
            username= username,
            password= password
        )

        return response
