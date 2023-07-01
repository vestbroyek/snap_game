# SNAP!
This project implements a game of Snap. 

## Overview
In Snap, the players are dealt cards from a standard playing deck (or multiple decks). In every round, they will draw a card. If their cards' values match, whoever first shouts 'Snap!' wins the cards in the pot. If they don't match, the cards are added to the pot and another round begins.

### Caveats
- This project only implements a game between two players.
- Draw rounds, where players shout 'Snap!' simultaneously, are not implemented.

## How to run
No third-party libraries have been used, so no `requirements.txt` has been provided.

To play the game, run `main.py`. You will be prompted with how many decks you would like to play with. The game will then proceed, logging the outcome of every round and the outcome of the game.