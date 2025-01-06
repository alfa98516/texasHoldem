import random as r
from models.card import *

class Deck:
    SUITS: list[str] = ["♠", "♥", "♣", "♦"]
    RANKS: list[str] = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    
    def __init__(self) -> None:
        self.deck: list[Card] = [Card(suit, ranks) for suit in Deck.SUITS for ranks in Deck.RANKS]

    def __str__(self) -> str:
        strDeck: list[str] = [str(x) for x in self.deck]
        deckStr: str = ""
        for i in strDeck:
            deckStr += f" {i}"
        return deckStr.strip()