# Author: Ravonne Byrd
# Date: June 2, 2021
# Description: TODO

"""
DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS

1. Initializing the board
        The board will be initialized as a list of lists inside the Board class. The beginning marble setup will be
    hardcoded into this major list - i.e. ['W', 'W', 'X', 'X', 'X', 'B', 'B'] will be the first list in the list.

2. Determining how to track which player's turn it is to play right now.
        Inside the make_move() method. At the end of a successful, valid move, before exiting the method,
    make_move() will use an if/else statement to set the turn to the next player, by using the set_next_turn() method.

3. Determining how to validate a move.
    TODO

4. Determine how to return the marble count.
    Inside the KubaGame class' get_marble_count(), it will use the Board object's method get_count() to get the 3-tuple.
        For example - self.get_board().get_count()
                      will be inside get_marble_count() method, which will return that result.
    The Board object's method get_count() will utilize get_count_white(), get_count_black(), get_count_red() to create
        this 3-tuple.
        For example - return self.get_count_white(), self.get_count_black(), self. get_count_red()
                      will be inside get_count()
    The marble counts on the board will be updated after every successful move, in the make_move() method,
        if a move results in a marble being captured or knocked off the board.

5. Determine how to move the marbles on the board.
    TODO

"""


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
    pass

    def __init__(self, player_a, player_b):
        """
        Purpose: To instantiate a game round of KubaGame.
        This method will use the Player and Board classes to implement players and board object.

        Attributes: self._winner - The winner of the game, else None if no winner is established yet (string).
                    self._turn - The current player whose turn it is, else None is game has just begun (string).
                    self._board - The game board (Board object).

        :param player_a: A tuple containing the player playername and their marble color. (ex: ('PlayerA', 'B'))
        :param player_b: A tuple containing the player playername and their marble color. (ex: ('PlayerB', 'W'))
        :return None
        """
        pass

    def get_next_turn(self):
        """
        Purpose: To return the player who can make a valid move currently.
        :return: Name of player whose turn it is.
                 Will return None at the beginning of the game, since either player can start.
        """
        pass

    def set_current_turn(self, playername):
        """
        Purpose: To set the self._turn attribute to the opposing Player object playername.

        :param playername: The playername of the Player object whose turn it is next.
        :return: None
        """
        pass

    def make_move(self, playername, coordinates, direction):
        """
        Purpose:
            *Note: A push only shifts the affected marbles one spot.
                  Thus, only one marble can get knocked off per turn.
                  Up to six marbles can be pushed by the named player's marble at one time - unless every slot
                    in a column is full with 'R', 'B', or 'W', then a player can push the whole column, if a valid move.

        :param playername: Name of the player (ONLY)
        :param coordinates: Tuple - (row_number, col_number)
        :param direction: Direction the player wants to push the marble.
                          'L'(Left), 'R'(Right), 'F'(Forward) and 'B'(Backward)
        :return: True if the move is successful.
                 False if: The game has already been won.
                           If it is not the named player's turn.
                           If the coordinates are invalid.
                           If the marble in that coordinate cannot move in that direction
                                Such as: a move that undoes the opponent's move.
                                         a move that results in knocking off the named player's own marble.
                           If the marble in that coordinate is not the named player's marble.
                                A player can only directly push their own marble
                                *Note: Any marble can be pushed indirectly.
                           Or for any other other invalid condition.
        """
        pass

    def get_board(self):
        """
        Purpose: To return the self._board attribute's Board object.

        :return: The board object.
        """
        pass

    def get_winner(self):
        """
        Purpose: To return the Player object's playername of the winning player.

        :return: Name of the winning player ONLY
                 Else, None, if no one has won yet.
        """
        pass

    def get_captured(self, playername):
        """
        Purpose: To return how many captures a player has made.

        :param playername: The player's playername.
        :return: Number of 'R' marbles captured by the named player.
                 Returns 0 if named player hasn't captured any marbles.
        """
        pass

    def get_marble(self, coordinates):
        """
        Purpose: Takes the coordinates of a game cell, and returns the color of the marble occupying that space.

        :param coordinates: Tuple - (row_number, col_number)
        :return: Marble color: 'R', 'B', or 'W'.
                 Else, 'X' for no marble.
        """
        pass

    def get_marble_count(self):
        """
        Purpose: To return the count of all marbles on the board.

        :return: Tuple in the order (W, B, R), with each letter representing an integer of that color's remaining
                    board count.
        """
        pass


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
        Will use a list of lists to create the Board object.
            Top left cell: (0,0)
            Bottom right cell: (6,6).
            Coordinates: (row_number, col_number)

        Attributes: self._board - A list of lists representation of the board.
                    self._previous - A deepcopy of the previous self._board after the previous turn.
                    self._W - The count of white marbles on the board. Instantiated to 8.
                    self._B - The count of black marbles on the board. Instantiated to 8.
                    self._R - The count of red marbles on the board. Instantiated to 13.

        :return None
        """
        pass

    def get_count(self):
        """
        Purpose: To return the total marble counts of the current self._board

        :return: A tuple containing the counts per color of marbles remaining on the board
                    - i.e. (W, B, R), letters = integers.
        """
        pass

    def get_count_black(self):
        """
        Purpose: To return the black marble count of the current self._board.

        :return: The number of black marbles on the current self._board.
        """
        pass

    def get_count_white(self):
        """
        Purpose: To return the white marble count of the current self._board.

        :return: The number of white marbles on the current self._board.
        """
        pass

    def get_count_red(self):
        """
        Purpose: To return the red marble count of the current self._board.

        :return: The number of red marbles on the current self._board.
        """
        pass

    def decrement_count_black(self):
        """
        Purpose: To decrement the count of black marbles on the current self._board.

        :return: None
        """
        pass

    def decrement_count_white(self):
        """
        Purpose: To decrement the count of black marbles on the current self._board.

        :return: None
        """
        pass

    def decrement_count_red(self):
        """
        Purpose: To decrement the count of black marbles on the current self._board.

        :return: None
        """
        pass


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

    def __init__(self):
        """
        Purpose: To instantiate a Player object.
        Attributes: self._name - The playername of the player (string).
                    self._color - The marble color of the player (string).
                    self._captured - The amount of 'R' marbles the player has captured (integer).
                                     Instantiated to 0.
        :return None
        """
        pass

    def get_name(self):
        """
        Purpose: To get the playername of the Player object.

        :return: The playername of the player.
        """
        pass

    def get_color(self):
        """
        Purpose: To get the marble color of the Player.

        :return: 'W' or 'B'
        """
        pass

    def set_name(self):
        """
        Purpose: To set the playername of the Player object.

        :return: None
        """
        pass

    def set_color(self):
        """
        Purpose: To set the marble color chosen for the Player object.

        :return: None
        """
        pass

    def get_captured(self):
        """
        Purpose: To get the count of 'R' marbles that the Player object has captured.

        :return: Number of 'R' marbles captured.
        """
        pass

    def increment_captured(self):
        """
        Purpose: To increment the count of 'R' marbles that the Player object has captured.

        :return: None
        """
        pass


def main():
    """TODO"""
    pass


if __name__ == '__main__':
    main()
