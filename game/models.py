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
        print(elec)
        print(self.tiles[elec].cant)
        (self.actualizado[elec].cant) -= 1
        print(self.actualizado[elec].cant)
        return(elec)

    def put(self, letra):
        if self.actualizado[letra].cant < self.tiles[letra].cant:
            (self.actualizado[letra].cant) += 1
            print(self.actualizado[letra].cant)


bag = BagTiles()
print(bag.take())

class Player():
    def __init__ (self):
        self.tiles = []
    def repartidas(self):
        self.tiles.append(bag.take())


player = Player()


class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]
            for _ in range(15)
        ]

        
#Celda en especifico, como agregarle un multiplicador a 1 celda en especifico
class Cell:
    def __init__(self, multiplayer, multiplayer_type):
        self.multiplayer = multiplayer
        self.multiplayer_type = multiplayer_type
        self.letter = None

    def add_letter(self, letter:Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplayer_type == 'letter':
            return self.letter.value * self.multiplayer
        else:
            return self.letter.value
    

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

#23 ago. 
