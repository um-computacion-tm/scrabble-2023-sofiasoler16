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
        self.inplay = None
        main = Main()
        main.get_player_acount()
        
        self.scrabble = ScrabbleGame(main.player_count)

    def play(self):
        self.scrabble.game_started()
        while self.scrabble.game_state == "ongoing":
            
            self.scrabble.iniciate_turn()
            self.inplay = "yes"
        self.inplay = "no"
        for win in self.scrabble.players:
            if win.player_estado == "ganando":
                winner = win.index

                print("El ganador es: Player", winner)


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
        self.already_board_cell = []

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

    def iniciate_turn(self):
        if self.board.validate_empty_board(self.board.grid[7][7]) is True:
            self.turnt()
            
        else:
            self.turnt()
            
            
    def turnt(self):
            self.next_turn()
            self.current_player.index = self.player_index

            print("ESTA JUGANDO EL JUGADOR: ", self.player_index)
            print("Las tiles del jugador ", self.player_index, "son ", self.current_player.tilesp)
            
            self.elecc = input("MENU: 1. Cambiar letras 2. Anadir palabra, (Puede usar su turno para 1 opcion)")
            if self.elecc == "1":
                self.current_player.tiles_cambiadas()
                
            elif self.elecc == "2":
                self.new_word()
                

            self.current_player.score_player(self.current_player.current_word_value)
            if self.elecc == "2" and self.board.status == "not empty":
                for cell in self.current_player.cell_wordlist:
                    self.already_board_cell.append(cell)
            

            print("EL SCORE DEL JUGADOR ES: ", self.current_player.score)
            print("OK, siguiente turno")
            
            self.end_game()

    def new_word(self):
        b = True
        while b == True:
            self.pregunta = str(input("Va a agregar palabra? Y/N (Si elije no saltea el turno)")) #Si no se valida la palabra pregunte si quiere saltear y si si quiere termine
            self.pregunta
            if self.pregunta != "Y":
                b == False
                break
            if self.board.validate_empty_board(self.board.grid[7][7]) is True:
                a = self.current_player.put_word_first(self.board, self.bag, self.word)
                a
                if self.board.status == "not empty":
                    b = False
                elif self.board.status != "not empty":
                    print("ERROR: No hay letras en la posicion (7,7)")
            else:
                self.current_player.put_not_first_word(self.board, self.bag, self.word, self)
            
            self.pregunta
            if self.pregunta != "Y":
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


