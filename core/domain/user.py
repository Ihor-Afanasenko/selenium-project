class User:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 company: str,
                 message: str,
                 email: str,
                 incorrect_email: str,
                 password: str,
                 ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.message = message
        self.email = email
        self.incorrect_email = incorrect_email
        self.password = password
