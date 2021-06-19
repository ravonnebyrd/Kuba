import unittest
from KubaGame import KubaGame


class TestKubaGame(unittest.TestCase):
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
        game.make_move('Richard', (0, 6), 'B')
        game.make_move('Jane', (1, 2), 'R')
        game.make_move('Richard', (1, 6), 'B')
        game.make_move('Jane', (1, 3), 'R')
        game.make_move('Richard', (6, 0), 'R')
        game.make_move('Jane', (1, 4), 'R')
        self.assertEqual(game.get_player_a().get_captured(), 1)

    # test capture top
    def test_make_move_8(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        game.make_move('Richard', (6, 0), 'F')
        game.make_move('Jane', (6, 5), 'F')
        game.make_move('Richard', (5, 0), 'F')
        game.make_move('Jane', (5, 5), 'F')
        game.make_move('Richard', (4, 0), 'F')
        game.make_move('Jane', (4, 5), 'F')
        game.make_move('Jane', (3, 5), 'F')
        game.make_move('Jane', (2, 5), 'F')
        self.assertEqual(game.get_player_a().get_captured(), 1)

    # test capture left
    def test_make_move_9(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        game.make_move('Richard', (1, 6), 'L')
        game.make_move('Jane', (5, 6), 'L')
        game.make_move('Richard', (1, 5), 'L')
        game.make_move('Jane', (5, 5), 'L')
        game.make_move('Richard', (1, 4), 'L')
        game.make_move('Richard', (1, 3), 'L')
        game.make_move('Richard', (1, 2), 'L')
        self.assertEqual(game.get_player_b().get_captured(), 1)

    # test undoing previous move error - Ko Rule
    def test_make_move_10(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        game.make_move('Jane', (0, 0), 'R')
        game.make_move('Richard', (0, 6), 'L')
        game.make_move('Jane', (0, 1), 'R')
        game.make_move('Richard', (0, 5), 'L')
        self.assertFalse(game.make_move('Jane', (0, 1), 'R'))

    # test win by capturing 7 R marbles
    def test_make_move_11(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        game.get_board().set_board([
            ['W', 'R', 'X', 'X', 'X', 'B', 'B'],
            ['W', 'W', 'X', 'R', 'X', 'B', 'B'],
            ['X', 'X', 'X', 'X', 'R', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'R', 'R', 'X'],
            ['X', 'X', 'X', 'X', 'W', 'X', 'X'],
            ['B', 'B', 'X', 'R', 'X', 'W', 'W'],
            ['B', 'B', 'X', 'X', 'X', 'W', 'W']
        ])
        game.get_player_a().increment_captured()
        game.get_player_a().increment_captured()
        game.get_player_a().increment_captured()
        game.get_player_a().increment_captured()
        game.get_player_a().increment_captured()
        game.get_player_a().increment_captured()
        game.make_move('Jane', (1, 1), 'F')
        self.assertEqual(game.get_winner(), 'Jane')

    # test win by clearing opponent's marbles A
    def test_make_move_12(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        game.get_board().set_board([
            ['X', 'X', 'X', 'X', 'X', 'X', 'B'],
            ['W', 'B', 'X', 'R', 'X', 'B', 'B'],
            ['X', 'X', 'R', 'R', 'R', 'X', 'X'],
            ['X', 'R', 'R', 'R', 'R', 'R', 'X'],
            ['X', 'X', 'R', 'R', 'R', 'X', 'X'],
            ['B', 'B', 'X', 'R', 'X', 'X', 'X'],
            ['B', 'B', 'X', 'X', 'X', 'X', 'X']
        ])
        game.get_board().decrement_count_white()
        game.get_board().decrement_count_white()
        game.get_board().decrement_count_white()
        game.get_board().decrement_count_white()
        game.get_board().decrement_count_white()
        game.get_board().decrement_count_white()
        game.get_board().decrement_count_white()
        game.make_move('Richard', (1, 1), 'L')
        self.assertEqual(game.get_winner(), 'Richard')

    # test win by having no legal moves available - no marbles can move
    def test_make_move_13(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        game.get_board().set_board([
            ['X', 'B', 'X', 'X', 'R', 'W', 'R'],
            ['B', 'W', 'B', 'X', 'X', 'R', 'X'],
            ['X', 'B', 'X', 'X', 'X', 'B', 'X'],
            ['X', 'R', 'R', 'X', 'R', 'R', 'X'],
            ['X', 'X', 'R', 'X', 'R', 'R', 'X'],
            ['B', 'B', 'X', 'R', 'X', 'B', 'X'],
            ['X', 'X', 'X', 'X', 'R', 'W', 'R']
        ])
        self.assertFalse(game.make_move('Jane', (1, 1), 'L'))
        self.assertEqual(game.get_winner(), 'Richard')

    # test turns at the beginning of the game - first player
    def test_make_move_14(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        self.assertTrue(game.make_move('Jane', (0, 0), 'B'))

    # test turns at the beginning of the game - second player
    def test_make_move_15(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        self.assertTrue(game.make_move('Richard', (0, 5), 'B'))

    # test turns when set
    def test_make_move_16(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        game.make_move('Jane', (0, 0), 'B')
        self.assertFalse(game.make_move('Jane', (1, 0), 'R'))

    # test win by clearing opponent's marbles B
    def test_make_move_17(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        game.get_board().set_board([
            ['W', 'W', 'X', 'X', 'X', 'X', 'B'],
            ['W', 'X', 'X', 'R', 'X', 'X', 'W'],
            ['X', 'X', 'R', 'R', 'R', 'X', 'X'],
            ['X', 'R', 'R', 'R', 'R', 'R', 'X'],
            ['X', 'X', 'R', 'R', 'R', 'X', 'X'],
            ['X', 'X', 'X', 'R', 'X', 'W', 'W'],
            ['X', 'X', 'X', 'X', 'X', 'W', 'W']
        ])
        game.get_board().decrement_count_black()
        game.get_board().decrement_count_black()
        game.get_board().decrement_count_black()
        game.get_board().decrement_count_black()
        game.get_board().decrement_count_black()
        game.get_board().decrement_count_black()
        game.get_board().decrement_count_black()
        game.make_move('Jane', (1, 6), 'F')
        self.assertEqual(game.get_winner(), 'Jane')

    # test trying to make a move after game has been won
    def test_make_move_18(self):
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        game.get_board().set_board([
            ['W', 'W', 'X', 'X', 'X', 'X', 'B'],
            ['W', 'X', 'X', 'R', 'X', 'X', 'W'],
            ['X', 'X', 'R', 'R', 'R', 'X', 'X'],
            ['X', 'R', 'R', 'R', 'R', 'R', 'X'],
            ['X', 'X', 'R', 'R', 'R', 'X', 'X'],
            ['X', 'X', 'X', 'R', 'X', 'W', 'W'],
            ['X', 'X', 'X', 'X', 'X', 'W', 'W']
        ])
        game.get_board().decrement_count_black()
        game.get_board().decrement_count_black()
        game.get_board().decrement_count_black()
        game.get_board().decrement_count_black()
        game.get_board().decrement_count_black()
        game.get_board().decrement_count_black()
        game.get_board().decrement_count_black()
        game.make_move('Jane', (1, 6), 'F')
        self.assertFalse(game.make_move('Richard', (0, 6), 'L'))

    # test getting an extra turn after a successful move - player A
    def test_make_move_19(self):
        # game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        game = KubaGame(('Jane', 'W'), ('Richard', 'B'))
        game.make_move('Jane', (0, 0), 'B')
        game.make_move('Richard', (0, 5), 'B')
        game.make_move('Jane', (1, 0), 'R')
        game.make_move('Richard', (1, 5), 'B')
        game.make_move('Jane', (1, 1), 'R')
        game.make_move('Richard', (2, 5), 'B')
        self.assertFalse(game.make_move('Jane', (1, 2), 'R'))
        self.assertEqual(game.get_current_turn(), 'Richard')


if __name__ == '__main__':
    unittest.main()
