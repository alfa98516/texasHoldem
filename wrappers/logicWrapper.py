from models.user import *
from models.deck import *
from models.hand import *
from models.draw import *
from logic.userLogic import *
from logic.deckLogic import *

class LogicWrapper:
    def __init__(self) -> None:
        self.userLogic = UserLogic()
        self.deckLogic = DeckLogic()

    def loginLogic(self, userName: str, password: str) -> User:
        return self.userLogic.loginLogic(userName, password)
    
    def initializeGame(self, deck) -> list[Hand, Draw, Hand]:
        return self.deckLogic.initializeGame(deck)