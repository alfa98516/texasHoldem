from models.user import *
from wrappers.storageWrapper import *

class UserLogic:
    def __init__(self) -> None:
        self.storageWrapper = StorageWrapper()

    def loginLogic(self, username: str, password: str) -> User:
        users: list[User] = self.storageWrapper.getAllUsers()

        for x in users:
            if x.userName == username and x.password == password:
                return x
        return

        