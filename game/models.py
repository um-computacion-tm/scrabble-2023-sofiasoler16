import random

class YaHaySuficientes(Exception):
    pass

class Tile:
    def __init__(self, letter, value, cant):
        self.letter = letter
        self.value = value
        self.cant = cant

class BagTiles:
    def __init__(self):
        self.tiles = {"A":Tile("A",1,12), "B":Tile("B",3,2), "C":Tile("C",3,4), "D":Tile("D",2,5), "E":Tile("E",1,12),
                    "F": Tile("F",4,1), "G":Tile("G",2,2), "H":Tile("H",4,2), "I":Tile("I",1,6), "J":Tile("J",8,1),
                    "L":Tile("L",1,4), "M":Tile("M",3,2), "N":Tile("N",1,5), "Ñ":Tile("Ñ",8,1), "O":Tile("O",1,9),
                    "P":Tile("P",3,2), "Q":Tile("Q",5,1), "R":Tile("R",1,5), "S":Tile("S",1,6), "T":Tile("T",1,4),
                    "U":Tile("U",1,5), "V":Tile("V",4,1), "X":Tile("X",8,1), "Y":Tile("Y",4,1), "Z":Tile("Z",10,1),
                    "LL":Tile("LL",8,1), "RR":Tile("RR",8,1)
                    }
        self.actualizado = {"A":Tile("A",1,12), "B":Tile("B",3,2), "C":Tile("C",3,4), "D":Tile("D",2,5), "E":Tile("E",1,12),
                    "F": Tile("F",4,1), "G":Tile("G",2,2), "H":Tile("H",4,2), "I":Tile("I",1,6), "J":Tile("J",8,1),
                    "L":Tile("L",1,4), "M":Tile("M",3,2), "N":Tile("N",1,5), "Ñ":Tile("Ñ",8,1), "O":Tile("O",1,9),
                    "P":Tile("P",3,2), "Q":Tile("Q",5,1), "R":Tile("R",1,5), "S":Tile("S",1,6), "T":Tile("T",1,4),
                    "U":Tile("U",1,5), "V":Tile("V",4,1), "X":Tile("X",8,1), "Y":Tile("Y",4,1), "Z":Tile("Z",10,1),
                    "LL":Tile("LL",8,1), "RR":Tile("RR",8,1)
                    }
    def take(self):
        letras = list(self.tiles.keys())
        elec = random.choice(letras)
        (self.actualizado[elec].cant) -= 1
        return(elec)

    def put(self, letra):
        if self.actualizado[letra].cant < self.tiles[letra].cant:
            (self.actualizado[letra].cant) += 1

class Dictionary:
    def __init__(self, file_path):
        self.words = self.load_words(file_path)

    def load_words(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return set(word.strip() for word in file)

    def valid_word(self, word):
        if word in self.words:
            return True
        else:
            return False

class ScrabbleGame():
    def __init__(self, players_count):
        self.board = Board()
        self.bag = BagTiles()
        self.players = []
        self.current_player = None
        self.player_index = 0
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


"""     
        if self.score > player_1.score: #Que compare con todos los otros jugadores, no uno
            self.estado = "ganando"
"""


#Celda en especifico, como agregarle un multiplicador a 1 celda en especifico
class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.letter = None
        self.valueletter = None
        self.value = 0
        self.used = False

    def add_letter(self, letter:Tile):
        self.letter = letter
        self.valueletter = letter.letter

    def multiplier_value(self, usecell):
 #Mismo problema que player, no puedo llamar a un atributo que sea otra celda dentro de Cell?
        celldoble = [Cell(4,1), Cell(12,1)]
        if self.letter != None: #No puedo hacer una lista de lugares para usarlos en las posibles casillas?
            if self.used == False:
                #Casillas de doble letra
                for liscell in celldoble:
                    print(liscell.row, liscell.column)
                    print(usecell) #compara con el lugar de usecell, no con la celda que esta en usecell
                    if liscell == usecell:
                        self.value = 2 * self.letter.value
                        self.used = True
                    else:
                        self.value = self.letter.value
                else:
                    self.value = self.letter.value

class Main(): #Te deja entrar cantidad de jugadores y verifica que sea bueno
    def __init__(self):
        self.status_players = "valid"
        self.player_count = 0
        self.status_word = None
        self.board = Board()
        self.cell = Cell(None, None)
    
    def main(self):
        if self.player_count <= 1 or self.player_count > 4:
            self.status_players = "invalid"  
        self.status_players = "valid"


class Word():
    def __init__(self):
        self.wordvalue = 0
    
    def calculate_word_value(self, wordplace: list[Cell]): #Suma el puntaje de una palabra
        wordcell = []
        listpalabra = []
        for cell in wordplace: #Se fija si la palabra existe antes de sumar puntaje
            listpalabra.append(cell.valueletter)
        palabramayus = "".join(listpalabra)
        palabraminus = palabramayus.lower()
        dictionary = Dictionary("dictionaries/dictionary .txt")

        if palabraminus in dictionary.words:
            for cell in wordplace:
                wordcell.append(cell.value)

        self.wordvalue = sum(wordcell)
#Intentar arreglar la vieja para poder automatizar el proceso
"""
    def calculate_word_value(self, cell:Cell):
        wordcell = []
        
        while cell.value != 0:
            print(cell.value)
            wordcell.append(cell.value)
            print(cell.column)
            cell.column = (cell.column + 1)
            print(cell.column)
            print(cell.row, cell.column)
            print(cell.value)
            if cell.value == 0:
                break
        if len(wordcell) > 0:
            self.wordvalue = sum(wordcell)
            return self.wordvalue 
        else: 
            return self.wordvalue
"""
        

class Board:
    def __init__(self):
        self.status = "empty"
        self.grid = [
            [ Cell("", "") for _ in range(15) ]
            for _ in range(15)
        ]

    def validate_word_inside_board(self, word, location, orientation):
        position_x = location[0]
        position_y = location[1]
        len_word = len(word)
        if orientation == "H":
            if position_x + len_word > 15:
                return False
            else:
                return True
        elif orientation == "V":
            if position_y + len_word > 15:
                return False
            else:
                return True
            
    def validate_empty_board(self, center_cell:Cell):
        #if center_cell == Cell(7,7):

        if center_cell.letter != None:
            self.status = "not empty"

class Player():
    def __init__ (self,bag:BagTiles):
        self.tilesp = []
        self.bag = bag
        self.name = ""
        self.score = 0
        self.estado = "jugando"
        for _ in range(7):
            self.tilesp.append(self.bag.take())

        self.current_player = None

    def tiles_cambiadas(self, letterchoice:Tile):
        letter = letterchoice #Que no sea random choice, que sea una letra elegida por usuario
        self.tilesp.pop(self.bag.put(letter))
        self.tilesp.append(self.bag.take())

    def cambio_estado(self, other_player):
        other_player = Player(BagTiles())
        if len(self.tilesp) == 0:
            self.estado = "terminado"

    def score_player(self, wordvalue): 
        player_word_score = 0
        self.words = []

        player_word_score += (wordvalue)
        self.score += (player_word_score)
    
    def has_letters(self, tiles:list[Tile]):
        self.valid = True
        
        for letter in tiles:
            if letter.letter in self.tilesp:
                self.valid = True
            else:
                self.valid = False
                break
                




