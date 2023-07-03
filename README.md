# SNAP!
This project implements a game of Snap. 

## Overview
In Snap, 

1. The players are dealt cards from a standard playing deck (or multiple decks). 
2. In every round, they will draw a card from their pile. If their cards' values match, whoever first shouts 'Snap!' wins the cards in the pot. If they don't match, the cards are added to the pot and another round begins.
3. Whoever has the most won cards at the end, wins.

### Caveats
- This project only implements a game between two players.
- Draw rounds, where players shout 'Snap!' simultaneously, are not implemented.

## How to run
No third-party libraries have been used, so no `requirements.txt` has been provided. Linting and formatting has been done with `flake8` and `black` but they are not required to run the project.

To play the game, run `python3 main.py` from the root directory. You will be prompted with how many decks you would like to play with. The game will then proceed, logging the outcome of every round and the outcome of the game.

The code was written with Python 3.10.9 but should run with any version of Python 3.

## Possible improvements
- Allow more than 2 players to play
- Restrict the number of decks that can be played with
- Think more about testing and possible edge cases, e.g. nobody wins