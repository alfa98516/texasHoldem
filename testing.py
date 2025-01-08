from models.deck import *
from models.card import *
from models.hand import *
from storage.userStorage import *
import sys
import getpass

userStorage = UserStorage()

users = userStorage.getAllUsers()


deck = Deck()



hand1 = Hand(deck.deck[4], deck.deck[17])
hand2 = Hand(deck.deck[0], deck.deck[1])

print(hand1)
print(hand2)
