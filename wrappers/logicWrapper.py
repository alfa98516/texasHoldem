from models.user import *
from models.deck import *
from models.hand import *
from models.draw import *
from logic.userLogic import *
from logic.deckLogic import *
from logic.AIlogic import *

class LogicWrapper:
    def __init__(self) -> None:
        self.userLogic = UserLogic()
        self.deckLogic = DeckLogic()
        self.AIlogic = AIlogic()

    def loginLogic(self, userName: str, password: str) -> User:
        return self.userLogic.loginLogic(userName, password)
    
    def initializeGame(self, deck) -> list[Hand, Draw, Hand]:
        return self.deckLogic.initializeGame(deck)
    
    def AIbetLogic(self, hand: Hand, playerBet: int, minmum: int, user: User, draw: Draw = None) -> int:
        return self.AIlogic.AIbetLogic(hand, playerBet, minmum, user, draw)
    
    def bluffCheck(self, hand: Hand, bet: int, minimum: int, user: User, draw: Draw = None) -> bool:
        return self.userLogic.bluffCheck(hand, bet, minimum, user, draw)