class Card:

    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit
    
    def __str__(self) -> str:
        return f"""        ┌─────────┐
        │{self.rank}       │
        │         │
        │         │
        │    {self.suit}    │
        │         │
        │         │
        │       {self.rank}│
        └─────────┘"""
    
    def getVal(self) -> list[int]:
        try:
            return int(self.rank)
        except ValueError:
            if self.rank == "A ":
                return 14
            if self.rank == "K ":
                return 13
            if self.rank == "Q ":
                return 12
            if self.rank == "J ":
                return 11
