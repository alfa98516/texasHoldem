class Card:

    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit
    
    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"