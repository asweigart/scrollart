import random, os, shutil, time

os.system('cls | clear')  # Clear the screen


"""
0
┌┐
└┘

1
┌──┐
│  │
└──┘

2
┌────┐
│    │
│    │
└────┘

3
┌──────┐
│      │
│      │
│      │
│      │
└──────┘


"""


# Constants for settings:
DELAY = 0.1  # Pause after each row in seconds.
WIDTH = shutil.get_terminal_size()[0] - 1  # Number of columns in output.
MIN_SQUARE_SIZE = 1
MAX_SQUARE_SIZE = 7
CHANCE_OF_FILLED_SQUARE = 0.0
NUM_SQUARES_PER_ROW = 3

UP_DOWN_CHAR         = chr(9474)  # Character 9474 is '│'
LEFT_RIGHT_CHAR      = chr(9472)  # Character 9472 is '─'
DOWN_RIGHT_CHAR      = chr(9484)  # Character 9484 is '┌'
DOWN_LEFT_CHAR       = chr(9488)  # Character 9488 is '┐'
UP_RIGHT_CHAR        = chr(9492)  # Character 9492 is '└'
UP_LEFT_CHAR         = chr(9496)  # Character 9496 is '┘'

UP_DOWN_RIGHT_CHAR   = chr(9500)  # Character 9500 is '├'
UP_DOWN_LEFT_CHAR    = chr(9508)  # Character 9508 is '┤'
DOWN_LEFT_RIGHT_CHAR = chr(9516)  # Character 9516 is '┬'
UP_LEFT_RIGHT_CHAR   = chr(9524)  # Character 9524 is '┴'
CROSS_CHAR           = chr(9532)  # Character 9532 is '┼'

 
EMPTY = ' ' * 25 + '...,' + chr(9633)  # The characters in this string are used to fill outside the squares.
SQUARE_INTERIOR = ' '  # The characters in this string are used to fill the square interiors.
#SQUARE_INTERIOR = '1234567890ABCDEF'  # Uncomment this for a hackery-data look.


def get_outline_square(size):
    assert size >= 0
    
    rows = []
    # Make the top row of the square:
    rows.append(DOWN_RIGHT_CHAR + (LEFT_RIGHT_CHAR * (size * 2)) + DOWN_LEFT_CHAR)

    # Make the middle segment of the square:
    for i in range(size):
        rows.append(UP_DOWN_CHAR + (''.join([random.choice(SQUARE_INTERIOR) for i in range((size * 2))])) + UP_DOWN_CHAR)

    # Make the bottom row of the square:
    rows.append(UP_RIGHT_CHAR + (LEFT_RIGHT_CHAR * (size * 2)) + UP_LEFT_CHAR)

    return rows


def get_filled_square(size):
    assert size >= 0
    
    rows = []
    # Make the top row of the square:
    rows.append(DOWN_RIGHT_CHAR + (DOWN_LEFT_RIGHT_CHAR * (size * 2)) + DOWN_LEFT_CHAR)

    # Make the middle segment of the square:
    for i in range(size):
        rows.append(UP_DOWN_RIGHT_CHAR + (CROSS_CHAR * (size * 2)) + UP_DOWN_LEFT_CHAR)

    # Make the bottom row of the square:
    rows.append(UP_RIGHT_CHAR + (UP_LEFT_RIGHT_CHAR * (size * 2)) + UP_LEFT_CHAR)

    return rows



"""
# Debug, see returned values from diamond functions:
d = get_filled_diamond(4)
for row in d:
    for char in row:
        if char is None:
            print(' ', end='')
        else:
            print(char, end='')
    print()
import sys; sys.exit()
"""

try:
    next_rows = []
    while True:
        for j in range(NUM_SQUARES_PER_ROW):
            size = random.randint(MIN_SQUARE_SIZE, MAX_SQUARE_SIZE)

            if random.random() < CHANCE_OF_FILLED_SQUARE:
                square = get_filled_square(size)
            else:
                square = get_outline_square(size)

            x_start = random.randint(0, WIDTH - 1 - (size * 2 + 2))

            # Make sure there are enough rows in `next_rows`:
            if len(next_rows) < size + 2:
                for k in range(((size + 2) - len(next_rows))):
                    next_rows.append([random.choice(EMPTY) for i in range(WIDTH)])

            # Add the square to `next_rows`
            for y, row in enumerate(square):
                for x, char in enumerate(row):
                    next_rows[y][x + x_start] = char

        # Print the row and then remove it:
        print(''.join(next_rows[0]))
        del next_rows[0]
        time.sleep(DELAY)

except KeyboardInterrupt:
    print('Diamond Sky, by Al Sweigart al@inventwithpython.com 2024')



