import unittest
from KubaGame import KubaGame


class TestKubaGame(unittest.TestCase):
    # game.make_move('', (), '')

    # player out of turn
    def test_make_move_1(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        game.make_move('Jane', (0, 0), 'B')
        self.assertFalse(print(game.make_move('Jane', (0, 1), 'B')))

    # player moving from blocked left direction
    def test_make_move_2(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        self.assertFalse(print(game.make_move('Jane', (0, 1), 'R')))

    # player moving from blocked right direction
    def test_make_move_3(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        self.assertFalse(print(game.make_move('Richard', (0, 5), 'L')))

    # player moving from blocked top direction
    def test_make_move_4(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        self.assertFalse(print(game.make_move('Richard', (1, 5), 'B')))

    # player moving from blocked bottom direction
    def test_make_move_5(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        self.assertFalse(print(game.make_move('Jane', (5, 5), 'F')))

    # test capture 1
    def test_make_move_6(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        game.make_move('Jane', (0, 0), 'B')
        game.make_move('Richard', (0, 5), 'B')
        game.make_move('Jane', (1, 0), 'R')
        game.make_move('Richard', (1, 5), 'B')
        game.make_move('Jane', (1, 1), 'R')
        game.make_move('Richard', (2, 5), 'B')
        game.make_move('Jane', (1, 2), 'R')
        game.make_move('Richard', (3, 5), 'B')
        game.make_move('Jane', (1, 3), 'R')
        game.make_move('Richard', (4, 5), 'B')
        self.assertEqual(game.get_player_b().get_captured(), 1)

    # test capture 2
    def test_make_move_7(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        game.make_move('Jane', (0, 0), 'B')
        game.make_move('Richard', (0, 5), 'B')
        game.make_move('Jane', (1, 0), 'R')
        game.make_move('Richard', (1, 5), 'B')
        game.make_move('Jane', (1, 1), 'R')
        game.make_move('Richard', (2, 5), 'B')
        game.make_move('Jane', (1, 2), 'R')
        game.make_move('Richard', (3, 5), 'B')
        game.make_move('Jane', (1, 3), 'R')
        game.make_move('Richard', (4, 5), 'B')
        game.make_move('Jane', (1, 4), 'R')
        self.assertEqual(game.get_player_a().get_captured(), 1)

    def test_make_move_8(self):
        pass

    def test_make_move_9(self):
        pass

    def test_make_move_10(self):
        pass

    def test_make_move_11(self):
        pass

    def test_make_move_12(self):
        pass

    def test_make_move_13(self):
        pass

    def test_make_move_14(self):
        pass

    def test_make_move_15(self):
        pass


if __name__ == '__main__':
    unittest.main()
