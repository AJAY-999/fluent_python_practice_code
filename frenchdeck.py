from collections import namedtuple
from random import choice

Card = namedtuple('Card',['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)]+list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
        for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
        
    def __getitem__(self, position):
        #This method makes our deck iterable as a result we can use 'in' operator
        return self._cards[position]
    


deck = FrenchDeck()#__init__
print(len(deck))#__len__
print(deck[-1])#__getitem__

print(choice(deck))

print([card for card in deck._cards])

print(Card(rank='2', suit='spades') in deck)

print(Card(rank='2', suit='beasts') in deck)