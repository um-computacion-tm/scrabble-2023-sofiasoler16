import random
import unittest
import io
from unittest.mock import patch, call
from io import StringIO


from game.models import *
from game.player import *
from game.cell import *
from game.board import *
from game.word import *


from unittest.mock import patch


# class Game(unittest.TestCase):

    # @patch('builtins.input', side_effect=["Y", "2", "3", "A", "N"])
    # def test_put_word(self, mock_output):
    #     board = Board()

    #     board.put_word()
    #     self.assertEqual(board.grid[2][3].valueletter, "A")

class TestTiles(unittest.TestCase):
    def test_tile_valueycantA(self):
        tile = Tile('A',1, 12)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.cant, 12)
        self.assertEqual(tile.value, 1)

class TestBag(unittest.TestCase):
    @patch("random.choice",return_value = "A")
    def test_bag_tilesA(self, patch_choice):
        bag = BagTiles()
        self.assertEqual(
            bag.tiles["A"].cant,
            12,
        )
        bag.take()
        self.assertEqual(
            bag.tiles["A"].cant,
            11,
        )

        bag.put_in_bag("A")
        self.assertEqual(
            bag.tiles["A"].cant, 12
        )

#Este test saca y despues agrega
#Test para que pasaria si intento agregar algo que ya esta en maximo


class TestBag2(unittest.TestCase):
    @patch("random.choice",return_value = "C")
    def test_bag_tilesC(self, patch_choice):
        bag = BagTiles()
        self.assertEqual(
            bag.tiles["C"].cant,
            4,
        )
        bag.take()
        self.assertEqual(
            bag.tiles["C"].cant,
            3,
        )
        bag.take()
        bag.take()

        bag.put_in_bag("C")
        self.assertEqual(
            bag.tiles["C"].cant, 2
        )



class TestPlayer(unittest.TestCase):
    def test_init(self):
        bag = BagTiles()
        player_1 = Player(bag)
        self.assertEqual(
        len(player_1.tilesp),7
        )

        self.assertEqual(
            player_1.score, 0 
        )
        self.assertEqual(
            player_1.player_estado, "jugando"
        )
    @patch('builtins.print')
    @patch('builtins.input', return_value = "A")
    def test_cambiadas(self, patched_print, mock_input):
        #Hacer un test para la funcion tile_cambiadas que no imprima los print?
        bag = BagTiles()
        player_1 = Player(bag)

        player_1.tilesp = ["A", "B", "C", "D", "E", "F", "G"]
        player_1.tiles_cambiadas()

        self.assertEqual(
            len(player_1.tilesp),7
        )

    def test_cambio_estado_tilesp_empty(self):
        bag = BagTiles()
        player_1 = Player(bag)
        player_2 = Player(bag)
        player_1.score = 10
        player_2.score = 20  

        player_1.tilesp = []  # Simular que tilesp está vacío
        player_1.winning_player([player_1, player_2])
        self.assertEqual(player_1.player_estado, "terminado")

    def test_winner(self):
        bag = BagTiles()
        player_1 = Player(bag)
        player_2 = Player(bag)

        player_1.score = 10
        player_2.score = 20   

        player_1.winning_player([player_1, player_2])
        player_2.winning_player([player_1, player_2])

        self.assertEqual(
            player_2.player_estado, "ganando"
            )
        
    def test_score_player_2_words_con_multiplier(self):
        bag = BagTiles()
        player = Player(bag)
        board = Board()

#Primera palabra
        cell = Cell(2,5)
        letter = Tile(letter="A", value=1, cant=12)
        cell.add_letter(letter)
        board.calculate_cell_value(cell)

        cell1 = Cell(2,6)
        letter = Tile(letter="B", value=3, cant=2)
        cell1.add_letter(letter)
        board.calculate_cell_value(cell1)

        cell2 = Cell(2,7)
        letter = Tile(letter="A", value=1, cant=12)
        cell2.add_letter(letter)
        board.calculate_cell_value(cell2)

        word = Word()
        word.calculate_word_value([cell, cell1, cell2])

        wordvalue = word.wordvalue

        player.score_player(wordvalue)
