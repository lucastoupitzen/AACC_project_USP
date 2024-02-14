class User():

    def __init__(self, username: str, email: str, first_name: str, 
                 last_name: str, staff_status: int) -> None:

        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.staff_status = staff_status
