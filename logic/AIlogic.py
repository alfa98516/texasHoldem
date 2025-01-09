import random as r
from models.hand import *
from models.draw import *
from models.user import *

class AIlogic:
    def __init__(self):
        pass

    def AIbetLogic(self, hand: Hand, playerBet: int, minimum: int, user: User, draw: Draw) -> int:

        betInc = 0
        handCard1 = hand.card1.getVal()
        handCard2 = hand.card2.getVal()
        if not draw:
            if handCard1 == handCard2:
                betInc += 50
            
            if hand.card1.suit == hand.card2.suit:
                betInc += 20

            if handCard1+1 == handCard2 or handCard2 == handCard2+1:
                betInc += 20

            if r.randint(1, 8) == 8:
                betInc += r.randint(1, 50)
        else:
            drawList: list[Card] = [draw.card1, draw.card2, draw.card3]
            
            if draw.card4:
                drawList.append(draw.card4)
                if draw.card5:
                    drawList.append(draw.card5)

            for x in drawList:
                if x.getVal() == handCard1 or x.getVal() == handCard2:
                    betInc += 50
                if x.suit == hand.card1.suit or x.suit == hand.card2.suit:
                    betInc += 20
                if x.getVal() == handCard1-1 or x.getVal()-1 == handCard1:
                    betInc += 40
                if x.getVal() == handCard2-1 or x.getVal()-1 == handCard2:
                    betInc += 40

        if playerBet > betInc+minimum:
            try:
                bluffChance = (user.bluffCount / user.gameCount)*100
            except ZeroDivisionError:
                return playerBet-minimum
            d100 = r.rabint(1, 100)
            if d100 >= bluffChance:

                return playerBet-minimum
            
            return -1
        return betInc


