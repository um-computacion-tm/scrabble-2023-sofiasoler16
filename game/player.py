
from game.tile import BagTiles, Tile
from game.models import *

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
        self.tilesp.pop(self.bag.put(letter))
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


    def score_player(self, wordvalue): 
        player_word_score = 0
        self.words = []

        player_word_score += (wordvalue)
        self.score += (player_word_score)
    
    def has_letters(self, tiles:list[Tile]):
        
        for letter in tiles:
            if letter.letter in self.tilesp:
                return True
            else:
                raise Not_Letters_Exception('Error, no tiene las letras')
                