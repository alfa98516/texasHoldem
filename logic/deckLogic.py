from models.hand import *
from models.deck import *
from models.card import *
from models.draw import *

class DeckLogic:
    def __init__(self):
        pass

    def initializeGame(self, deck: Deck) -> list[Hand, Draw, Hand]:
        deck.shuffle()
        return [Hand(deck.deck.pop(0), deck.deck.pop(0)), Draw(deck.deck.pop(0), deck.deck.pop(0), deck.deck.pop(0)), Hand(deck.deck.pop(0), deck.deck.pop(0))]