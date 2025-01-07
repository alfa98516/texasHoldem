import os
import art as a
from models.hand import *

class Clear:

    def clear(self, menu: bool = True, hand: Hand = None):
        os.system('cls' if os.name=='nt' else "clear")

        if menu:
          print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
          a.tprint("Texas Hold'em", "3D Diagonal")
          print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        else:
          print("-"*30)
          a.tprint("Your Hand", "3D Diagonal")
          print("-"*30)
          print(f"{hand}")