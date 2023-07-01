from snap.player import Player
from typing import List


def declare_winner(player: Player, pile: List):
    """
    Implements the sequence of winning a round of Snap:
    1. Shouting "SNAP"!
    2. Adding the pile to the player's cards
    3. Clearing up the pile

    :param player: a Player object representing the winning player
    :param pile: a list of Cards to be added to the winner's pile
    """
    player.shout()
    player.cards.extend(pile)
    pile.clear()


def generate_outcome_string(n_rounds: int, winner: Player, pile: List) -> str:
    """Generate a log message describing the outcome of the game.

    :param n_rounds: The number of rounds played
    :param winner: The winning Player
    :param pile: The size of the pile at the end of the game
    :returns str: A log message describing the outcome
    """

    return f"""
            Player one wins after {n_rounds} rounds!
            They have {len(winner.cards)} cards.
            The size of the pile is {len(pile)}"
        """
