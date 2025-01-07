from tui.clear import *
from wrappers.logicWrapper import *
from models.deck import *
from models.card import *
from models.hand import *
from models.draw import *
import time as t
class GameUI(Clear):
    def __init__(self):
        self.logicWrapper = LogicWrapper()

    def main(self, user):
        self.clear()
        print("You will be playing against an AI, since this is a completely offline TUI system")
        t.sleep(1)
        print("First you and the AI draw two cards")
        deck = Deck()
        gameCards: list[Hand, Draw, Hand] = self.logicWrapper.initializeGame(deck)
        self.clear(False, gameCards[0])
        
        input()
        
