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
    
    def test_multi(self):
        cell = Cell(row=3, column=5)
        letter = Tile(letter="A", value=1, cant=12)
        cell.add_letter(letter)
        cell.multiplier_value()
        self.assertEqual(
            cell.value, 2
        )

    def test_value_normal(self):
        cell = Cell(row=4, column=7)
        letter = Tile(letter="Q", value=5, cant=1)
        cell.add_letter(letter)
        cell.multiplier_value()
        self.assertEqual(
            cell.value,5
        )

    def test_value_segundavez(self):
        cell = Cell(row=3, column=5)
        letter = Tile("Q",5,1)
        cell.add_letter(letter)

        cell.multiplier_value()
        self.assertEqual(
            cell.value,10
        )
        cell.used = True  
        cell.multiplier_value()
        self.assertEqual(
            cell.value,5
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

class TestMain(unittest.TestCase):
    def setUp(self):
        self.main = Main()

    def test_input_valid_player_count(self):
        main = Main()
        main.main()
        self.assertEqual(main.status_players, "valid")

    def test_1letter_word(self):
        """
        word2 = Cell(2,6)

        letter = Tile(letter="C", value=1, cant=4)
        word2.add_letter(letter)
        word2.multiplier_value()
        """
        #Como agrego valores a las celdas de al lado y que se queden ahi
        word = Word(Cell(2,5))

        letter = Tile(letter="C", value=1, cant=4)
        word.cell.add_letter(letter)
        word.cell.multiplier_value()

        word.calculate_word_value()
        self.assertEqual(word.wordvalue, 1)

    def word_calculate_value(self): #No toma el test
        cell1 = Cell(row=2, column=5) #No se como setear una celda para siempre con un valor para testear con ese valor
        cell1.add_letter("C")
        cell2 = Cell(row=2, column=6)
        cell2.add_letter("A")
        cell3 = Cell(row=2, column=7)
        cell3.add_letter("S")
        cell4 = Cell(row=2, column=8)
        cell4.add_letter("A")

        word = Word(Cell(2,5))
        word.calculate_word_value()
        self.assertEqual(word.wordvalue,4)

"""
    cell1 = Cell(row=2, column=5)
    cell1.add_letter("C")
    cell2 = Cell(row=2, column=6)
    cell2.add_letter("A")
    cell3 = Cell(row=2, column=7)
    cell3.add_letter("S")
    cell4 = Cell(row=2, column=8)
    cell4.add_letter("A")
"""
class TestDictionary(unittest.TestCase):
    def test_word_in_dictionary(self):
        dictionary = Dictionary("/home/sofia16044/Documentos/computacion/scrabble-2023-sofiasoler16/dictionaries/dictionary .txt")
        self.assertEqual(dictionary.valid_word('arbol'), True)
    def test_word_not_dictionary(self):
        dictionary = Dictionary("/home/sofia16044/Documentos/computacion/scrabble-2023-sofiasoler16/dictionaries/dictionary .txt")
        self.assertEqual(dictionary.valid_word('schmolicnsd'), False)    


if __name__ == '__main__':
    unittest.main()