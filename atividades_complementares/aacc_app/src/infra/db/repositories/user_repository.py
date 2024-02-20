from django.contrib.auth import authenticate
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
from .....src.data.interfaces.user_repository import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):

    @classmethod
    def authenticate_user(cls, username : str, password: str) -> (AbstractBaseUser | None):

        usuario = authenticate(username= username, password= password)

        return usuario

    @classmethod
    def register_user(cls, username: str, email: str, first_name: str, 
                last_name: str, password: str) -> None: 
        
        try: 

            user = User.objects.filter(username=username).first()

            if user: raise Exception("Usuário já cadastrado!")
            
            user = User.objects.create_user(username=username, email=email, password=password, 
                                            first_name=first_name, last_name=last_name)
            user.save()

        except:
            raise Exception("Erro ao registrar usuário")