#Segunda palabra
        cell3 = Cell(7,6)
        letter = Tile(letter="A", value=1, cant=12)
        cell3.add_letter(letter)
        board.calculate_cell_value(cell3)

        cell4 = Cell(8,6)
        letter = Tile(letter="B", value=3, cant=2)
        cell4.add_letter(letter)
        board.calculate_cell_value(cell4)

        cell5 = Cell(9,6)
        letter = Tile(letter="A", value=1, cant=12)
        cell5.add_letter(letter)
        board.calculate_cell_value(cell5)

        word = Word()
        word.calculate_word_value([cell3, cell4, cell5])

        wordvalue = word.wordvalue

        player.score_player(wordvalue)

        self.assertEqual(player.score, 16)
        
    def test_validate_letter(self):
        bag = BagTiles()
        player1 = Player(bag)
        scrabble = ScrabbleGame(4)
        board = Board()
        player1.tilesp = [
            "H",
            "O",
            "A",
            "A",
            "S",
            "B",
            "C",
        ]

        cell3 = Cell(7,7)
        letter1 = Tile(letter="A", value=1, cant=12)
        cell3.add_letter(letter1)
        board.calculate_cell_value(cell3)

        cell4 = Cell(7,8)
        letter2 = Tile(letter="B", value=3, cant=2)
        cell4.add_letter(letter2)
        board.calculate_cell_value(cell4)

        cell5 = Cell(7,9)
        letter3 = Tile(letter="A", value=1, cant=12)
        cell5.add_letter(letter3)
        board.calculate_cell_value(cell5)
        scrabble.already_board_cell = [cell3, cell4, cell5]
        word = Word()
        word.calculate_word_value([cell3, cell4, cell5])

        wordvalue = word.wordvalue

        player1.score_player(wordvalue)

        self.assertEqual(player1.score, 12)

        self.assertEqual(player1.has_letters_always([letter1, letter2, letter3], scrabble), True)
        


