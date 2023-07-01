from player import Player
from typing import List

def declare_winner(player: Player, pile: List):
    player.shout()
    player.cards.extend(pile)
    pile.clear()