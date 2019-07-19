import qLearningAi

print("Don't touch the white tile Q Learning")

# Give the user options for what they would like to do
choice = input("What would you like to do:\n  1: Train\n  2: Run ai\n")

# Only accept valid inputs of 1 or 2
while choice not in ['1', '2']:
    choice = input("Invalid input. Please enter '1' or '2'.\n")

if choice == '1':
    # This will train the ai using a simulation of the white tile game
    qLearningAi.train()

else:
    # This gets the ai to play the actual web game
    qLearningAi.play()
