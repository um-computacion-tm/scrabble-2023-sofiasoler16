
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
        for _ in range(7):
            self.tilesp.append(self.bag.take())
#Como testeo que resta la cantidad de letras tambien para el siguiente jugador?
        self.current_player = None

    def tiles_cambiadas(self, letterchoice:Tile):
        letter = letterchoice #Que no sea random choice, que sea una letra elegida por usuario
        self.tilesp.pop(self.bag.put_in_bag(letter))
        self.tilesp.append(self.bag.take())

    def cambio_estado(self):
        if len(self.tilesp) == 0:
            self.player_estado = "terminado"

    def winning_player(self,all_players):
        for player in all_players:
            player:Player
            if self.score > player.score:
                self.player_estado = "ganando"
            elif self.score < player.score: #No marca que esta perdiendo, lo deja en jugando
                player.player_estado = "perdiendo"

    def put_word(self, board:Board, bag:BagTiles):
        si = str(input("Quiere agregar letra? Y/N: "))
        word = list[Cell]
        while si == "Y":
            row = input("Ingrese fila: ")
            column = input("Ingrse columna: ")
            letter = input("Ingrese letra a agregar: ")
            bag.tiles[letter]
            board.grid[int(row)][int(column)].add_letter(bag.tiles[letter])
            print(board.grid[int(row)][int(column)].valueletter)
            word.append(board.grid[int(row)][int(column)])
            board.calculate_cell_value(board.grid[int(row)][int(column)])
            #Hacer a word una lista de celdas para poder calculate word value
            si = str(input("Quiere agregar letra? Y/N: "))
        return word

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

            
                