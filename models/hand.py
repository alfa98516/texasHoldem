from models.card import *

class Hand:
    def __init__(self, card1: Card, card2: Card):
        self.card1 = card1
        self.card2 = card2
    
    def __str__(self) -> str:
        if self.card1.rank == "10" and self.card2.rank == "10" and False:
            return f"""        ┌─────────┐┌─────────┐
        │{self.card1.rank}       ││{self.card2.rank}       │
        │         ││         │
        │         ││         │
        │    {self.card1.suit}    ││    {self.card2.suit}    │
        │         ││         │
        │         ││         │
        │       {self.card1.rank}││       {self.card2.rank}│
        └─────────┘└─────────┘"""
        if self.card1.rank == "10" and False:
            return f"""        ┌─────────┐┌─────────┐
        │{self.card1.rank}       ││{self.card2.rank}        │
        │         ││         │
        │         ││         │
        │    {self.card1.suit}    ││    {self.card2.suit}    │
        │         ││         │
        │         ││         │
        │       {self.card1.rank}││        {self.card2.rank}│
        └─────────┘└─────────┘"""
        if self.card2.rank == "10" and False:
            return f"""        ┌─────────┐┌─────────┐
        │{self.card1.rank}        ││{self.card2.rank}       │
        │         ││         │
        │         ││         │
        │    {self.card1.suit}    ││    {self.card2.suit}    │
        │         ││         │
        │         ││         │
        │        {self.card1.rank}││       {self.card2.rank}│
        └─────────┘└─────────┘"""


        return f"""        ┌─────────┐┌─────────┐
        │{self.card1.rank:<1}        ││{self.card2.rank:>1}        │
        │         ││         │
        │         ││         │
        │    {self.card1.suit}    ││    {self.card2.suit}    │
        │         ││         │
        │         ││         │
        │        {self.card1.rank:<1}││        {self.card2.rank:>1}│
        └─────────┘└─────────┘"""
