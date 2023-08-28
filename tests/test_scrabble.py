import random
import unittest

from game.models import Tile, BagTiles, YaHaySuficientes, Player, ScrabbleGame, Cell, Board

from unittest.mock import patch


class TestTiles(unittest.TestCase):
    def test_tile_valueycantA(self):
        tile = Tile('A',1, 12)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.cant, 12)
        self.assertEqual(tile.value, 1)
    def test_tile_valueycantB(self):
        tile = Tile('B',3, 2)
        self.assertEqual(tile.letter, 'B')
        self.assertEqual(tile.cant, 2)
        self.assertEqual(tile.value, 3)
    def test_tile_valueycantH(self):
        tile = Tile('H',4, 2)
        self.assertEqual(tile.letter, 'H')
        self.assertEqual(tile.cant, 2)
        self.assertEqual(tile.value, 4)

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
        player_1 = Player()
        self.assertEqual(
        len(player_1.tilesp),5
        )
    def test_cambiadas(self):
        player_1 = Player()
        player_1.tiles_cambiadas
        self.assertEqual(
            len(player_1.tilesp),5
        )


            
class TestScrabble(unittest.TestCase):
    Scrabble_game = ScrabbleGame(3)

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
    def test_init(self):
        cell = Cell(multiplayer=2, multiplayer_type="letter")
        
        self.assertEqual(
            cell.multiplayer, 2
        )
        self.assertEqual(
            cell.multiplayer_type, "letter"
        )
        self.assertIsNone(cell.letter)

    def test_add_letter(self):
        cell = Cell(multiplayer=1, multiplayer_type="")
        letter = Tile(letter="A", value=1, cant=12)

        cell.add_letter(letter=letter)
        self.assertEqual(cell.letter, letter)

    def test_cell_value(self):
        cell = Cell(multiplayer=1, multiplayer_type="letter")
        letter = Tile(letter="P", value=3, cant=2)

        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),3
        )

    def test_cell_multiplier_word(self):
        cell = Cell(multiplayer=2, multiplayer_type='word')
        letter = Tile(letter='p', value=3, cant=2)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            3,
        )


if __name__ == '__main__':
    unittest.main()