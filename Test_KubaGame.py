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

    # test capture bottom
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

    # test capture right
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

    # test capture top
    def test_make_move_8(self):
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
        game.make_move('Richard', (5, 0), 'R')
        game.make_move('Jane', (0, 1), 'B')
        game.make_move('Richard', (5, 2), 'F')
        game.make_move('Jane', (1, 5), 'B')
        game.make_move('Richard', (4, 2), 'F')
        game.make_move('Jane', (2, 5), 'B')
        game.make_move('Richard', (3, 2), 'F')
        self.assertEqual(game.get_player_b().get_captured(), 2)

    # test capture left
    def test_make_move_9(self):
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
        game.make_move('Richard', (5, 0), 'R')
        game.make_move('Jane', (0, 1), 'B')
        game.make_move('Richard', (5, 2), 'F')
        game.make_move('Jane', (1, 5), 'B')
        game.make_move('Richard', (4, 2), 'F')
        game.make_move('Jane', (2, 5), 'B')
        game.make_move('Richard', (3, 2), 'F')
        game.make_move('Jane', (3, 5), 'L')
        game.make_move('Richard', (6, 1), 'F')
        game.make_move('Jane', (3, 4), 'L')
        game.make_move('Richard', (4, 1), 'R')
        game.make_move('Jane', (3, 3), 'L')
        self.assertEqual(game.get_player_a().get_captured(), 2)

    # test undoing previous move error
    def test_make_move_10(self):
        pass

    # test win by capturing 7 R marbles
    def test_make_move_11(self):
        pass

    # test win by clearing opponent's marbles
    def test_make_move_12(self):
        pass

    # test win by having no legal moves available - no marbles can move
    def test_make_move_13(self):
        pass

    # test turns at the beginning of the game - first player
    def test_make_move_14(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        self.assertTrue(game.make_move('Jane', (0, 0), 'B'))

    # test turns at the beginning of the game - first player
    def test_make_move_15(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        self.assertTrue(game.make_move('Richard', (0, 5), 'B'))

    # test turns when set
    def test_make_move_16(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        game.make_move('Jane', (0, 0), 'B')
        self.assertFalse(game.make_move('Jane', (1, 0), 'R'))


if __name__ == '__main__':
    unittest.main()
