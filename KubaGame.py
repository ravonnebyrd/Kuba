# Author: Ravonne Byrd
# Date: June 2, 2021
# Description: Halfway Progress Report

"""
DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS

1. Initializing the board
        The board will be initialized as a list of lists inside the Board class. The beginning marble setup will be
    hardcoded into this major list - i.e. ['W', 'W', 'X', 'X', 'X', 'B', 'B'] will be the first list in the list.

2. Determining how to track which player's turn it is to play right now.
        Inside the make_move() method. At the end of a successful, valid move, before exiting the method,
    make_move() will use an if/else statement to set the turn to the next player, by using the set_next_turn() method.

3. Determining how to validate a move.
    3A. Boolean check that the game has not already been won, by calling self.get_winner().
    3B. Boolean check that is actually the player's turn, by equating playername and the result of self.get_next_turn().
    3C. Boolean check that the coordinates are valid, by seeing if desired coordinate is in
     list from self.get_board().get_coordinates().
    3D. Check that the possibly pushed off marble is not the player's own color.
    3E. Check that the marble to move is actually the player's marble.
    3F. Check that the marble isn't blocked on its side the direction is pushing off of. This require checking that
        the marble is either on an edge, or that there isn't another marble in that space, or that the marble is not
        surrounded.
    3G. Boolean check that resulting move won't recreate the same board immediately previous.
        Do this by checking self.get_board().get_previous() against sle.get_board().get_possible().

4. Determine how to return the marble count.

    4A. Inside the KubaGame class' get_marble_count(), it will use the Board object's method get_count() to
    get the 3-tuple.For example:
        self.get_board().get_count()
    will return the marble count. It will be inside KubaGame's get_marble_count() method.

        4A.1. The Board object's method get_count() will utilize get_count_white(), get_count_black(), get_count_red()
        to create this 3-tuple. For example:
            return self.get_count_white(), self.get_count_black(), self. get_count_red()
        will be inside the Board's get_count() method.

        4A.2. The marble counts on the board will be updated after every successful move, in the KubaGame make_move()
        method, if a move results in a marble being captured or knocked off the board.
        In order to do this I would need to:
            1. Check that there are no empty spaces between the player's marble, and the edge in the direction
            the marbles will be pushed.
            2. Store the marble being pushed in a temporary variable. (using pop() method).
            3. Depending on what that temporary variable equals, I will chose the most appropriate Board object
            method: decrement_count_white(), decrement_count_black(), or decrement_count_red().
            4. If pushed marble is 'R', I will also need to update the Player's captured count.

5. Determine how to move the marbles on the board.
    Check that marble isn't surrounded.
    Check that marble isn't the opponent's color.
    Check that marble is clear from the side being pushed on.
    5A. If direction is 'L', player must shift affected marbles left, one space. This can be done by iterating through
    the list and changing the index's of affected marbles to the previous index, until a marble is pushed off or a white
    space is encountered. .
    5B. If direction is 'R', player must shift affected marbles right, one space. This can be done by iterating through
    the list and changing the index's of affected marbles to the next index, until a marble is pushed off or a white
    space is encountered.
    5C. If the direction is 'F', transpose the board using the list() map() and zip() functions, and treat as if going
    right.
    5D. If the direction is 'B', transpose the board using the list() map() and zip() functions, and treat as if going
    left.
"""
import copy


