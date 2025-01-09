from models.user import *
from models.hand import *
from models.draw import *
from wrappers.storageWrapper import *

class UserLogic:
    def __init__(self) -> None:
        self.storageWrapper = StorageWrapper()

    def loginLogic(self, username: str, password: str) -> User:
        users: list[User] = self.storageWrapper.getAllUsers()

        for x in users:
            if x.userName == username and x.password == password:
                return x
        return
    
    def bluffCheck(self, hand: Hand, bet: int, minimum: int, user: User, draw: Draw) -> bool:
        expectedBet = minimum
        card1 = hand.card1.getVal()
        card2 = hand.card2.getVal()

        if not draw:
            if card1 == card2:
                expectedBet += 50
            if hand.card1.suit == hand.card2.suit:
                expectedBet += 20
            if card1-1 == card2 or card2-1 == card1:
                expectedBet += 30
        else:
            drawList: list[Card] = [draw.card1, draw.card2, draw.card3]
            if draw.card4:
                drawList.append(draw.card4)
                if draw.card5:
                    drawList.append(draw.card5)
            for x in drawList:
                if x.getVal() == card1 or x.getVal() == card2:
                    expectedBet += 50
                if x.suit == hand.card1.suit or x.suit == hand.card2.suit:
                    expectedBet += 20
                if x.getVal() == card1-1 or x.getVal()-1 == card1:
                    expectedBet += 40
                if x.getVal() == card2-1 or x.getVal()-1 == card2:
                    expectedBet += 40

        if expectedBet+20 < bet:
            user.bluffCount += 1
            users: list[User] = self.storageWrapper.getAllUsers()
            for x in range(len(users)):
                if users[x].userName == user.userName:
                    users[x] = user
                    self.storageWrapper.saveNewUserJson(users)
                    break
            return True
        return False
                    


        