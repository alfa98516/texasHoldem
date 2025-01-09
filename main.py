from tui.mainUI import *
from tui.clear import *

 
MAIN = MainUI()
CLEAR = Clear()
CLEAR.clear()

option: str = "0"
while option != "2":
    print("1.) Login")
    print("2.) Exit")
    option: str = input("Please choose option: ")

    match option:
        case "1":
            CLEAR.clear()
            MAIN.login()
            CLEAR.clear()
            continue
        case "2":
            print("Goodbye :)")
        case _:
            print("Not Valid")
            input("Press enter to continue....")
            CLEAR.clear()
