from decks import StackOfDecks, Player
import logging
import random
from utils import declare_winner

# Set up logger
logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])

if __name__ == "__main__":
    logging.info("Let the game commence!")

    # Create two players
    player_one, player_two = Player(1), Player(2)

    n_decks = int(
        input("How many decks would you like to play with? Please enter an integer... ")
    )

    # Create a stack of the required number of decks, acting as one big deck
    deck = StackOfDecks(n_decks)

    # Deal the cards (they will be shuffled as part of dealing)
    logging.info("Dealing the cards...")
    player_one.cards, player_two.cards = deck.deal()

    logging.info("We'll now proceed to draw cards!")

    n_rounds = 0
    pile = []

    # play continues while both players have cards
    while player_one.cards and player_two.cards:
        n_rounds += 1
        card_one = player_one.draw()
        card_two = player_two.draw()

        # Add the cards to the winnable pile
        pile.extend([card_one, card_two])

        if card_one == card_two:
            # if the cards match, randomise who shouts first
            if random.random() >= 0.5:
                declare_winner(player_one, pile)
            else:
                declare_winner(player_one, pile)

        else:
            logging.info(f"No match in round {n_rounds}, continuing...")

    if len(player_one.cards) > len(player_two.cards):
        logging.info(
            f"Player one wins after {n_rounds}! They have {len(player_one.cards)} cards. The size of the pile is {len(pile)}"
        )
    else:
        logging.info(
            f"Player two wins after {n_rounds} rounds! They have {len(player_two.cards)} cards. The size of the pile is {len(pile)}"
        )
