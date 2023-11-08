
from game.cell import Cell
from game.dictionary import Dictionary
from game.board import Board
#NO puedo hacer commit
class Word():
    def __init__(self):
        self.wordvalue = 0
        self.multiplier = 1
        self.multiplier_used = False
        self.existing_word = None
    
    def calculate_word_value(self, wordplace: list[Cell]): #Suma el puntaje de una palabra
        self.wordcell = []
        self.listpalabra = []
        self.doubleword = [Cell(1, 1), Cell(8, 1), Cell(15, 1), Cell(2, 2), Cell(14, 2), Cell(3, 3), Cell(13, 3), Cell(4, 4), 
                      Cell(12, 4), Cell(7, 7), Cell(11, 7), Cell(4, 12), Cell(12, 12), Cell(1, 15), Cell(8, 15), Cell(15, 15)]
        self.tripleword = [Cell(1, 2), Cell(8, 1), Cell(0, 0), Cell(7, 0), Cell(14, 0), Cell(0, 7), Cell(14, 7), Cell(0, 14), Cell(7, 14), Cell(14, 14)]

        self.multi(wordplace)

        palabramayus = "".join(self.listpalabra) #Se fija si la palabra existe antes de sumar puntaje
        palabraminus = palabramayus.lower()
        dictionary = Dictionary("dictionaries/dictionary .txt") #Hasta aca verifica

        if palabraminus in dictionary.words:
            for cell in wordplace:
                self.wordcell.append(cell.value)
            self.existing_word = True
        else: #Si palabra no en diccionario, remueve la palabra
            print("-----  PALABRA NO EXISTE. Su palabra no fue asignada al tablero -----")
            for cell in wordplace:
                cell.remove_letter()
                self.existing_word = False
            

        self.wordvalue = (sum(self.wordcell))*self.multiplier
        return self.wordvalue
    
    def multi(self, wordplace: list[Cell]):
        for cell in wordplace:
            self.listpalabra.append(cell.valueletter)
            self.calculate_multiplier(cell)

    def calculate_multiplier(self, cell: Cell):
        for doublecell in self.doubleword:
            if cell.row == doublecell.row and cell.column == doublecell.column:
                self.multiplier = 2
                return  # Una vez que se encuentra un multiplicador, no es necesario seguir buscando

        for triplecell in self.tripleword:
            if cell.row == triplecell.row and cell.column == triplecell.column:
                self.multiplier = 3
                return  

        
    