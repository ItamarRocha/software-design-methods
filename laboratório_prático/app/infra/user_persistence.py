from ..business.model.user import User

class UserPersistence:
    def __init__(self, path: str, encoding = "utf-8"):
        self.path = path
        self.encoding = encoding

    def save(self, users: dict):
        with open(self.path,"wb") as f:
            for login, user in users.items():
                f.write(login.encode(self.encoding))
                f.write("\t".encode(self.encoding))
                f.write(user.getPassword().encode(self.encoding))
                f.write("\n".encode(self.encoding))


    def load(self):
        users = {}

        with open(self.path, "rb") as f:
            for line in f:
                user_data = line.decode(self.encoding).split("\t")
                users[user_data[0]] = User(user_data[0], user_data[1][:-1])
        
        return users