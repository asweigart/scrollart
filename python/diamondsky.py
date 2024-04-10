# Code adapted from my diamonds.py program here: https://inventwithpython.com/bigbookpython/project16.html

import random, os, shutil, time

os.system('cls | clear')  # Clear the screen

# Constants for settings:
DELAY = 0.1  # Pause after each row in seconds.
WIDTH = shutil.get_terminal_size()[0] - 1  # Number of columns in output.
MIN_DIAMOND_SIZE = 1
MAX_DIAMOND_SIZE = 8

CHANCE_FOR_FILLED_DIAMOND = 0.3  # Set between 0.0 and 1.0

NUM_DIAMONDS_PER_ROW = 2

EMPTY = '                ...,'  # The characters in this string are used to fill outside the squares.

def get_outline_diamond(size):
    assert size > 0
    rows = []
    # Make the top half of the diamond:
    for i in range(size):
        rows.append(([None] * (size - i - 1)) + ['/'] + ([' '] * (i * 2)) + ['\\'])

    # Make the bottom half of the diamond:
    for i in range(size):
        rows.append(([None] * i) + ['\\'] + ([' '] * ((size - i - 1) * 2)) + ['/'])
    return rows


def get_filled_diamond(size):
    assert size > 0
    rows = []
    # Make the top half of the diamond:
    for i in range(size):
        rows.append(([None] * (size - i - 1)) + (['/'] * (i + 1)) + (['\\'] * (i + 1)))
        
    # Make the bottom half of the diamond:
    for i in range(size):
        rows.append(([None] * i) + (['\\'] * (size - i)) + (['/'] * (size - i)))
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
        for j in range(NUM_DIAMONDS_PER_ROW):
            size = random.randint(MIN_DIAMOND_SIZE, MAX_DIAMOND_SIZE)

            if random.random() < CHANCE_FOR_FILLED_DIAMOND:
                diamond = get_filled_diamond(size)
            else:
                diamond = get_outline_diamond(size)

            x_start = random.randint(0, WIDTH - 1 - (size * 2))

            # Make sure there are enough rows in `next_rows`:
            while len(next_rows) < size * 2:
                next_rows.append([random.choice(EMPTY) for i in range(WIDTH)])

            # Add the diamond to `next_rows`
            for y, row in enumerate(diamond):
                for x, char in enumerate(row):
                    if char is None:
                        continue  # Don't print anything for the None "characters"; this is effectively a transparent space in the diamond.
                    next_rows[y][x + x_start] = char

        # Print the row and then remove it:
        print(''.join(next_rows[0]))
        del next_rows[0]
        time.sleep(DELAY)

except KeyboardInterrupt:
    print('Diamond Sky, by Al Sweigart al@inventwithpython.com')