class KubaGame:
    """
    Represents a game of Kuba.

    Responsibilities:   Creates a new game (instantiates).
                        Keep track of whose turn it is currently.
                        Let players make a valid game moves.
                        Returns how many red marbles a player has captured.
                        Returns what color marble is on a game square.
                        Returns a count of each color of marbles remaining on the board.
                        Records the winner.

    Communication:  Player class - to have player objects that can play the game.
                    Board class - to have a board object to play with.
    """
    def __init__(self, player_a, player_b):
        """
        Purpose: To instantiate a game round of KubaGame.
        This method will use the Player and Board classes to implement players and board object.

        Attributes: self._board - The game board (Board object).
                    self._Current_turn - The current player whose turn it is, else None is game has just begun (string).
                    self._winner - The winner of the game, else None if no winner is established yet (string).


        :param player_a: A tuple containing the player playername and their marble color. (ex: ('PlayerA', 'B'))
        :param player_b: A tuple containing the player playername and their marble color. (ex: ('PlayerB', 'W'))
        :return None
        """
        self._board = Board()
        self._current_turn = None
        self._winner = None
        self._player_a = Player(player_a)
        self._player_b = Player(player_b)

    # get methods
    def get_board(self):
        """
        Purpose: To return the self._board attribute's Board object.
        :return: The board object.
        """
        return self._board

    def get_current_turn(self):
        """
        Purpose: To return the player who can make a valid move currently.
        :return: Name of player whose turn it is.
                 Will return None at the beginning of the game, since either player can start.
        """
        return self._current_turn

    def get_winner(self):
        """
        Purpose: To return the Player object's playername of the winning player.
        :return: Name of the winning player ONLY
                 Else, None, if no one has won yet.
        """
        return self._winner

    def get_player_a(self):
        """
        Purpose: To return the first Player object.
        :return: Player A object
        """
        return self._player_a

    def get_player_b(self):
        """
        Purpose: To return the second Player object.
        :return: Player B object
        """
        return self._player_b

    def get_captured(self, playername):
        """
        Purpose: To return how many captures a player has made.

        :param playername: The player's playername.
        :return: Number of 'R' marbles captured by the named player.
                 Returns 0 if named player hasn't captured any marbles.
        """
        return self.get_player_a().get_captured() if playername == self.get_player_a().get_name() else \
            self.get_player_b().get_captured()

    def get_marble(self, coordinates):
        """
        Purpose: Takes the coordinates of a game cell, and returns the color of the marble occupying that space.
        :param coordinates: Tuple - (row_number, col_number)
        :return: Marble color: 'R', 'B', or 'W'.
                 Else, 'X' for no marble.
        """
        row, column = coordinates
        return self._board.get_board()[row][column]

    def get_marble_count(self):
        """
        Purpose: To return the count of all marbles on the board.

        :return: Tuple in the order (W, B, R), with each letter representing an integer of that color's remaining
                    board count.
        """
        return self.get_board().get_count()

    # set methods
    def set_turn(self, playername):
        """
        Purpose: To set the self._turn attribute to the opposing Player object playername.
        :param playername: The playername of the Player object whose turn it is next.
        :return: None
        """
        self._current_turn = playername

    def set_winner(self, playername):
        """
        Purpose: To set the self._winner attribute to the winning Player.
        :param playername: The playername of the Player who has won.
        :return: None
        """
        self._winner = playername

    # other methods
    def make_move(self, playername, coordinates, direction):
        """
        Purpose:
            *Note: A push only shifts the affected marbles one spot.
                  Thus, only one marble can get knocked off per turn.

        :param playername: Name of the player (ONLY)
        :param coordinates: Tuple - (row_number, col_number)
        :param direction: Direction the player wants to push the marble.
                          'L'(Left), 'R'(Right), 'F'(Forward) and 'B'(Backward)
        :return: True if the move is successful.
                 False for invalid conditions.
        """
        # Invalid self.make_move() conditions:
        # A player has already won.
        if self.get_winner() is not None:
            return False

        # Can only continue if self._current_turn is None or equals the playername parameter.
        if self.get_current_turn() is not None and self.get_current_turn() != playername:
            return False

        # The coordinates are invalid.
        if coordinates not in self.get_board().get_coordinates():
            return False

        # The desired marble is not of the playername parameter's color.
        if playername == self.get_player_a().get_name():
            if self.get_marble(coordinates) != self.get_player_a().get_color():
                return False
        else:
            if self.get_marble(coordinates) != self.get_player_b().get_color():
                return False

        # If marble is surrounded, declare game winner and return False.
        if not self.check_right(coordinates) and not self.check_left(coordinates) and not \
                self.check_bottom(coordinates) and not self.check_top(coordinates):
            if playername == self.get_player_a().get_name():
                self.set_winner(self.get_player_b().get_name())
                return False
            else:
                self.set_winner(self.get_player_a().get_name())
                return False

        # if direction is 'L', and player has a marble blocking to the right
        if direction == 'L':
            if not self.check_right(coordinates):
                return False

        # if direction is 'R', and player has a marble blocking to the left
        if direction == 'R':
            if not self.check_left(coordinates):
                return False

        # if direction is 'F', and player has a marble blocking to the bottom
        if direction == 'F':
            if not self.check_bottom(coordinates):
                return False
        # if direction is 'B', and player has a marble blocking to the top
        if direction == 'B':
            if not self.check_top(coordinates):
                return False

        # A move that undoes the opponent's move (Ko Rule).

        # Do the pretend move.

            # Evaluate if it is a move that results in knocking off the named player's own marble.
            # If so, return False.

        # At this point, move is officially valid.

        # Make the move.

        # Update the Board's marble count.

        # If applicable, update the Player's captured marble count.

        # In the Board object, set the new current board and new previous board.

        # Evaluate a win by player's captured count.
            # If win, set new winner.
        if playername == self.get_player_a():
            if self.get_player_a().get_captured() == 7:
                self.set_winner(playername)
        else:
            if self.get_player_b().get_captured() == 7:
                self.set_winner(playername)

        # Set turn to next player.
        if playername == self.get_player_a().get_name():
            self.set_turn(self.get_player_b().get_name())
        else:
            self.set_turn(self.get_player_a().get_name())

        return True

    def check_right(self, coordinates):
        """
        Purpose: This method checks if there is a valid space to the right of a marble for a valid pushing move.
        :param coordinates: Tuple - (row_number, col_number)
        :return: True if move is possible
                 False if move is invalid, marble block
        """
        row, column = coordinates
        column += 1
        if column < 7 and self.get_marble((row, column)) != 'X':
            return False
        return True

    def check_left(self, coordinates):
        """
        Purpose: This method checks if there is a valid space to the left of a marble for a valid pushing move.
        :param coordinates: Tuple - (row_number, col_number)
        :return: True if move is possible
                 False if move is invalid, marble block
        """
        row, column = coordinates
        column -= 1
        if column > -1 and self.get_marble((row, column)) != 'X':
            return False
        return True

    def check_bottom(self, coordinates):
        """
        Purpose: This method checks if there is a valid space to the bottom of a marble for a valid pushing move.
        :param coordinates: Tuple - (row_number, col_number)
        :return: True if move is possible
                 False if move is invalid, marble block
        """
        row, column = coordinates
        row += 1
        if row < 7 and self.get_marble((row, column)) != 'X':
            return False
        return True

    def check_top(self, coordinates):
        """
        Purpose: This method checks if there is a valid space to the top of a marble for a valid pushing move.
        :param coordinates: Tuple - (row_number, col_number)
        :return: True if move is possible
                 False if move is invalid, marble block
        """
        row, column = coordinates
        row -= 1
        if row > -1 and self.get_marble((row, column)) != 'X':
            return False
        return True


