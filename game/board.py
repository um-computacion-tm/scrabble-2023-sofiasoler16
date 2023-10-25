
from game.cell import *
from game.word import *
from game.models import *
from game.dictionary import *
from game.tile import *
class Board:
    def __init__(self):
        self.status = "empty"
        self.grid = [
            [ Cell(column=row, row=column) #Esta al revez porque si no lo imprime al
            for row in range(15) ]
            for column in range(15)
        ]
    def show_board(board):
        print('\n    |' + ''.join([f'   {str(row_index).rjust(2)} ' for row_index in range(15)]))

        
        for row_index, row in enumerate(board.grid):
            print( str(row_index).rjust(2) + "  | " + 
                " ".join([repr(cell.get_value_for_board()) for cell in row])
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
    
    def validate_connected_word(self, word:list[Cell]):
        #Ver si una celda, que NO sea una de las celdas de word de al rededor de cada celda esta vacia
        #Si no lo es, la palabra no se puede formar en el tablero
        for cell in word:
            print("la fila en def ", cell.row)
            adjacent_cells = [
                (cell.row - 1, cell.column),  # Arriba
                (cell.row + 1, cell.column),  # Abajo
                (cell.row, cell.column - 1),  # Izquierda
                (cell.row, cell.column + 1)   # Derecha
            ]
            for fila, columna in adjacent_cells:
                print("ahora es ", cell.valueletter)
                print("la celda adyacente es fila ", Cell(fila,columna).row)
                print("la celda palabra fila: ", cell.row)
                if Cell(fila,columna).row != cell.row or Cell(fila,columna).column != cell.column:
                    print("finalmente es", cell.letter)
                    if (cell.valueletter != None):
                        return True  # Al menos una celda adyacente está ocupada
                    else:
                        
                        return False
                    

                    

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
                        #Casillas de triple letra
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