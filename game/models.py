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



bag = BagTiles()


class Player():
    def __init__ (self):
        self.tilesp = []
        self.name = ""
        self.score = 0
        self.estado = "jugando"
        self.tilesp.append(bag.take())
        self.tilesp.append(bag.take())
        self.tilesp.append(bag.take())
        self.tilesp.append(bag.take())
        self.tilesp.append(bag.take())
        self.tilesp.append(bag.take())
        self.tilesp.append(bag.take())

    def tiles_cambiadas(self):
        letter = random.choice(list(self.tilesp)) #Que no sea random choice, que sea una letra elegida por usuario
        self.tilesp.pop(bag.put(letter))
        self.tilesp.append(bag.take())
    def cambio_estado(self, other_player):
        player_1 = Player()
        if len(self.tilesp) == 0:
            self.estado = "terminado"
        if self.score > player_1.score: #Que compare con todos los otros jugadores, no uno
            self.estado = "ganando"

player = Player()


class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]
            for _ in range(15)
        ]

        
#Celda en especifico, como agregarle un multiplicador a 1 celda en especifico
class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.letter = None
        self.value = None
        self.used = False

    def add_letter(self, letter:Tile):
        self.letter = letter

    def multiplier_value(self, letter: Tile):
        if self.used == False:
            if self.row == 3 and self.column == 5:
                self.value = 2 * letter.value
                self.used = True  
            else:
                self.value = letter.value
        else:
            self.value = letter.value 
board = Board()

class ScrabbleGame():
    def __init__(self, players_count):
        self.board = Board()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player())

#20 ago. Agregamos valor y cant a cada letra. Vimos como acceder a ellos. 
#Metodo para restar cantidad cuando se saca una letra

#21 ago. Hacer funcion para agregar letras. Agregamos diccionario de actualizados

#23 ago. Creacion 
