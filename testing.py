from models.deck import *
from models.card import *
from storage.userStorage import *
import sys
import getpass

userStorage = UserStorage()

users = userStorage.getAllUsers()

print(users[0].userName)