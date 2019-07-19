import PIL.ImageGrab
import pyautogui
import time
from typing import Union
from config import LOCATION_MAPPING
from board import Board


class GameBoard(Board):
    def __init__(self):
        """ Start the game on the web """
        pyautogui.click(1205, 1215)  # Clicking the retry button
        time.sleep(0.1)
        pyautogui.click(1205, 1215)  # Clicking the retry button again. Sometimes two are needed
        time.sleep(4.5)
        # Load the boards starting state
        self.board = self.get_board_state()

    def get_board_state(self) -> list:
        """ Gets the boards state from the website and models it in a more readable format

        :return: A model of the web games board
        """
        new_board_state = []
        # Take a screen shot of the window
        img = PIL.ImageGrab.grab()

        # Check every tile location on the screen
        for val in LOCATION_MAPPING.values():
            # When the tile is black it is a 1
            if str(img.getpixel(val)) == '(0, 0, 0)':
                new_board_state.append(1)

            else:
                new_board_state.append(0)

        return new_board_state

    def click(self, location) -> Union[tuple, bool]:
        """ Clicks on the web games tile at the corresponding board index

        :param location: The board index to be clicked
        :return: The new board state and whether the game is over
        """
        # Click requested location
        pyautogui.click(LOCATION_MAPPING.get(location))

        # Check if the click was on a white tile
        if self.board[location] == 0:
            return None, True

        # Keep checking to see if the new square has been added to the board
        new_board_state = self.board
        while new_board_state == self.board or new_board_state.count(1) != 3:
            new_board_state = self.get_board_state()

        # Save the new board state
        self.board = new_board_state

        return self.get_board(), False

    def get_board(self) -> tuple:
        """ Returns the current model of the board as a tuple

        :return: Tuple of the current model of the board
        """
        return tuple(self.board)
