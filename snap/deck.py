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
    cards: list
        a list of Cards in the current deck

    Methods
    ----------
    __add__:
        add two decks together
    merge:
        returns a stack of n decks
    _shuffle:
        shuffle the deck
    deal:
        split the deck equally between two players
    """

    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
    VALUES = [*range(2, 15)]
    NAMES = [
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

    def __init__(self, cards=None):
        """
        Create a new deck of 52 cards.
        """
        if cards is None:
            cards = [
                Card(suit, value, name)
                for suit in self.SUITS
                for value, name in zip(self.VALUES, self.NAMES)
            ]
        self.cards = cards

    def __add__(self, other: "Deck") -> "Deck":
        """
        Add two decks together. Necessary for merge (below).

        :param other: another Deck to merge
        :returns Deck: a new Deck instance
        """
        return Deck(self.cards + other.cards)

    @classmethod
    def merge(cls, num_decks: int) -> "Deck":
        """
        Merge any number of decks into a single Deck.

        :param num_decks: the number of decks to create
        :returns Deck: a new Deck instance
        """
        return sum((cls() for i in range(1, num_decks)), cls())

    def _shuffle(self):
        """Shuffles the deck. Only used in deal()."""
        random.shuffle(self.cards)

    def deal(self) -> List[List[Card]]:
        """
        Deals the cards in the deck between two players.

        :returns List[List[Cards]]: a list of length 2, representing
        the cards to be dealt to player 1 and 2
        """
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
