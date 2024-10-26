from random import randint


class Dice:
    def __init__(self):
        pass
    def roll(self):
        self.n = randint(1,6)
        if self.n == 1:
            print("[ . ]")
        elif self.n == 2:
            print("[. .]")
        elif self.n == 3:
            print("[: .]")
        elif self.n == 4:
            print("[: :]")
        elif self.n == 5:
            print("[:.:]")
        elif self.n == 6:
            print("[:::]")
