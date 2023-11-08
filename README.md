# # scrabble-2023-sofiasoler16
Sofia Soler

# main
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/sofiasoler16/clase_2023-23-ago/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/sofiasoler16/clase_2023-23-ago/tree/main)

# develop
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/sofiasoler16/clase_2023-23-ago/tree/develop.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/sofiasoler16/clase_2023-23-ago/tree/develop)

# coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/cca1f4b69e1cf5212778/test_coverage)](https://codeclimate.com/github/sofiasoler16/clase_2023-23-ago/test_coverage)

# Maintenability
[![Maintainability](https://api.codeclimate.com/v1/badges/cca1f4b69e1cf5212778/maintainability)](https://codeclimate.com/github/sofiasoler16/clase_2023-23-ago/maintainability)

## --- SCRABBLE GAME ---
Made by Sofia Soler 
Scrabble is a word game in which two to four players score points by placing tiles, each bearing a single letter, onto a game board divided into a 15×15 grid of squares. The tiles must form words that, in crossword fashion, read left to right in rows or downward in columns and are included in a standard dictionary or lexicon.

You will find a commented function at the end of models.py to play the game


## HOW TO PLAY
It is very important to Play using Capital Letters. 
When the game starts, the player has to enter the number of players that are gona play. 

Once this is done, it will start the game in player number 1 (0, in the game). Each player can choose whether to exchange a letter thar they got or start adding word to the board. 

Every time the players wants to add a letter it will be asked if they in fact want to add a letter whith the question: "Quiere agregar una letra? Y/N" They have to choose "Y" until thw word is over. Also when adds the letter it has to say where is the letter wanted, adding the row and the collumn when its asked.
When the players choose to end the word it is time to the next player to play!

This process will be made until one of the players run out of tiles, when that happend the game is gona end and the player who has no letters first it is gonna be the Winner

## RULES
The game it is code in inglish but it is played in spanish, so the rules a those of the spanish game
The Spanish-language games use these 98 tiles:

2 WildCards (0 points)

1 point: A×12, E×12, O×9, I×6, S×6, N×5, L×4, R×5, U×5, T×4

2 points: D×5, G×2

3 points: C×4, B×2, M×2, P×2

4 points: H×2, F×1, V×1, Y×1

5 points: CH×1, Q×1

8 points: J×1, Ñ×1, X×1, RRx1, LLx1

10 points: Z×1

There are Cells where the word the players put it is multiplied x2 or x3

## How to run the game
Execute the following commands in a Command Line Interface (CLI):

docker build --no-cache -t scrabble
docker run -i scrabble:latest
