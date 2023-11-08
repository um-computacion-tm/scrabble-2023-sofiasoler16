# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog],
and this project adheres to [Semantic Versioning].

## [0.34] - 4-11-23
Fixed tiles_cambiadas
Added functions to first_turn 
Added the score function to the current turn
Added Cli Class and a function to play the game 

## [0.33] - 2-11-23
Made teh function has_letters to be able to remove the letters from the player bag

## [0.32] -  1-11-23
Created function to start game
Fixed function to verify if player has letters
Fixed some error of maintenbility 

# [0.31] - 31-10-23
FIxed validate_connected_word

## [0.30] - 30-10-23
Change validate_conncected_word to validate if it is not near word

## --- SEXTO SPRINT ---

## [0.29] - 24-10-23
Fixed board problem of showing the board backwards
FIxed validate_connected_words

## [0.28] - 23-10-23
Added funcion to validate connected words

## [0.27] - 21-10-23
Fixed function to change the state of a player
Made a function to tell if the player is winning the game or not
Made a function to end the game when a player has no tiles

# [0.26] - 18-10-23
Added the multipliers to the board

## [0.25] - 17-10-23
Made a function to get the player acount

## [0.24] 11-10-23
Fixed the board to be able to calculate the word value

## --- QUINTO SPRINT --- 

## [0.23] - 10-10-23
Added a function to remove the word if it is invalid
Word triple multiplier 

## [0.22] - 9-10-23
Added a word multiplier

## [0.21] - 8-10-23
Added a function to show the board
Added Cli class and a function to ask the player_count

## [0.20] - 7-10-23
Added a  triple cell multiplier function

## [0.19] - 4-10-23
Change the multiplier_value function to Board and fix it
Add all the possible cells that can contain a doble Multiplier

## [0.18] - 3-10-23
Try to add all the possible cells that can contain a multiplier

## [0.17] - 27-9-23
Added a function to validate if the player has the letters that use to play
Fixed the score_player function to check the score of more than 1 word

## --- CUARTO SPRINT ----

## [0.16.5] - 25-9-23 2do
Fixed function that calculate the word value just if it is in the dictionary

## [0.16] - 25-9-23 1ro
Try to make a function to check if the calculated word is in the dictionary

## [0.15] - 24-9-23
Add a function to calculate the player score

## [0.14] - 23-9-23
Made a function to check if the board is empty

## [0.13.2] - 22-9-23 2do
Made a new function to calculate the value of a word to fix the old one

## [0.13] - 22-9-23  1ro
Add the posibility to the cell of not having any value
(Try to fix the calculate_word_value funcion)

## [0.12] - 13-9-23
Created function to check if the words are inside the board 

## --- TERCER SPRINT ---

## [0.11.2] - 11-9-23 
Fixed the multiplier_value function
Made a function to calculate the value of a word

## [0,11] - 11-9-23 
Created a word class and added a function that calculate the word value

## [0.10] - 09-09-2023
Added a dictionary and created a function that returns if the word is valid

## [0.9] - 08-09-2023
Created a funcion in Main that checks if the word is valid

## [0.8] - 07-09-2023
Created class Main
Created a function that checks if the number of players that want to play is over the limit

## [0.7] - 06-09-2023
Created the function next_turn that change the current player 

## [0.6] - 30-08-2023
Added the posibility to the celll multiplier to be use just one time adding the atribute used

# --- SEGUNDO SPRINT ---

## [0.5] - 29-08-2023
Updated the Cell class, added a multiplier for each cell to calculate the value

## [0.4.1] - 28-08-2023 - Afternoon
Created a function for the players that defines the states that the player can have 

## [0.4] - 28-08-2023 - Morning
Added a function thats gives the player the possibility to change a tile for another

## [0.3] - 23-08-2023
Created classes Player, Board and Cell
Added a function to add letters to a player

## [0.2] - 20-08-2023
Created the put method in BagTile class
Add a dictionary for the updated tiles during the game

## [0.1] - 16-08-2023
Created classes Tile and BagTile
Improved the way to access the tiles using a dictionary
Add the value and quantity of each tile
# --- PRIMER SPRINT ---