class Board:
    """
    Represents the Board object.

    Responsibilities:   To instantiate a Board object with the correct marble setup.
                        To keep track of the immediately previous board (to stop Player objects from undoing their
                            opponent's moves.
                        Get the counts of the colors on the current board, as a 3-tuple.
                        Get/Decrement the count of any color on the board.
    Communication: KubaGame class - KubaGame will instantiate a board object. It will rely on the Boards get_count()
                                    method for its get_marble_count() method.
    """

    def __init__(self):
        """
        Purpose: To instantiate a Board object.
        Cell coordinates range from (0,0) to (6,6) - i.e. (row_number, col_number)

        Attributes: self._board - A list of lists representation of the board.
                    self._previous - A deepcopy of the previous self._board after the previous turn.
                    self._possible - A deepcopy of the current self._board, with the possible move made
                    self._W - The count of white marbles on the board. Instantiated to 8.
                    self._B - The count of black marbles on the board. Instantiated to 8.
                    self._R - The count of red marbles on the board. Instantiated to 13.
                    self._coordinates - A list of all possible coordinates.

        :return None
        """
        self._board = [
            ['W', 'W', 'X', 'X', 'X', 'B', 'B'],
            ['W', 'W', 'X', 'R', 'X', 'B', 'B'],
            ['X', 'X', 'R', 'R', 'R', 'X', 'X'],
            ['X', 'R', 'R', 'R', 'R', 'R', 'X'],
            ['X', 'X', 'R', 'R', 'R', 'X', 'X'],
            ['B', 'B', 'X', 'R', 'X', 'W', 'W'],
            ['B', 'B', 'X', 'X', 'X', 'W', 'W']
        ]
        self._previous = None
        self._possible = None
        self._W = 8
        self._B = 8
        self._R = 13
        self._coordinates = [(x, y) for x in range(7) for y in range(7)]

    # get methods
    def get_board(self):
        """
        Purpose: To return the current self._board
        :return: The list of lists of the current self._board.
        """
        return self._board

    def get_previous(self):
        """
        Purpose: To return the previous board.
        :return: The list of lists of the previous board.
        """
        return self._previous

    def get_possible(self):
        """
        Purpose: To return the possible board.

        :return: The list of lists of the possible board.
        """
        return self._possible

    def get_count(self):
        """
        Purpose: To return the total marble counts of the current self._board
        :return: A tuple containing the counts per color of marbles remaining on the board
                    - i.e. (W, B, R), where letters = integers.
        """
        return self.get_count_white(), self.get_count_black(), self.get_count_red()

    def get_count_black(self):
        """
        Purpose: To return the black marble count of the current self._board.
        :return: The number of black marbles on the current self._board.
        """
        return self._B

    def get_count_white(self):
        """
        Purpose: To return the white marble count of the current self._board.
        :return: The number of white marbles on the current self._board.
        """
        return self._W

    def get_count_red(self):
        """
        Purpose: To return the red marble count of the current self._board.
        :return: The number of red marbles on the current self._board.
        """
        return self._R

    def get_coordinates(self):
        """
        Purpose: To return a list of all possible coordinates.
        :return: TThe list of game coordinates/spaces.
        """
        return self._coordinates

    # set methods
    def set_board(self):
        """
        Purpose: To set the current self._board

        :return: None
        """
        pass

    def set_previous(self):
        """
        Purpose: To set the previous board.

        :return: None
        """
        pass

    def set_possible(self, playername, coordinates, direction):
        """
        Purpose: To set the immediately possible board.
        Do this by creating a deepcopy of the self.get_board() and making the move

        :param playername: Name of the player (ONLY)
        :param coordinates: Tuple - (row_number, col_number)
        :param direction: Direction the player wants to push the marble.
                          'L'(Left), 'R'(Right), 'F'(Forward) and 'B'(Backward)
        :return: None
        """
        pass

    # decrement set methods
    def decrement_count_black(self):
        """
        Purpose: To decrement the count of black marbles on the current self._board.

        :return: None
        """
        self._B -= 1

    def decrement_count_white(self):
        """
        Purpose: To decrement the count of black marbles on the current self._board.

        :return: None
        """
        self._W -= 1

    def decrement_count_red(self):
        """
        Purpose: To decrement the count of black marbles on the current self._board.

        :return: None
        """
        self._R -= 1


