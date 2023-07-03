import logging
from snap.game import Game

# Set up logger
logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])

if __name__ == "__main__":
    logging.info(
        """Welcome to this game of Snap.
                 How many decks would you like to play with?"""
    )

    n_decks = None
    while not isinstance(n_decks, int):
        try:
            n_decks = int(input("Please enter an integer... "))
        except ValueError:
            logging.warning("Please enter a valid integer...")

    game = Game(n_decks)

    while not game.is_finished:
        game.turn()

    else:
        logging.info(game.declare_winner())
