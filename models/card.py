class Card:

    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit
    
    def __str__(self) -> str:
        if self.rank == "10":
            return f"""        ┌─────────┐
        │{self.rank}       │
        │         │
        │         │
        │    {self.suit}    │
        │         │
        │         │
        │       {self.rank}│
        └─────────┘"""

        return f"""        ┌─────────┐
        │{self.rank}        │
        │         │
        │         │
        │    {self.suit}    │
        │         │
        │         │
        │        {self.rank}│
        └─────────┘"""