class Player:
    """
    Represents a Player object.

    Responsibilities:   Get/set the player's playername.
                        Get/set the player's marble color.
                        Get/increment the player's count of 'R' marbles captured.

    Communication: KubaGame class - Will instantiate two Player objects in its init method.
                                    Will use the get_captured_count() and increment_captured_count() methods in its
                                        get_captured() and make_move() methods, respectively.
    """

    def __init__(self, player_info):
        """
        Purpose: To instantiate a Player object.
        Attributes: self._playername - The playername of the player (string).
                    self._color - The marble color of the player (string).
                    self._captured - The amount of 'R' marbles the player has captured (integer).
                                     Instantiated to 0.
        :param player_info: A tuple, consisting of the player's name and chosen color.
        :return None
        """
        name, color = player_info
        self._playername = name
        self._color = color
        self._captured = 0

    # get methods
    def get_name(self):
        """
        Purpose: To get the playername of the Player object.
        :return: The playername of the player.
        """
        return self._playername

    def get_color(self):
        """
        Purpose: To get the marble color of the Player.
        :return: 'W' or 'B'
        """
        return self._color

    def get_captured(self):
        """
        Purpose: To get the count of 'R' marbles that the Player object has captured.
        :return: Number of 'R' marbles captured.
        """
        return self._captured

    # other methods
    def increment_captured(self):
        """
        Purpose: To increment the count of 'R' marbles that the Player object has captured.
        :return: None
        """
        self._captured += 1


def main():
    """TODO"""
    b = KubaGame(('Sarah', 'B'), ('Jamal', 'W'))


if __name__ == '__main__':
    main()
