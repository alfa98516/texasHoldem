from json import *
from models.user import *

class UserStorage:
    def __init__(self) -> None:
        self.__userPath: str = "data/users.json"
        self.__users: list[dict] = load(open(self.__userPath, 'r', encoding="utf-8"))
    
    def getAllUsers(self) -> list[User]:
        return [User(x["userName"], x["password"], x["balance"], x["gameCount"], x["bluffCount"]) for x in self.__users]
    
    def saveNewUserJson(self, users: list[User]) -> None:
        userDictList: list[dict] = []

        for x in users:
            userDictList.append(dict(x.__dict__))
            
        with open(self.__userPath, "w", encoding="utf-8") as json:
            dump(userDictList, json, indent=4)