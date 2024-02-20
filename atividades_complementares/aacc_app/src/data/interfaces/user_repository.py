from abc import ABC, abstractmethod
from django.contrib.auth.models import AbstractBaseUser

class UserRepositoryInterface(ABC):

    @abstractmethod
    def authenticate_user(self, username : str, password: str) -> (AbstractBaseUser | None): pass

    @abstractmethod
    def register_user(self, username: str, email: str, first_name: str, 
                last_name: str, password: str) -> None: pass
    