from player import Player
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
