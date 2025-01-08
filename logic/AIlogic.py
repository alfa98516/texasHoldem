import random as r
from models.hand import *
from models.draw import *
from models.user import *

class AIlogic:
    def __init__(self):
        pass

    def AIbetLogic(self, hand: Hand, playerBet: int, minimum: int, draw: Draw, user: User) -> int:

        betInc = 0

        if hand.card1.rank == hand.card2.rank:
            betInc += 50
        
        if hand.card1.suit == hand.card2.suit:
            betInc += 20

        if hand.card1.getVal()+1 == hand.card2.getVal() or hand.card1.getVal() == hand.card2.getVal()+1:
            betInc += 50

        if r.randint(1, 8) == 8:
            betInc += r.randint(1, 20)

        if playerBet > betInc+minimum:
            betInc = playerBet-minimum
            return betInc


        return betInc


