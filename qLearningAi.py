import json
import os
import pickle

import math
import numpy as np
from board import Board
from gameBoard import GameBoard

from config import CLICK_REWARD, MISS_PENALTY, SIZE, TRAINING_EPISODES, EPS_DECAY, LEARNING_RATE, DISCOUNT


def init_q_table() -> dict:
    """ Create a Q table with randomised Q values

    :return: A Q table initialised with random Q values
    """
    q_table = {}
    for i1 in range(0, SIZE):
        for i2 in range(0, SIZE):
            for i3 in range(0, SIZE):
                # Don't include values where the indexes overlap
                if len({i1, i2, i3}) != 3:
                    continue

                # Create the permutation
                permutation = [0] * SIZE
                permutation[i1] = permutation[i2] = permutation[i3] = 1
                # Initialise Q table with random values for each permutation
                q_table[tuple(permutation)] = [np.random.uniform(-5, 0) for i in range(SIZE)]

    return q_table


def start_q_table(filename: str = None) -> dict:
    """ Starts the Q table. This could mean loading from a file or generating a table with random values.

    :param filename: The filename of the table to load
    :return: Either a new random Q table or a previously saved Q table
    """
    if not os.path.exists(filename):
        print("The provided Q table file doesn't exist. Generating a new Q table.")
        return init_q_table()

    if filename is None:
        # Initialise a random Q table
        return init_q_table()

    # Load a saved q_table
    with open(filename, "rb") as f:
        return pickle.load(f)


def choose_action(q_table: dict, state: tuple, epsilon: float = None) -> int:
    """ Gets the square that the Q table thinks is the right one to click.

    Epsilon will allow the ai to "explore" by performing random moves.

    :param q_table: The Q table currently being used
    :param state: The current state of the board
    :param epsilon: The chance that "exploration" takes place
    :return: The index location on the board to be clicked
    """
    if epsilon is not None and np.random.random() < epsilon:
        return np.random.randint(0, SIZE)

    return int(np.argmax(q_table[state]))


def get_new_q(reward: int, current_q: float, max_future_q: float) -> float:
    """ Calculates the new Q value for the action just taken.

    :param reward: The reward received from the last action
    :param current_q: The Q value of the last action taken
    :param max_future_q: The highest Q value for the next action
    :return: The new Q value for the action previously taken
    """
    # Apply click reward
    if reward == CLICK_REWARD:
        return float(CLICK_REWARD)

    # Apply miss penalty
    elif reward == -MISS_PENALTY:
        return float(-MISS_PENALTY)

    # Apply learning formula
    else:
        return (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)


def train():
    """ Trains the ai using a simulated version of the web game to decrease time on each episode """
    epsilon = 0.9
    SHOW_EVERY = math.ceil(TRAINING_EPISODES / 20)
    q_table = start_q_table('qtable.pickle')

    # Start learning loop
    episode_rewards = []
    for episode in range(TRAINING_EPISODES):
        # Create new board
        board = Board()

        # Logging the progress
        if not episode % SHOW_EVERY:
            latest_rewards = episode_rewards[-SHOW_EVERY:] if len(episode_rewards[-SHOW_EVERY:]) > 0 else [0]
            print(f'Episode {episode} - mean: {np.mean(latest_rewards)} epsilon: {epsilon}')

        episode_reward = 0
        for _ in range(100):
            state = board.get_board()

            # Decide on action
            action = choose_action(q_table, state, epsilon)

            # Make the action
            reward, new_state = board.click(action)
            episode_reward += reward

            # Calculate the new Q value
            new_q = get_new_q(reward, q_table[state][action], np.max(q_table[new_state]))
            q_table[state][action] = new_q

        # Add this episodes rewards to the rewards table
        episode_rewards.append(episode_reward)
        epsilon *= EPS_DECAY

    # Save the new Q table
    with open(f'qtable.pickle', "wb") as f:
        pickle.dump(q_table, f)


def play():
    """ Plays the actual game on the web with the learned data. """
    q_table = start_q_table('qtable.pickle')
    board = GameBoard()
    state = board.get_board()

    for _ in range(100):
        # Decide on action
        action = choose_action(q_table, state)
        state, done = board.click(action)

        if done:
            print('Game over!')
            return
