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
class Cli():
    def __init__(self):
        pass
    def ask_player_count(self):
        while True:
            try:
                player_count = int(input('cantidad de jugadores (1-3): '))
                if player_count <= 3:
                    break
            except Exception as e:
                print('ingrese un numero por favor')
        return player_count
    
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
        self.show = " "

    def get_value_for_board(self):
        celldouble = [Cell(4,1), Cell(12,1), Cell(1, 4),Cell(8, 4),Cell(15, 4),Cell(3, 7), Cell(7, 7), Cell(9, 7), 
                     Cell(13, 7),Cell(4, 10),Cell(12, 10), Cell(0, 12), Cell(7, 12), Cell(14, 12), Cell(3, 15), Cell(11, 15)]
        celltriple = [Cell(6,2),Cell(10,2), Cell(2, 6), Cell(6, 6), Cell(10, 6), Cell(14, 6), Cell(1, 8), Cell(5, 8), 
                      Cell(9, 8), Cell(13, 8), Cell(2, 10), Cell(6, 10), Cell(10, 10), Cell(14, 10), Cell(6, 14), Cell(10, 14)]
        
        for cell in celldouble:
            if cell in celldouble:
                self.show = "Multi x2"
        
    def add_letter(self, letter:Tile):
        self.letter = letter
        self.show = letter.letter
        self.valueletter = letter.letter
    
    def remove_letter(self):
        self.letter = None
        self.valueletter = None
    

    # def multiplier_value(self):
    #     if self.letter != None:
    #         if self.used == False:
    #             if self.row == 4 and self.column == 1:
    #                 self.value = 2 * self.letter.value
    #                 self.used = True  
    #             else:
    #                 self.value = self.letter.value
    #         else:
    #             self.value = self.letter.value


        # def multiplier_value(self, column, row):
        #     if column==0 and row==0:
        #         self.multiplier_type='letter'
        #         self.value=2


class Main(): #Te deja entrar cantidad de jugadores y verifica que sea bueno
    def __init__(self):
        self.status_players = "valid"
        self.player_count = 0
        self.status_word = None
        self.board = Board()
        self.cell = Cell(None, None)
    #Hacer una funcion que pida el player_count
    def main(self):
        if self.player_count <= 1 or self.player_count > 4:
            self.status_players = "invalid"  
        self.status_players = "valid"


class Word():
    def __init__(self):
        self.wordvalue = 0
        self.multiplier = 1
        self.multiplier_used = False
    
    def calculate_word_value(self, wordplace: list[Cell]): #Suma el puntaje de una palabra
        wordcell = []
        listpalabra = []
        doubleword = [Cell(1, 1), Cell(8, 1), Cell(15, 1), Cell(2, 2), Cell(14, 2), Cell(3, 3), Cell(13, 3), Cell(4, 4), 
                      Cell(12, 4), Cell(7, 7), Cell(11, 7), Cell(4, 12), Cell(12, 12), Cell(1, 15), Cell(8, 15), Cell(15, 15)]
        tripleword = [Cell(1, 1), Cell(8, 1)]

        for cell in wordplace: 
            listpalabra.append(cell.valueletter)
            for doublecell in doubleword:
                if cell.row == doublecell.row and cell.column == doublecell.column:
                    self.multiplier = 2
                else:
                    for triplecell in tripleword:
                        if cell.row == triplecell.row and cell.column == triplecell.column:
                            self.multiplier = 3



        palabramayus = "".join(listpalabra) #Se fija si la palabra existe antes de sumar puntaje
        palabraminus = palabramayus.lower()
        dictionary = Dictionary("dictionaries/dictionary .txt") #Hasta aca verifica

        if palabraminus in dictionary.words:
            for cell in wordplace:
                wordcell.append(cell.value)
        else: #Si palabra no en diccionario, remueve la palabra
            for cell in wordplace:
                cell.remove_letter()

        self.wordvalue = (sum(wordcell))*self.multiplier

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
            [ Cell(row=row, column=column) 
            for row in range(15) ]
            for column in range(15)
        ]
    def show_board(board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))

        
        for row_index, row in enumerate(board.grid):
            print( str(row_index).rjust(2) + " | " + 
                  " ".join([repr(cell.show) for cell in row])
                  )
        

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

    def calculate_cell_value(self, usecell:Cell):
 #Mismo problema que player, no puedo llamar a un atributo que sea otra celda dentro de Cell?
        celldouble = [Cell(4,1), Cell(12,1), Cell(1, 4),Cell(8, 4),Cell(15, 4),Cell(3, 7), Cell(7, 7), Cell(9, 7), 
                     Cell(13, 7),Cell(4, 10),Cell(12, 10), Cell(0, 12), Cell(7, 12), Cell(14, 12), Cell(3, 15), Cell(11, 15)]
        celltriple = [Cell(6,2),Cell(10,2), Cell(2, 6), Cell(6, 6), Cell(10, 6), Cell(14, 6), Cell(1, 8), Cell(5, 8), 
                      Cell(9, 8), Cell(13, 8), Cell(2, 10), Cell(6, 10), Cell(10, 10), Cell(14, 10), Cell(6, 14), Cell(10, 14)]
        if usecell.letter != None: #No puedo hacer una lista de lugares para usarlos en las posibles casillas?
            if usecell.used == False:
                #Casillas de doble letra
                for liscell in celldouble:
                    if liscell.row == usecell.row and liscell.column == usecell.column:
                        usecell.value = 2 * usecell.letter.value
                        usecell.used = True
                        if usecell.used == True:
                            break
                    else:
                        for cell in celltriple:
                            if cell.row == usecell.row and cell.column == usecell.column:
                                usecell.value = 3 * usecell.letter.value
                                usecell.used = True
                                if usecell.used == True:
                                    break  
                        else:
                            usecell.value = usecell.letter.value
            else:
                usecell.value = usecell.letter.value

class Player():
    def __init__ (self,bag:BagTiles):
        self.tilesp = []
        self.bag = bag
        self.name = ""
        self.score = 0
        self.estado = "jugando"
        for _ in range(7):
            self.tilesp.append(self.bag.take())
#Como testeo que resta la cantidad de letras tambien para el siguiente jugador?
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
                




