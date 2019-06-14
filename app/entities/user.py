class User:
    def __init__(self, username, password, id_: int = None):
        self.id_ = id_
        self.password = password
        self.username = username
