from abc import ABC, abstractmethod

class Clothes:
    @abstractmethod
    def name(self, title='Noname'):
        self.title = title
        return print(f'This clothes is made by {title}.')

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def tailor(self):
        return print(f'For your coat {((self.v / 6.5) - 0.5):.2f} m of wool is required.')

    def name(self, title='Noname'):
        return print(f'This coat is made by {title}')

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def tailor(self):
        return print(f'For your suit {(((self.h / 100) * 2) + 0.3):.2f} m of wool is required')

    def name(self, title='Noname'):
        return print(f'This suit is made by {title}')

my_coat = Coat(46)
my_coat.tailor
my_coat.name('Lampard')

my_suit = Suit(1.76)
my_suit.tailor
my_suit.name('Sourd')




