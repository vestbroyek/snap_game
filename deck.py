import random
from typing import List


class Card:
    """
    Represents a playing card in a standard deck.
    A value of 2 is the lowest; 11 represents Jack ... 14 represents Ace.
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
    """

    def __init__(self, n_decks: int):
        self.cards = []
        for i in range(n_decks):
            deck = Deck()
            self.cards.extend(deck.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self) -> List[List[Card]]:
        # divide the deck into two
        # since a deck has 52 cards, len(self.cards) is always even
        halfway_point = len(self.cards) // 2
        # only need to shuffle before dealing, so can implement here
        self.shuffle()
        first_half = self.cards[:halfway_point]
        second_half = self.cards[halfway_point:]

        # the deck will be empty once dealing is complete
        self.cards.clear()
        return [first_half, second_half]
