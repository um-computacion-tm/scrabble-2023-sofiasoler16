import random
import unittest

from game.models import *

from unittest.mock import patch


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
            bag.actualizado["A"].cant,
            11,
        )

        bag.put("A")
        self.assertEqual(
            bag.actualizado["A"].cant, 12
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
            bag.actualizado["C"].cant,
            3,
        )
        bag.take()
        bag.take()

        bag.put("C")
        self.assertEqual(
            bag.actualizado["C"].cant, 2
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
            player_1.estado, "jugando"
        )
    def test_cambiadas(self):
        bag = BagTiles()
        player_1 = Player(bag)
        player_1.tiles_cambiadas
        self.assertEqual(
            len(player_1.tilesp),7
        )

    def test_cambio_estado_terminado(self):
        bag = BagTiles()
        player_1 = Player(bag)

        self.assertEqual(
            player_1.estado, "jugando"
            )  
        player_1.tilesp = []  
        player_1.cambio_estado(player_1)

        self.assertEqual(
            player_1.estado, "terminado"
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
        player1.tilesp = [
            "H",
            "O",
            "L",
            "A",
            "S",
            "B",
            "C",
        ]
        tiles = [
            Tile("H", 1, 3),
            Tile("O", 2, 3),
            Tile("L", 1, 5),
            Tile("A", 1, 12),
        ]
        player1.has_letters(tiles)
        self.assertEqual(player1.valid, True)




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
        center_cell = Cell(7,7)
        center_cell.add_letter(Tile("Q",5,1))
        
        board.validate_empty_board(center_cell) #Como hago para que la center cell sea solo la 7,7?

        self.assertEqual(board.status, "not empty")

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
    
    def test_show_board(self):
        #Crear un tablero con sus letras ubicadas
        board = Board()
        board.grid[3][1].add_letter(Tile('A',1,12))
        board.grid[3][2].add_letter(Tile('B',3,2))
        board.grid[3][3].add_letter(Tile('A',1,12))
        board.show_board()


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


class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag)

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
    
class TestClI(unittest.TestCase):

    @patch('builtins.input', return_value='3')
    def test_get_player_count(self, input_patched):
        cli = Cli()
        self.assertEqual(
            cli.ask_player_count(),
            3,
        )

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['A', '3'])
    def test_get_player_count_wrong_input(self, input_patched, print_patched):
        cli = Cli()
        self.assertEqual(
            cli.ask_player_count(),
            3,
        )

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['10', '1'])
    def test_get_player_count_control_max(self, input_patched, print_patched):
        cli = Cli()
        self.assertEqual(
            cli.ask_player_count(),
            1,
        )


class TestMain(unittest.TestCase):
    def setUp(self):
        self.main = Main()

    def test_input_valid_player_count(self):
        main = Main()
        main.main()
        self.assertEqual(main.status_players, "valid")


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

    def test_remove_invalid_word(self):
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