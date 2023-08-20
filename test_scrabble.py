import random
import unittest

from scrabble import Tile, BagTiles
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
            bag.tiles["A"].cant,
            11,
        )


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




if __name__ == '__main__':
    unittest.main()