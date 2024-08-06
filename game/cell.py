from game.tile import Tile

class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.letter = None
        self.valueletter = None
        self.value = 0
        self.used = False
        

    def get_value_for_board(self):
        self.celldouble = [(4,1), (12,1), (1, 4),(8, 4),(15, 4),(3, 7), (7, 7), (9, 7), 
                     (13, 7),(4, 10),(12, 10), (0, 12), (7, 12), (14, 12), (3, 15), (11, 15)]
        self.celltriple = [(6,2),(10,2), (6, 6), (10, 6), (14, 6), (1, 8), (5, 8), 
                      (9, 8), (13, 8), (2, 10), (6, 10), (10, 10), (14, 10), (6, 14), (10, 14)]
        self.doublewords = [(1, 1), (8, 1), (15, 1), (2, 2), (14, 2), (3, 3), (13, 3), (4, 4), 
                      (12, 4), (7, 7), (11, 7), (4, 12), (12, 12), (1, 15), (8, 15), (15, 15)]
        self.triplewords = [(0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14)]
        
        
        if self.letter is not None:
            return " " + self.letter.letter + " "

        if (self.row, self.column) in self.celldouble:
            return "Cx2"
        
        if (self.row, self.column) in self.celltriple:
            return "Cx3"
        

        return "   "
    
        
    def add_letter(self, letter:Tile):
        self.letter = letter

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
