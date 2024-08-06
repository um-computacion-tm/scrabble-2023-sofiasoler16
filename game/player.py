
from game.tile import BagTiles, Tile
from game.board import Board
from game.word import Word
from game.cell import Cell

class Not_Letters_Exception(Exception):
    pass

class Player():
    def __init__ (self,bag:BagTiles):
        self.tilesp = []
        self.bag = bag
        self.index = 0
        self.score = 0
        self.player_estado = "jugando"
        self.current_word_value = 0
        

        for _ in range(7):
            self.tilesp.append(self.bag.take())
#Como testeo que resta la cantidad de letras tambien para el siguiente jugador?
        self.current_player = None

    def tiles_cambiadas(self):
        print(self.tilesp)
        a = True
        while a == True:
            try:
                letterchoice = str(input("Ingrese letra para devolver (en mayuscula): "))
                if letterchoice in self.tilesp:
                    self.tilesp.remove(letterchoice)
                    self.bag.put_in_bag(letterchoice)
                    self.tilesp.append(self.bag.take())
                    a = False
                else:
                    raise ValueError("No puede intercambiar letras que no tiene")
            except ValueError as error:
                print("NO puede intercambiar letras que no tiene")
        print("Sus nuevas letras son: ", self.tilesp)

    def winning_player(self,all_players):

        for player in all_players:
            if len(self.tilesp) == 0:
                self.player_estado = "terminado"
                
            player:Player
            if self.score > player.score:
                self.player_estado = "ganando"
            elif self.score < player.score: #No marca que esta perdiendo, lo deja en jugando
                player.player_estado = "perdiendo"

    def put_word_first(self, board:Board, bag:BagTiles, word:Word):
        board.show_board()
        
        self.new(bag,board)
        word.calculate_word_value(self.cell_wordlist)
        if self.has_letters_first(self.word_tiles, self.cell_wordlist) == True and word.existing_word == True:
            self.current_word_value = word.calculate_word_value(self.cell_wordlist)
                
            print("el valor de la palabra es: ", self.current_word_value)
            board.validate_empty_board(board.grid[7][7])
            for letter in self.word_tiles:
                self.tilesp.remove(letter.letter)
            

        board.show_board()

    def put_not_first_word(self, board:Board, bag:BagTiles, word:Word, scrabble):
        board.show_board()
        scrabble:ScrabbleGame
        self.new(bag,board)
        word.calculate_word_value(self.cell_wordlist)
        if self.has_letters_always(self.word_tiles, self.cell_wordlist, scrabble) == True:
            if board.validate_connected_word3(self.cell_wordlist, scrabble) == True and word.existing_word == True:
                self.current_word_value= word.calculate_word_value(self.cell_wordlist)
                print("el valor de la palabra es: ", self.current_word_value)
                for letter in self.word_tiles:
                    if letter.letter in self.tilesp:
                        self.tilesp.remove(letter.letter)

            elif board.validate_connected_word3(self.cell_wordlist, scrabble) == False:
                print("-----  PALABRA NO CONECTADA. Su palabra no fue asignada al tablero -----")

        board.show_board()

    def new(self, bag:BagTiles, board:Board):
        si = str(input("Quiere agregar letra? Y/N: "))
        self.cell_wordlist = []
        self.current_word_value = 0
        self.word_tiles =[]
        while si == "Y":
            row = input("Ingrese fila: ")
            column = input("Ingrese columna: ")
            letter = input("Ingrese letra a agregar: ")
            print("la tile es: ", bag.tiles[letter])
            z = bag.tiles[letter]
            self.word_tiles.append(z)
            board.grid[int(row)][int(column)].add_letter(bag.tiles[letter])
            self.cell_wordlist.append(board.grid[int(row)][int(column)])
            board.calculate_cell_value(board.grid[int(row)][int(column)])
            si = str(input("Quiere agregar letra? Y/N: "))
        
    def show_tiles(self):
        return self.tilesp

    def score_player(self, wordvalue): 
        self.current_word_value = 0
        player_word_score = 0
        self.words = []

        player_word_score += (wordvalue)
        self.score += (player_word_score)
    
    def has_letters_always(self, tiles:list[Tile], wordplace:list[Cell], scrabble):
        scrabble:ScrabbleGame
        
        for letter in tiles:
            for cell in scrabble.already_board_cell:
                if letter.letter in self.tilesp:
                    return True
                elif letter.letter not in self.tilesp and letter.letter == cell.valueletter:
                    print('Esta usando letras de otra palabra')
                    return True
                else: 
                    print("-----  NO TIENE LAS LETRAS. Su palabra no fue asignada al tablero -----")
                    for cell in wordplace:
                        cell.remove_letter()
                    return False
                    #         for cell in wordplace:
                    #     for already_cell in scrabble.already_board_cell:
                    #         if cell in wordplace and already_cell == cell:
                    #             cell.remove_letter()
                    # return False
            
    def has_letters_first(self, tiles:list[Tile], wordplace: list[Cell]):
        
        for letter in tiles:
                if letter.letter in self.tilesp:
                    return True
                else:
                    print("-----  NO TIENE LAS LETRAS. Su palabra no fue asignada al tablero -----")
                    for cell in wordplace:
                        cell.remove_letter()
                    
                        return False


            
                