from tui.clear import *
from getpass import *
from wrappers.logicWrapper import *
from tui.gameUI import *

class MainUI(Clear):
    def __init__(self) -> None:
        self.logicWrapper = LogicWrapper()
        self.gameUI = GameUI()

    def login(self) -> None:
        name: str = input("Please input username: ")
        password: str = getpass("Please input Password: ")
        user: User = self.logicWrapper.loginLogic(name, password)

        if user:
            self.menu(user)
        else:
            print("User Not Found")
    

    def menu(self, user) -> None:
        while True:
            self.clear()
            print("1.) Play ")
            print("2.) Leaderboard")
            print("3.) Go Back")
            option: str =  input("Please Choose Option: ").strip()

            match option:
                case "1":
                    self.gameUI.main(user)
                    continue
                case "2":
                    self.leaderboard(user)
                    continue
                case "3":
                    return
                case _:
                    print("not valid")
                    input("press enter to continue....")
                    self.clear()
                    continue

    def leaderboard(self, user) -> None:
        self.clear()
        print("Not implemented yet.....")
        input("Press enter to continue....")
                      

