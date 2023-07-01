from snap.deck import Card


class Player:
    """
    Represents a player in the game of Snap

    Attributes
    ----------
    name: int
        the player's "name", e.g. 1 or 2
    cards: list
        the player's cards, populated not on class instantiation but when cards are dealt

    Methods
    ----------
    draw:
        take the first Card from the stack of cards
    shout:
        shout "SNAP" to win the round
    """

    def __init__(self, name: int):
        self.name = name
        self.cards = []

    def __repr__(self) -> str:
        return f"Player {self.name}"

    def draw(self) -> Card:
        # draw the top card
        return self.cards.pop(0)

    def shout(self):
        print(f"{repr(self)}: SNAP!")
