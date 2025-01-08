import os
import art as a
from models.hand import *
from models.draw import *

class Clear:

    def clear(self, menu: bool = True, hand: Hand = None, draw: Draw = None):
        os.system('cls' if os.name=='nt' else "clear")

        if menu:
          print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
          a.tprint("Texas Hold'em", "3D Diagonal")
          print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        else:
          if hand:

            a.tprint("Your Hand", "3D Diagonal")

            print(f"{hand}")
          else:
            a.tprint("Drawn Cards", "3D Diagonal")
            print(f"{draw}")