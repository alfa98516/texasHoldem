from models.deck import *
from models.card import *
from models.hand import *
from models.draw import *
from storage.userStorage import *
import sys
import getpass

userStorage = UserStorage()

users = userStorage.getAllUsers()


deck = Deck()



hand1 = Hand(deck.deck[4], deck.deck[17])
hand2 = Hand(deck.deck[0], deck.deck[1])

draw = Draw(deck.deck[4], deck.deck[17], deck.deck[18])

print(draw)

draw.card4 = deck.deck[20]

print(draw)

draw.card5 = deck.deck[47]

print(draw)



print(int("9 "))