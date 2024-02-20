from abc import ABC, abstractmethod
from django.contrib.auth.models import AbstractBaseUser

class AutenticarUserInterface(ABC):

    @abstractmethod
    def autenticar(self, username: str, password: str) -> (AbstractBaseUser | None): pass
    