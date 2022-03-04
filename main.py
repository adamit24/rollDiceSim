# Name: Taylor Renee Adami
# Date: 3-3-22
# Project: Weekly Assignment, Rolling dice Simulator
# File: rollingDiceSim -->main.py
# https://realpython.com/python-dice-roll/#demo
#--------------------------------------------------------------------
# -------------- Import Libraries ------------
import time
import random

# ---- Creating a function ------------------
def genDiceFace(diceValues): # Defines a function that generates the dice faces based off of the values in the dictionary
    # Generate a list of dice face from diceDict
    diceFaces = [] # Creates an empty list for the diceFaces based off the dice values w
    for value in diceValues: # starts the for loops
        diceFaces.append(diceDict[value]) # retrieves the die face value from the dictionary key

    # Generate a list containing the dice face rows
    diceFaceRows = [] # Creates an empty list to hold the rows for the dice diagrams
    for rowIdx in range(dieHeight): # Row Index, each index represents the index of a given row in the dice faces
        rowComponents = [] # Creates empty list to hold the dice faces that fill a given rom
        for die in diceFaces: # starts the for loop to iterate over the dice faces
            rowComponents.append(die[rowIdx]) # Stores each row Component
        rowString = diceSep.join(rowComponents) # Joins the row ompoenets together into a final string, separing with spaces
        diceFaceRows.append(rowString) # Creates the final diagram

    # Generate header with the word 'Results' centered
    width = len(diceFaceRows[0]) # Creates a temporary variable to hold the width of the current dice faces
    diagramHeader = ' RESULTS '.center(width, '~')

    diceFaceDiagram = '\n'.join([diagramHeader] + diceFaceRows)
    return diceFaceDiagram
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
dieWidth = len(diceDict[1][0]) # Holds the number of columns required for the side of the die. This is 11
diceSep = ' ' # Holds white space
while True:
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

    # generate the ASCII diagram of dice faces
    diceFaceDiagram = genDiceFace(rollResults)


    print(f'\n{diceFaceDiagram}')

    rollResults.clear()

# Extra practice:
# 1)
# Create an infinite loop so that it will continue to ask the user to roll dice.
# You may come into some problems with the list, because It will continue updating the list before.
# You will need to clear the list at the end of the program

# 2)
# Create your program to support any number of rolling dice.
# Allow the user to be able to choose more than six dice

# 3) 
# Support for dice with different number of faces. 
# Create the code to support not only six sided dice. 
# allow for 20, 10, etc,
