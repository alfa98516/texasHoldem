from models.card import *

class Draw:
    def __init__(self, card1: Card, card2: Card, card3: Card):
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.card4 = None
        self.card5 = None
    
    def __str__(self) -> str:
        if self.card4:
            if self.card5:
                return f"""┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│{self.card1.rank}       ││{self.card2.rank}       ││{self.card3.rank}       ││{self.card4.rank}       ││{self.card5.rank}       │
│         ││         ││         ││         ││         │
│         ││         ││         ││         ││         │
│    {self.card1.suit}    ││    {self.card2.suit}    ││    {self.card3.suit}    ││    {self.card4.suit}    ││    {self.card5.suit}    │
│         ││         ││         ││         ││         │
│         ││         ││         ││         ││         │
│       {self.card1.rank}││       {self.card2.rank}││       {self.card3.rank}││       {self.card4.rank}││       {self.card5.rank}│
└─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
"""
            return f"""┌─────────┐┌─────────┐┌─────────┐┌─────────┐
│{self.card1.rank}       ││{self.card2.rank}       ││{self.card3.rank}       ││{self.card4.rank}       │
│         ││         ││         ││         │
│         ││         ││         ││         │
│    {self.card1.suit}    ││    {self.card2.suit}    ││    {self.card3.suit}    ││    {self.card4.suit}    │
│         ││         ││         ││         │
│         ││         ││         ││         │
│       {self.card1.rank}││       {self.card2.rank}││       {self.card3.rank}││       {self.card4.rank}│
└─────────┘└─────────┘└─────────┘└─────────┘
"""
        return f"""┌─────────┐┌─────────┐┌─────────┐
│{self.card1.rank}       ││{self.card2.rank}       ││{self.card3.rank}       │
│         ││         ││         │
│         ││         ││         │
│    {self.card1.suit}    ││    {self.card2.suit}    ││    {self.card3.suit}    │
│         ││         ││         │
│         ││         ││         │
│       {self.card1.rank}││       {self.card2.rank}││       {self.card3.rank}│
└─────────┘└─────────┘└─────────┘
"""

