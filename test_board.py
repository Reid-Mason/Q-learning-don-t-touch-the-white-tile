import unittest
from board import Board
from config import CLICK_REWARD, MISS_PENALTY, SIZE


class TestBoard(unittest.TestCase):
    def test_get_board(self):
        """ Testing that the get board function returns the right values """
        board_state = Board().get_board()

        # Check the board state is returned as a tuple
        self.assertEqual(type(board_state), tuple)
        # Check the board has 16 elements
        self.assertEqual(len(board_state), SIZE)
        # Check the board has thirteen 0 values
        self.assertEqual(board_state.count(0), 13)
        # Check the board has three 1 values
        self.assertEqual(board_state.count(1), 3)

    def test_add_new_square(self):
        """ Testing whether the board is able to add a new square """
        # Create board
        board = Board()
        original_state = board.get_board()
        # Add a new square
        board.add_new_square()
        new_state = board.get_board()

        # The table should have been changed in some way
        self.assertNotEqual(original_state, new_state)
        # There should be one more 1 value in the table
        self.assertEqual(new_state.count(1), original_state.count(1) + 1)
        # There should be one less 0 value in the table
        self.assertEqual(new_state.count(0), original_state.count(0) - 1)

    def test_click_value_one(self):
        board = Board()
        original_state = board.get_board()

        # Choose a location and click it when the value is 1
        for i, val in enumerate(board.get_board()):
            if val == 1:
                # Check that before the click the value is 1
                self.assertEqual(list(board.get_board())[i], 1)
                reward, new_state = board.click(i)
                self.assertEqual(reward, CLICK_REWARD)
                # Check that after the click the value is 0
                self.assertEqual(list(board.get_board())[i], 0)
                # Check the number of 1 values wasn't changed
                self.assertEqual(original_state.count(1), new_state.count(1))
                # Check the new board different
                self.assertNotEqual(original_state, new_state)
                break

    def test_click_value_zero(self):
        board = Board()
        original_state = board.get_board()

        # Choose a location and click it when the value is 0
        for i, val in enumerate(board.get_board()):
            if val == 0:
                reward, new_state = board.click(i)
                self.assertEqual(reward, -MISS_PENALTY)
                # Check the number of 1 values wasn't changed
                self.assertEqual(original_state.count(1), new_state.count(1))
                # Check the new board is the same
                self.assertEqual(original_state, new_state)
                break


if __name__ == '__main__':
    unittest.main()
