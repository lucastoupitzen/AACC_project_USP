from ....src.domain.interfaces.json_serializible import JsonSerializableInterface

class User(JsonSerializableInterface):

    def __init__(self, username: str, email: str, first_name: str, 
                 last_name: str, password: str) -> None:

        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def to_json(self):
        return {
            "username": self.username,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
    
    def identificador(self) -> str:
        return str(self.username)
    