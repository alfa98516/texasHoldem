from models.deck import *
from models.card import *
from models.hand import *
from storage.userStorage import *
import sys
import getpass

userStorage = UserStorage()

users = userStorage.getAllUsers()


deck = Deck()

print(deck)

hand1 = Hand(deck.deck[4], deck.deck[17])


print(hand1)

