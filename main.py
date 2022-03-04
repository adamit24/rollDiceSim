# Name: Taylor Renee Adami
# Date: 3-3-22
# Project: Weekly Assignment, Rolling dice Simulator
# File: rollingDiceSim -->main.py
# https://realpython.com/python-dice-roll/#demo
#--------------------------------------------------------------------
# -------------- Import Libraries ------------
import time
import random

# --------------- Predefined Variables -------
rollResults = [] # Creates a list to hold the all results of the rolls of the dice.
diceDict = { # Creates the dictionary that holds the art for each value
    1: ('___________',
        '|         |',
        '|    ●    |',
        '|         |',
        '|_________|'),
    2: ('___________',
        '| ●       |',
        '|         |',
        '|       ● |',
        '|_________|'),
    3: ('___________',
        '| ●       |',
        '|    ●    |',
        '|       ● |',
        '|_________|'),
    4: ('___________',
        '| ●     ● |',
        '|         |',
        '| ●     ● |',
        '|_________|'),
    5: ('___________',
        '| ●     ● |',
        '|    ●    |',
        '| ●     ● |',
        '|_________|'),
    6: ('___________',
        '| ●     ● |',
        '| ●     ● |',
        '| ●     ● |',
        '|_________|'),
}
dieHeight = len(diceDict[1]) # Holds the number of rows a side of the die will take up.
dieWidth = len(diceDict[1][0]) # Holds the number of columns requred for the side of the die. This is 11
diceSep = ' ' # Holds white space
# -------------------- Gather and Validate User input ---------------
numDiceInput = int(input('How many Dice do you want to roll? [1 - 6] \n'))

# Create if statement to check for validation or to quit the game ---
if 1 <=numDiceInput <= 6:
    print('Perfect, let\'s roll')
else:
    print('Invalid Option')
    quit()

# Create Timed dialog for the rolling aspect of the game.
time.sleep(1)
print('Rolling...')
time.sleep(1)
print('Rolling...')
time.sleep(1)
print('Rolling...')
time.sleep(1)
# --------------- For loop to roll multiple dice ----------------------
for i in range(numDiceInput):
    roll = random.randint(1, 6) # Create a variable to hold the random roll for 1 through 6
    rollResults.append(roll) # Add the roll to the roll results list.

print(rollResults)
print(diceDict)