class TestBoard(unittest.TestCase):

    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )
    def test_out_of_board(self):
        board = Board()
        word = "FACULTAD"
        location = (14,4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == False

    def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        word = "FACULTAD"
        location = (7,4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == True

    def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        word = "FACULTAD"
        location = (8,9)
        orientation ="V"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == False

    def test_place_word_empty_board_vertical_fine(self):
        board = Board()
        word = "FACULTAD"
        location = (7,4)
        orientation = "V"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == True
    
    def test_empty_board(self):
        board = Board()

        board.grid[7][7].add_letter(Tile("Q",5,1))

        self.assertEqual(board.validate_empty_board(board.grid[7][7]), False)

    def test_not_empty_board(self):
        board = Board()

        board.grid[6][7].add_letter(Tile("Q",5,1))

        self.assertEqual(board.validate_empty_board(board.grid[7][7]), True)

    def test_multiplier_dobleletter(self):
        board = Board()
        cell = Cell(12,1)
        letter = Tile(letter="A", value=1, cant=12)
        cell.add_letter(letter)
        board.calculate_cell_value(cell)
        self.assertEqual(
            cell.value, 2
        )

    def test_multiplier_triplletter(self):
        board = Board()
        cell = Cell(10,2)
        letter = Tile(letter="A", value=1, cant=12)
        cell.add_letter(letter)
        board.calculate_cell_value(cell)
        self.assertEqual(
            cell.value, 3
        )

    def test_value_segundavez_double(self):
        board = Board()
        cell = Cell(row=4, column=1)
        letter = Tile("A",1,12)
        cell.add_letter(letter)

        board.calculate_cell_value(cell)
        self.assertEqual(
            cell.value,2
        )
        cell.used = True  
        board.calculate_cell_value(cell)
        self.assertEqual(
            cell.value,1
        )
    def test_value_segundavez_triple(self):
        board = Board()
        cell = Cell(row=10, column=2)
        letter = Tile("A",1,12)
        cell.add_letter(letter)

        board.calculate_cell_value(cell)
        self.assertEqual(
            cell.value,3
        )
        cell.used = True  
        board.calculate_cell_value(cell)
        self.assertEqual(
            cell.value,1
        )
    @patch('sys.stdout', new_callable=StringIO)
    def test_show_board(self, mock_output):
        board = Board()
        board.show_board()

    def test_calculate_word_value_board(self):
        board = Board()
        word = Word()

        board.grid[3][1].add_letter(Tile('A',1,12))
        board.grid[3][2].add_letter(Tile('B',3,2))
        board.grid[3][3].add_letter(Tile('A',1,12))

        board.grid[4][3].add_letter(Tile('V',1,12))
        board.grid[5][3].add_letter(Tile('I',3,2))
        board.grid[6][3].add_letter(Tile('O',1,12))
        board.grid[7][3].add_letter(Tile('N',1,12))


        board.calculate_cell_value(board.grid[3][1])
        board.calculate_cell_value(board.grid[3][2])      
        board.calculate_cell_value(board.grid[3][3])

        word.calculate_word_value([board.grid[3][1],board.grid[3][2],board.grid[3][3]])

        board.calculate_cell_value(board.grid[3][3])
        board.calculate_cell_value(board.grid[4][3])
        board.calculate_cell_value(board.grid[5][3])      
        board.calculate_cell_value(board.grid[6][3])
        board.calculate_cell_value(board.grid[6][3])


        word.calculate_word_value([board.grid[3][3],board.grid[4][3],board.grid[5][3],board.grid[6][3]])
        self.assertEqual (word.wordvalue, 12)


    def test_adyacent_word(self):
        board = Board()
        word = Word()


        board.grid[3][1].add_letter(Tile('A',1,12))
        board.grid[3][2].add_letter(Tile('B',3,2))
        board.grid[3][3].add_letter(Tile('A',1,12))

        board.grid[4][3].add_letter(Tile('V',1,12))
        board.grid[5][3].add_letter(Tile('I',3,2))
        board.grid[6][3].add_letter(Tile('O',1,12))
        board.grid[7][3].add_letter(Tile('N',1,12))

        board.grid[4][3].row

        print()

        self.assertEqual(board.validate_connected_word3([board.grid[3][3],board.grid[4][3],board.grid[5][3],board.grid[6][3],board.grid[7][3]])
                        , True)
    
    @patch ('builtins.print')
    def test_adyacent_word_false(self, patched_print):
        board = Board()

        board.grid[3][1].add_letter(Tile('A',1,12))
        board.grid[3][2].add_letter(Tile('B',3,2))
        board.grid[3][3].add_letter(Tile('A',1,12))

        board.grid[5][7].add_letter(Tile('A',1,12))
        board.grid[6][7].add_letter(Tile('B',3,2))
        board.grid[7][7].add_letter(Tile('A',1,12))

        self.assertEqual(board.validate_connected_word3([board.grid[3][1],board.grid[3][2],board.grid[3][3]])
                        , False)
        self.assertEqual(board.grid[3][2].valueletter, None)



class TestCell(unittest.TestCase):
    def _init_cell(self):
        cell = Cell(5, 7)
        self.assertEqual(
            cell.value, 1
        )

    def test_add_letter(self):
        cell = Cell(row=5, column=5)
        letter = Tile(letter="A", value=1, cant=12)

        cell.add_letter(letter=letter)
        self.assertEqual(cell.letter, letter)

    def test_value_normal(self):
        board = Board()
        cell = Cell(row=4, column=7)
        letter = Tile(letter="Q", value=5, cant=1)
        cell.add_letter(letter)
        board.calculate_cell_value(cell)

        cell1 = Cell(row=4, column=8)
        board.calculate_cell_value(cell1)

        self.assertEqual(
            cell.value,5
        )
        self.assertEqual(
            cell1.value, 0
        )

class TestCli(unittest.TestCase):
    @patch('builtins.input', return_value="2")  # Simulo la entrada de usuario
    def test_init(self, mock_input):
        cli = Cli()
        
        self.assertIsNotNone(cli.scrabble)


class TestScrabbleGame(unittest.TestCase):

    @patch ('builtins.input', return_value = ["Y", "Y", 7, 7, "A", "N"])
    @patch ('builtins.print')
    def test_firs_turn(self, mock_output, patched_print):
        scrabbl = ScrabbleGame(3)
        scrabbl.iniciate_turn()

    # @patch ('builtins.print')
    # @patch ('builtins.input', return_value = ["Y", "Y", 7, 7, "A", "N"])
    # def test_first_turn(self, patched_print, mock_output):
    #     player_acount = 4
    #     scrabble = ScrabbleGame(player_acount)
    #     scrabble.next_turn()

    #     scrabble.first_turn()
    #     self.assertEqual(scrabble.player_index, 0)

    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag)

    def test_game_over(self):
        scrabble_game = ScrabbleGame(players_count=3)
        bag = BagTiles()
        scrabble_game.next_turn()
        scrabble_game.current_player.tilesp = []

        scrabble_game.players[0].winning_player(scrabble_game.players)

        scrabble_game.end_game()
        self.assertEqual(scrabble_game.game_state, "over")


    def test_next_turn_when_game_is_starting(self):
        scrabble_game = ScrabbleGame(players_count=3)

        scrabble_game.next_turn()

        assert scrabble_game.current_player == scrabble_game.players[0]
    def test_next_turn_when_player_is_not_the_first(self):
        scrabble_game = ScrabbleGame(players_count=3)

        scrabble_game.current_player = scrabble_game.players[0]

        scrabble_game.next_turn()
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[2]

    def test_next_turn_when_player_is_last(self):
        #Suponiendo que tenemos 3 jugadores, luego del jugador 3, le toca al jugador 1
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]

        scrabble_game.next_turn()

        assert scrabble_game.current_player == scrabble_game.players[0]

    @patch('builtins.input', return_value='2')
    @patch('builtins.print')
    def test_start(self, mock_output, patched_print):
        #Testea que pregunte cant players, y empiece en el player 0
        main = Main()

        main.get_player_acount()
        self.assertEqual(main.player_count, 2)

        scrabble = ScrabbleGame(main.player_count)

        scrabble.next_turn()
        self.assertEqual(scrabble.current_player, scrabble.players[0])

        scrabble.game_started()
        self.assertEqual(scrabble.game_state, "ongoing")


    # def test_play_word(self):
    #         # Configura el juego y el jugador
    #     scrabble_game = ScrabbleGame(players_count=1)
    #     player = scrabble_game.players[0]
    #     player.tilesp = [Tile('H', 1), Tile('O', 1), Tile('L', 1), Tile('A', 1)]
    #     valid_word = "HOLA"
    #     self.assertTrue(scrabble_game.play_word(valid_word, player.tiles))
    #     invalid_word = "MALO"
    #     with self.assertRaises(Not_Letters_Exception):
    #         scrabble_game.play_word(invalid_word, player.tiles)

