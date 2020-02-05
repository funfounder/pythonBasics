from abc import ABC, abstractmethod

class Clothes:
    def __init__(self, title='Noname'):
        self.title = title
    @abstractmethod
    def name(self):
        return print(f'This clothes is made by {self.title}')

class Coat(Clothes):
    def tailor(self, v):
        self.v = v
        return print(f'For your coat {((self.v / 6.5) - 0.5):.2f} m of wool is required.')
    @property
    def name(self):
        return print(f'This coat is made by {self.title}')


class Suit(Clothes):
    def tailor(self, h):
        self.h = h
        return print(f'For your suit {(((self.h / 100) * 2) + 0.3):.2f} m of wool is required')
    @property
    def name(self):
        return print(f'This coat is made by {self.title}')


my_coat = Coat('Lampard')
my_coat.tailor(46)
my_coat.name

my_suit = Suit('Sourd')
my_suit.tailor(1.76)
my_suit.name

my_clothes = Clothes()
my_clothes.name()



