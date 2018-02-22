import unittest
from game import Game
class test_game(unittest.TestCase):
    game = Game()

    def test_add(self):
        result = self.game.add(10,5)
        self.assertEqual(result,15)

    def test_update(self):
        self.assertEqual(self.game.lives, 2)