# class TestClI(unittest.TestCase):

    # @patch('builtins.input', return_value='3')
    # def test_get_player_count(self, input_patched):
    #     cli = Cli()
    #     self.assertEqual(
    #         cli.ask_player_count(),
    #         3,
    #     )

    # @patch('builtins.print')
    # @patch('builtins.input', side_effect=['A', '3'])
    # def test_get_player_count_wrong_input(self, input_patched, print_patched):
    #     cli = Cli()
    #     self.assertEqual(
    #         cli.ask_player_count(),
    #         3,
    #     )

    # @patch('builtins.print')
    # @patch('builtins.input', side_effect=['10', '1'])
    # def test_get_player_count_control_max(self, input_patched, print_patched):
    #     cli = Cli()
    #     self.assertEqual(
    #         cli.ask_player_count(),
    #         1,
    #     )


class TestMain(unittest.TestCase):
    def setUp(self):
        self.main = Main()

    @patch('builtins.input', return_value='3')
    @patch('builtins.print')
    def test_get_player_account_with_3(self, patched_print, mock_output):
        main = Main()
        main.get_player_acount()
        self.assertEqual(patched_print.call_args_list, [call("Good")])


    # @patch('builtins.input', return_value='4')  # Ingresamos un valor fuera del rango
    # @patch('sys.stdout', new_callable=io.StringIO)
    # def test_get_player_account_with_invalid_input(self, mock_stdout, mock_input):
    #     main = Main()
    #     main.get_player_acount()
    #     printed_output = mock_stdout.getvalue()
    #     self.assertEqual("Error, enter a valid number between 1 and 3", printed_output)

    # def test_invalid_input(self):
    #     main = Main()
    #     with patch('builtins.input', side_effect=["5", "1", "0", "abc"]):
    #         main.get_player_acount()
    #     self.assertEqual(main.player_count, 1)




