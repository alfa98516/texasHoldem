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
                    self.logicWrapper.bluffCheck(gameCards[0], playerBet, (round/4)*200, user)
                    print("Thanks For Playing :)")
                    return
                        

            AIbet += (round/4)*200
            pot += AIbet

            print(f"AI bets {AIbet}")
            t.sleep(1)

            self.clear(False, None, gameCards[1])
            




            