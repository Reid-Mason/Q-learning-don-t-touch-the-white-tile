import unittest
import qLearningAi
from config import CLICK_REWARD, MISS_PENALTY, SIZE


class TestQLearningAi(unittest.TestCase):
    def test_init_q_table(self):
        q_table = qLearningAi.init_q_table()

        # Check the Q table is 560 entries long
        self.assertEqual(len(q_table), 560)

        # Check the Q table is a dictionary
        self.assertEqual(type(q_table), dict)

        # Check the Q table permutations are the right length
        for permutation in q_table.values():
            self.assertEqual(len(permutation), SIZE)

        # Check the Q table Q values are the right length
        for values in q_table.keys():
            self.assertEqual(len(values), SIZE)

    def test_choose_action(self):
        q_table = qLearningAi.init_q_table()
        board_state = tuple([1] * 3 + [0] * (SIZE - 3))
        action = qLearningAi.choose_action(q_table, board_state)

        # Check the action is int
        self.assertEqual(type(action), int)

        # Check the action is within the size limit
        self.assertLessEqual(action, SIZE)

    def test_get_new_q(self):
        # Check the new Q if the reward was the click reward
        new_q = qLearningAi.get_new_q(CLICK_REWARD, -1, -1)
        # Check the returned type is a float
        self.assertEqual(type(new_q), float)
        # Check the neq Q value is equal to click reward
        self.assertEqual(new_q, CLICK_REWARD)

        # Check the new Q if the reward was the miss penalty
        new_q = qLearningAi.get_new_q(-MISS_PENALTY, -1, -1)
        # Check the returned type is a float
        self.assertEqual(type(new_q), float)
        # Check the neq Q value is equal to click reward
        self.assertEqual(new_q, -MISS_PENALTY)

        # Check the new Q if the reward was neither the click reward or miss penalty
        new_q = qLearningAi.get_new_q(-1, -1, -1)
        # Check the returned type is a float
        self.assertEqual(type(new_q), float)


if __name__ == '__main__':
    unittest.main()
