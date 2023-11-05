import random

from game.dictionary import *
from game.tile import *
from game.cell import *
from game.word import *
from game.board import *
from game.player import Player

class YaHaySuficientes(Exception):
    pass

class Cli():
    def __init__(self):
        main = Main()
        main.get_player_acount()

        self.scrabble = ScrabbleGame(main.player_count)
    def play(self):
        self.scrabble.game_started()
        while self.scrabble.game_state == "ongoing":
            self.scrabble.first_turn()


class ScrabbleGame():
    def __init__(self, players_count):
        self.word = Word()
        self.board = Board()
        self.bag = BagTiles()
        self.players = []
        self.current_player = None
        self.player_index = 0
        self.game_state = None
        self.turn_number = 0

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
        self.turn_number += 1

    def game_started(self):
        self.game_state = 'ongoing'
    
    def end_game(self):
        if self.current_player.player_estado == "terminado":
            self.game_state = "over"
        else:
            self.game_state = "ongoing"
            
    # def assign_name_current_player(self):
    #     name = input("Escriba nombre del jugador ", self.current_player)
    #     self.current_player

    def first_turn(self):
        if self.board.validate_empty_board(self.board.grid[7][7]) is True:
            self.next_turn()

            print("ESTA JUGANDO EL JUGADOR: ", self.player_index)
            self.new_word()

            self.current_player.score_player(self.current_player.current_word_value)
            print("EL SCORE DEL JUGADOR ES: ", self.current_player.score)
            print("OK, siguiente turno")
            self.end_game()
            
        else:
            self.next_turn()

            print("ESTA JUGANDO EL JUGADOR: ", self.player_index)
            self.new_word()

            print("EL SCORE DEL JUGADOR ES: ", self.current_player.score)
            print("OK, siguiente turno")
            self.end_game()
            self.next_turn()


    # def all_turn(self):
    #     self.next_turn()

    #     print("ESTA JUGANDO EL JUGADOR: ", self.player_index)
    #     self.new_word()

    #     self.current_player.score_player(self.current_player.current_word_value)
    #     print("EL SCORE DEL JUGADOR ES: ", self.current_player.score)
    #     print("OK, siguiente turno")
    #     self.next_turn()
    

    
    def new_word(self):
        b = True
        while b == True:
            pregunta = str(input("Va a agregar palabra? Y/N (Si elije no saltea el turno)"))
            pregunta
            if pregunta != "Y":
                b == False
                break
            a = self.current_player.put_word(self.board, self.bag, self.word)
            a
#Si no se valida la palabra pregunte si quiere saltear y si si quiere termine
                
            if self.board.status == "not empty":
                b = False
            elif self.board.status != "not empty":
                    print("ERROR: No hay letras en la posicion (7,7)")
            elif self.turn_number != 0: #No valida si estan conectadas 
                if self.board.validate_connected_word3(self.current_player.wordlist):
                    self.current_player.score_player(self.current_player.current_word_value)
                else:
                    print("La palabra no esta conectada")
            
            pregunta
            if pregunta != "Y":
                b == False
                


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
                self.player_count = int(input("Enter the number of players (max 4)"))
                if 1 <= self.player_count <= 4:
                    print("Good")
                    break
                else:
                    raise ValueError("Number must be between 1 and 4")
            except ValueError as error:
                print("Error, enter a valid number between 1 and 4")


# cli = Cli()
# cli.play()







