from json import *
from models.user import *

class UserStorage:
    def __init__(self) -> None:
        self.__userPath: str = "data/users.json"
        self.__users: list[dict] = load(open(self.__userPath, 'r', encoding="utf-8"))
    
    def getAllUsers(self) -> list[User]:
        return [User(x["userName"], x["password"], x["balance"]) for x in self.__users]