from abc import abstractmethod  , ABCMeta
from enum import Enum
import random
class Suit(Enum):
    CLUB=0
    DIAMOND=1
    HEART=2
    SPADE=3

class Card(metachass=ABCMeta):
    def __init__(self , valueOnCard  , suit   ):
        self._valueOncard=valueOnCard
        self._suit=suit
    def getValueOnCard(self):
        return self._valueOncard

    def getSuit(self):
        return self._suit

    @abstractmethod
    def getValue(self):
        pass

class BlackJCard(Card):
    def __init__(self , valueOnCard , suit):
        super.__init__(valueOnCard , suit)

    def getValue(self):
        if self._valueOncard>10:
            return 10
        else:
            return self._valueOncard

class Hand:

    def __init__(self , cards):
        self._cards=cards

    def getCard(self , card):
        self._cards.append(card)

    def getScore(self):
        score=0
        for card in self._cards:
            score+=card.getValue()
        return score

class BlackJHand(Hand):
    BlackJ=21

    def __init__(self , cards):
        super.__init__(cards)
    def getScore(self):
        #blackJ Score

    def possibleScore(self):
        #get all possible score
class Deck:

    def __init__(self):
        self._cards=self._initCard()
        self._dealIdx=0
    def remainingCard(self):
        return len(self._cards)-self._dealIdx

    def dealCard(self):
        if self._dealIdx==len(self._cards):
            raise Exception('Run out of cards')
        card= self._cards[self._dealIdx]
        self._dealIdx+=1
        return
    def shuffle(self):
        random.shuffle(self._cards)
    def _initCard(self):
        # initializion  _cards with all 52 card
