class User:
    def __init__(self, userName: str, password: str, balance: int, gameCount: int, bluffCount: int):
        self.userName = userName
        self.password = password
        self.balance = balance
        self.gameCount = gameCount
        self.bluffCount = bluffCount
        