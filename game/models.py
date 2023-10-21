import random

from game.dictionary import *
from game.tile import *
from game.cell import *
from game.word import *
from game.board import *
from game.player import *

class YaHaySuficientes(Exception):
    pass

        
class Cli():
    def __init__(self):
        pass


class ScrabbleGame():
    def __init__(self, players_count):
        self.board = Board()
        self.bag = BagTiles()
        self.player = Player(self.bag)
        self.players = []
        self.current_player = None
        self.player_index = 0
        self.game_state = None

        for _ in range(players_count):
            self.players.append(Player(bag=self.bag))

    def next_turn(self):
        if self.current_player == None:
            self.current_player = self.players[self.player_index]
        elif self.current_player == self.players[-1]:
            self.player_index = 0
            self.current_player = self.players[self.player_index]
        else:
            self.player_index += 1
            self.current_player = self.players[self.player_index]
    
    def end_game(self):
        if self.player.player_estado == "terminado":
            self.game_state = "over"



class Main(): #Te deja entrar cantidad de jugadores y verifica que sea bueno
    def __init__(self):
        self.status_players = "valid"
        self.player_count = 0
        self.status_word = None
        self.board = Board()
        self.cell = Cell(None, None)
    #Hacer una funcion que pida el player_count
    def get_player_acount(self):
        while True:
            try:
                self.player_count = int(input("Enter the number of players (max 3)"))
                if self.player_count <= 3:
                    print ("Good")
                    break
            except Exception as more_than_expected: #Porque no hace esta parte?
                print ("Error, enter a valid number between 1 and 3")

    def valid_player_count(self):
        if self.player_count <= 1 or self.player_count > 4:
            self.status_players = "invalid"  
        self.status_players = "valid"


# Arreglar el Maintanbility






