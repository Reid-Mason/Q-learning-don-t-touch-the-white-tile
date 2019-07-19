# Penalty and rewards
MISS_PENALTY = 300
CLICK_REWARD = 25

# Number of squares in the grid
SIZE = 16
# Number of episodes to train for
TRAINING_EPISODES = 5_000

# The rate of decay for "exploration"
EPS_DECAY = 0.9
# How aggressive the learning rate is
LEARNING_RATE = 0.1
# How much to discount the rewards by
DISCOUNT = 0.95

# The mapping of board indexes to the location on the screen of the game board
LOCATION_MAPPING = {0 : (960, 410),
                    1 : (1190, 410),
                    2 : (1420, 410),
                    3 : (1640, 410),

                    4 : (960, 650),
                    5 : (1190, 650),
                    6 : (1420, 650),
                    7 : (1640, 650),

                    8 : (960, 870),
                    9 : (1190, 870),
                    10: (1420, 870),
                    11: (1640, 870),

                    12: (960, 1100),
                    13: (1190, 1100),
                    14: (1420, 1100),
                    15: (1640, 1100),
                    }
