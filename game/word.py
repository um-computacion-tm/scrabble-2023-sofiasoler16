
from game.cell import *
from game.models import *
from game.dictionary import *

cell= Cell
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
        