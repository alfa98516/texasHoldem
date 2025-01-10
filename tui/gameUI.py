from tui.clear import *
from wrappers.logicWrapper import *
from models.deck import *
from models.card import *
from models.hand import *
from models.draw import *
import time as t
class GameUI(Clear):
    def __init__(self):
        self.logicWrapper = LogicWrapper()

    def main(self, user: User):
        self.clear()
        print("You will be playing against an AI, since this is a completely offline TUI system")
        t.sleep(1)
        print("First you and the AI draw two cards")
        print("Then You make a bet and the first 3 cards are shown")
        t.sleep(1)
        deck = Deck()
        gameCards: list[Hand, Draw, Hand] = self.logicWrapper.initializeGame(deck)
        quit = 0
        round = 1
        pot = 0
        while not quit:

            self.clear(False, gameCards[0])
            try:
                print(f"Your current balance: {user.balance}")
                print(f"Minimum bet is {(round/4)*200}")
                playerBet = int(input("Please input bet amount: "))
                if playerBet < (round/4) * 200:
                    print("Bet Not High Enough")
                    input("Press Enter To Continue.....")
                    continue
                if playerBet > user.balance:
                    print("Not Enough Balance in account")
                    input("Press Enter To Continue.....")

            except ValueError:
                print("Bet Amount Invalid")
                input("Press Enter To Continue.....")
                continue

            pot += playerBet
            user.balance -= playerBet

            AIbet = self.logicWrapper.AIbetLogic(gameCards[2], playerBet, (round/4)*200, user)
            if AIbet < 0:
                print("AI Folds, You Win The Pot")
                user.balance += pot + (round/4)*200
                print(f"{(round/4)*400} has been added to your balance")
                while True:
                    usrInput: str = input("Play next round? (y/n): ").strip()
                    if usrInput.lower() == "y":
                        round +=1
                        continue
                    if usrInput.lower() == "n":
                        quit = True
                    user.gameCount += 1
                    if self.logicWrapper.bluffCheck(gameCards[0], playerBet, (round/4)*200, user):
                        print("You liar, I'll get you next time")
                    print("Thanks For Playing :)")
                    return
            


            AIbet += (round/4)*200
            pot += AIbet

            print(f"AI bets {AIbet}")
            t.sleep(1)
            while True:
                self.clear(False, None, gameCards[1])
                print(gameCards[0])
                print("1.) Raise")
                print("2.) Call")
                print("3.) Fold")
                print()
                usrInput: str = input("Please Choose an Option: ")
                
                if usrInput == "1":
                    print(f"Current bet: {playerBet}")
                    try:
                        betInc: int = int(input("How much more would you like to increse?: "))
                        if betInc < 0:
                            print("Bet Needs to be a Positive Integer")
                            input("Press Enter To Continue....")
                            continue
                        if betInc > user.balance:
                            print("Not Enough Balance in Account")
                            input("Press Enter To Continue....")
                            continue
                    except ValueError:
                        print("Bet Needs to be a number")
                        input("Press Enter To Continue....")
                        continue
                    pot += betInc
                    user.balance -= betInc
                    user.gameCount += 1
                    print("Funds Have Been Withdrawn from Account")
                    break
                if usrInput == "2":
                    print("Good Choice")
                    round += 1
                    user.gameCount += 1
                    break
                if usrInput == "3":
                    user.balance -= playerBet
                    user.gameCount += 1
                    print(f"{playerBet} withdrawn from account")
                    t.sleep(1)
                    self.clear(False)
                    a.tprint("AI Cards", "3D Diagonal")
                    print(gameCards[2])
                    input("Press enter to continue.....")
                    quit = True
                else:
                    print("Not Valid")
                    continue

            if usrInput == "2" or usrInput == "1":
                betInc = self.logicWrapper.AIbetLogic(gameCards[2], playerBet, (round/4)*200, user)
                if betInc < 0:
                    print("AI Folds, You Win The Pot")
                    if self.logicWrapper.bluffCheck(gameCards[0], playerBet, (round/4)*200, user, gameCards[1]):
                        print("You liar, I'll get you next time")
                    user.balance += pot + (round/4)*200
                AIbet += betInc
                pot += AIbet 
                print(f"AI adds {betInc} to pot")
                while True:
                    self.clear(False, None, gameCards[1])
                    if AIbet > playerBet:
                        print("1.) Call")
                        print("2.) Fold")
                        usrInput: str = input("Please Choose Option: ")
                        if usrInput == "1":
                            user.balance -= (AIbet - playerBet)
                            pot += (AIbet - playerBet)
                            playerBet = AIbet

                        if usrInput == "2":
                            pass
                        else:
                            print("Not Valid")
                            continue




            