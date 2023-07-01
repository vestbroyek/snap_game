import random
from typing import List


class Card:
    """
    Represents a playing card in a standard deck.
    A value of 2 is the lowest; 11 represents Jack ... 14 represents Ace.

    Attributes
    ----------
    suit: str
        the card's suit
    value: str
        the integer value of the card, between 2 and 14
    name: int
        a user-friendly representation of the name of the card
    """

    def __init__(self, suit: str, value: int, name: str):
        self.suit = suit
        self.value = value
        self.name = name

    def __repr__(self) -> str:
        return f"{self.name} of {self.suit}"

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.value == other.value


class Deck:
    """
    A deck of 52 standard playing cards.

    Attributes
    ----------
    suits: List
        a list of available suits
    values: str
        the integer values of the cards, between 2 and 14
    names: int
        user-friendly representations of the names of the card


    Methods
    ----------
    build:
        create a deck of 52 Cards
    """

    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    values = [*range(2, 15)]
    names = [
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        self.cards = [
            Card(suit, value, name)
            for suit in self.suits
            for value, name in zip(self.values, self.names)
        ]


class StackOfDecks:
    """
    A stack of decks, i.e. multiple Decks put together as if it were one deck.

    Attributes
    ----------
    cards: List[Card]
        all the cards in the deck

    Methods
    ----------
    _shuffle:
        shuffle the deck
    deal:
        first shuffle the deck, then return two halves

    """

    def __init__(self, n_decks: int):
        self.cards = []
        for i in range(n_decks):
            deck = Deck()
            self.cards.extend(deck.cards)

    def _shuffle(self):
        random.shuffle(self.cards)

    def deal(self) -> List[List[Card]]:
        # divide the deck into two
        # since a deck has 52 cards, len(self.cards) is always even
        halfway_point = len(self.cards) // 2
        # only need to shuffle before dealing, so can implement here
        self._shuffle()
        first_half = self.cards[:halfway_point]
        second_half = self.cards[halfway_point:]

        # the deck will be empty once dealing is complete
        self.cards.clear()
        return [first_half, second_half]
