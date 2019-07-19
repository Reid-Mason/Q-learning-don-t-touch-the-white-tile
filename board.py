import random
from typing import Union
import numpy as np
from config import CLICK_REWARD, MISS_PENALTY, LOCATION_MAPPING


class Board:
    """ This is a simulation of the web game don't touch the white tile.

    This class is used for training the ai faster as it takes many iterations for the ai to learn.
    By using this class we can cycle through games much faster and allow the ai to solve Q states after it fails them.
    """

    def __init__(self):
        """ Creates a board with three black squares in random positions """
        self.board = [0] * 13 + [1] * 3
        np.random.shuffle(self.board)

    def add_new_square(self) -> None:
        """ Adds a new black square to a random position  on the board """
        choice = random.choice([i for i, x in enumerate(self.board) if x == 0])
        self.board[choice] = 1

    def click(self, location: int) -> Union[int, tuple]:
        """ Simulates a click at a selected location on the board.

        This will also evaluate the reward or penalty for the move.
        If the click is on a white tile the board will not be changed
        in order to allow the ai to learn from it's mistake.

        :param location: The index value of the board where the click should take place
        :return: The reward or penalty for clicking the chosen location and the current board state
        """
        if self.board[location] == 1:
            # Set the black tile to white
            self.board[location] = 0
            self.add_new_square()

            return CLICK_REWARD, self.get_board()

        # When the clicked tile is white
        return -MISS_PENALTY, self.get_board()

    def get_board(self) -> tuple:
        """ Getter for the current board state

        :return: The current board state
        """
        return tuple(self.board)

    def __str__(self) -> str:
        """ A string representation of the board, mostly for debugging purposes

        :return: A human readable string representation of the board
        """
        return f'Board: {self.board}'
