from models.user import *
from logic.userLogic import *

class LogicWrapper:
    def __init__(self) -> None:
        self.userLogic = UserLogic()

    def loginLogic(self, userName: str, password: str) -> User:
        return self.userLogic.loginLogic(userName, password)