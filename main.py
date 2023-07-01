import logging
import random
from snap.utils import declare_winner, generate_outcome_string
from snap.player import Player
from snap.deck import StackOfDecks

# Set up logger
logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])

if __name__ == "__main__":
    logging.info("Let the game commence!")

    # Create two players
    player_one, player_two = Player(1), Player(2)

    logging.info("How many decks would you like to play with?")
    try:
        n_decks = int(input("Please enter an integer... "))
    except ValueError:
        logging.warning("That is not a valid integer.")
        n_decks = int(input("Please enter an integer... "))

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
            # If the cards match, randomise who shouts first
            if random.random() >= 0.5:
                declare_winner(player_one, pile)
            else:
                declare_winner(player_one, pile)

        else:
            logging.info(f"No match in round {n_rounds}, continuing...")

    if len(player_one.cards) > len(player_two.cards):
        logging.info(generate_outcome_string(n_rounds, player_one, pile))
    else:
        logging.info(generate_outcome_string(n_rounds, player_two, pile))
