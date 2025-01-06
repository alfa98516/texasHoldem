from storage.userStorage import *

class StorageWrapper:
    def __init__(self):
        self.userStorage = UserStorage()

    def getAllUsers(self) -> list[User]:
        return self.userStorage.getAllUsers()