import logging
import random
from snap.deck import Card, Deck

# Set up logger
logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])


class Player:
    """
    Represents a player in the game of Snap

    Attributes
    ----------
    name: int
        the player's "name", e.g. 1 or 2
    cards: list
        the player's cards, populated when cards are dealt

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
        self.won_pile = []

    def __repr__(self) -> str:
        return f"Player {self.name}"

    def draw(self) -> Card:
        # draw the top card
        return self.cards.pop(0)

    def shout(self):
        print(f"{repr(self)}: SNAP!")


class Game:
    """
    Represents a game of Snap.

    Attributes
    ----------
    player_one: Player
        the first player
    player_two: Player
        the second player
    deck: Deck
        the deck to play with
    n_rounds:
        the number of rounds played so far
    pile: the winnable pile in each round

    """

    def __init__(self, num_decks: int):
        """
        Initialises a game of snap.
        1. Create two players
        2. Create a deck with the specified number of decks
        3. Initialise num_rounds to 0
        4. Shuffle and deal the cards
        5. Initialise an empty winnable pile

        :param num_decks: The desired number of decks
        """
        self.player_one = Player(1)
        self.player_two = Player(2)
        self.deck = Deck.merge(num_decks)
        self.n_rounds = 0
        logging.info("Dealing the cards...")
        self.player_one.cards, self.player_two.cards = self.deck.deal()
        self.pile = []

    def turn(self):
        """
        A turn in the game
        1. Both players draw a card
        2. The cards are added to the winnable pile
        3. If the cards match, a winner is picked randomly
        4. The winner adds the cards to their won pile
        """
        self.n_rounds += 1
        if not self.pile:
            self.pile = []

        card_one = self.player_one.draw()
        card_two = self.player_two.draw()

        # Add the cards to the winnable pile
        self.pile.extend([card_one, card_two])

        if card_one == card_two:
            # Pick a winner
            winner = random.choice([self.player_one, self.player_two])
            # The winner shouts
            winner.shout()
            # Add pile to pile of won cards
            winner.won_pile.extend(self.pile)

            self.pile.clear()

        else:
            logging.info(
                f"""No match in round {self.n_rounds}, the pile has {len(self.pile)} cards. Continuing..."""
            )

    @property
    def is_finished(self):
        """
        Check whether the players still have cards to play with.

        :returns bool: Whether there are cards left
        """
        # The game continues while either player has cards
        return not bool(self.player_one.cards)

    def declare_winner(self):
        """
        Declare the outcome of the game.
        1. If the players have won the same number, draw
        2. If uneven, declare a winner

        returns str: A string declaring the outcome
        """
        if len(self.player_one.won_pile) == len(self.player_two.won_pile):
            return "It's a draw!"
        if len(self.player_one.won_pile) > len(self.player_two.won_pile):
            winner = self.player_one
        else:
            winner = self.player_two

        return f"""
            {winner} wins after {self.n_rounds} rounds!
            They have won {len(winner.won_pile)} cards.
        """
