class UserManager:
    def __init__(self):
        self.users = {}

    def addUser(self, email, password):
        if email in self.users:
            raise ValueError("User already exists")
        self.users[email] = password
        return "User added successfully"