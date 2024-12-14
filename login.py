class Login:
    def __init__(self, id, password):
        self.id = id
        self.password = password

    def login(self):
        print(f"Login with {self.id} and {self.password}!!!")
