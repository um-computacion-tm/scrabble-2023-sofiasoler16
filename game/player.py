
from game.tile import BagTiles, Tile
from game.models import *
from game.board import Board

class Not_Letters_Exception(Exception):
    pass

class Player():
    def __init__ (self,bag:BagTiles):
        self.tilesp = []
        self.bag = bag
        self.name = ""
        self.score = 0
        self.player_estado = "jugando"
        self.current_word_value = 0
        for _ in range(7):
            self.tilesp.append(self.bag.take())
#Como testeo que resta la cantidad de letras tambien para el siguiente jugador?
        self.current_player = None

    def tiles_cambiadas(self, tile:BagTiles):
        print(self.tilesp)
        a = True
        while a == True:
            try:
                letterchoice = str(input("Ingrese letra para devolver (en mayuscula): "))
                if letterchoice in self.tilesp:
                    self.tilesp.remove(letterchoice)
                    self.bag.put_in_bag(letterchoice)
                    self.tilesp.append(self.bag.take())
                    a = False
                else:
                    raise ValueError("No puede intercambiar letras que no tiene")
            except ValueError as error:
                print("NO puede intercambiar letras que no tiene")
        print("Sus nuevas letras son: ", self.tilesp)

    def winning_player(self,all_players):

        for player in all_players:
            if len(self.tilesp) == 0:
                self.player_estado = "terminado"
                
            player:Player
            if self.score > player.score:
                self.player_estado = "ganando"
            elif self.score < player.score: #No marca que esta perdiendo, lo deja en jugando
                player.player_estado = "perdiendo"

    def put_word(self, board:Board, bag:BagTiles, word:Word):
        board.show_board()

        si = str(input("Quiere agregar letra? Y/N: "))
        self.wordlist = []
        self.current_word_value = 0

        while si == "Y":
            row = input("Ingrese fila: ")
            column = input("Ingrese columna: ")
            letter = input("Ingrese letra a agregar: ")
            bag.tiles[letter]
            board.grid[int(row)][int(column)].add_letter(bag.tiles[letter])
            self.wordlist.append(board.grid[int(row)][int(column)])
            board.calculate_cell_value(board.grid[int(row)][int(column)])
            si = str(input("Quiere agregar letra? Y/N: "))

        self.current_word_value= word.calculate_word_value(self.wordlist)
        print("el valor de la palabra es: ", self.current_word_value)
        board.validate_empty_board(board.grid[7][7])
        


    def show_tiles(self):
        return self.tilesp

    def score_player(self, wordvalue): 
        player_word_score = 0
        self.words = []

        player_word_score += (wordvalue)
        self.score += (player_word_score)
    
    def has_letters(self, tiles:list[Tile]):
        
        for letter in tiles:
            if letter.letter in self.tilesp:
                self.tilesp.remove(letter.letter)
            else:
                print('Error, no tiene las letras suficientes')

        return True

            
                