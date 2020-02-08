from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    @property
    def consumption(self):
        return print(f'For your coat {((self.param / 6.5) - 0.5):.2f} m of wool is required.')

class Costume(Clothes):
    @property
    def consumption(self):
        return print(f'For your suit {(((self.param / 100) * 2) + 0.3):.2f} m of wool is required')

my_coat = Coat(46)
my_coat.consumption

my_suit = Costume(1.76)
my_suit.consumption