class TestWord(unittest.TestCase):

    def test_word_value_con_multiplier_letter(self):
        board = Board()
        cell = Cell(2,5)
        letter = Tile(letter="A", value=1, cant=12)
        cell.add_letter(letter)
        board.calculate_cell_value(cell)

        cell1 = Cell(2,6)
        letter = Tile(letter="B", value=3, cant=2)
        cell1.add_letter(letter)
        board.calculate_cell_value(cell1)

        cell2 = Cell(2,7)
        letter = Tile(letter="A", value=1, cant=12)
        cell2.add_letter(letter)
        board.calculate_cell_value(cell2)

        word = Word()
        word.calculate_word_value([cell, cell1, cell2])
        self.assertEqual(word.wordvalue, 11)
    
    def test_word_value_con_word_multiplierx3(self):
        board = Board()
        cell = Cell(2,2)
        letter = Tile(letter="A", value=1, cant=12)
        cell.add_letter(letter)
        board.calculate_cell_value(cell)

        cell1 = Cell(2,3)
        letter = Tile(letter="B", value=3, cant=2)
        cell1.add_letter(letter)
        board.calculate_cell_value(cell1)

        cell2 = Cell(2,4)
        letter = Tile(letter="A", value=1, cant=12)
        cell2.add_letter(letter)
        board.calculate_cell_value(cell2)

        word = Word()
        word.calculate_word_value([cell, cell1, cell2])
        self.assertEqual(word.wordvalue, 10)

    def test_word_value_con_word_multiplierx2(self):
        board = Board()
        cell = Cell(1,1)
        letter = Tile(letter="A", value=1, cant=12)
        cell.add_letter(letter)
        board.calculate_cell_value(cell)

        cell1 = Cell(1,2)
        letter = Tile(letter="B", value=3, cant=2)
        cell1.add_letter(letter)
        board.calculate_cell_value(cell1)

        cell2 = Cell(1,3)
        letter = Tile(letter="A", value=1, cant=12)
        cell2.add_letter(letter)
        board.calculate_cell_value(cell2)

        word = Word()
        word.calculate_word_value([cell, cell1, cell2])
        self.assertEqual(word.wordvalue, 15)
    @patch('builtins.print')
    def test_remove_invalid_word(self, patched_print):
        board = Board()
        cell = Cell(2,5)
        letter = Tile(letter="A", value=1, cant=12)
        cell.add_letter(letter)
        board.calculate_cell_value(cell)

        cell1 = Cell(2,6)
        letter = Tile(letter="B", value=3, cant=2)
        cell1.add_letter(letter)
        board.calculate_cell_value(cell1)

        cell2 = Cell(2,7)
        letter = Tile(letter="C", value=1, cant=12)
        cell2.add_letter(letter)
        board.calculate_cell_value(cell2)

        word = Word()
        word.calculate_word_value([cell, cell1, cell2])
        self.assertEqual(word.wordvalue, 0)

        self.assertEqual(cell.letter, None)
        self.assertEqual(cell1.letter, None)
        self.assertEqual(cell2.letter, None)
"""
    def test_1letter_word(self):
        cell = Cell(2,5)
        letter = Tile(letter="C", value=1, cant=4)
        cell.add_letter(letter)
        cell.multiplier_value()

        cell1 = Cell(2,6)
        cell1.multiplier_value()

        word = Word()
        word.calculate_word_value(cell)
        
        self.assertEqual(word.wordvalue, 1)
"""




class TestDictionary(unittest.TestCase):
    def test_word_in_dictionary(self):
        dictionary = Dictionary("dictionaries/dictionary .txt")
        self.assertEqual(dictionary.valid_word('arbol'), True)
    def test_word_not_dictionary(self):
        dictionary = Dictionary("dictionaries/dictionary .txt")
        self.assertEqual(dictionary.valid_word('schmolicnsd'), False)    


if __name__ == '__main__':
    unittest.main()