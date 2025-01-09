from storage.userStorage import *

class StorageWrapper:
    def __init__(self):
        self.userStorage = UserStorage()

    def getAllUsers(self) -> list[User]:
        return self.userStorage.getAllUsers()
    
    def saveNewUserJson(self, users: list[User]) -> None:
        self.userStorage.saveNewUserJson(users)
