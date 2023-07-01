from deck import Card

class Player:
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