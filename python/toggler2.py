import os
import random
import time

"""
In this program, the togglers start in a random column and move
left AND right forming an equilateral triangle pattern.
"""

DELAY = 0.05
TOGGLER_DENSITY = 10

RIGHT_INCREMENT = 3  # Try changing this to a different integer.
LEFT_INCREMENT = RIGHT_INCREMENT * -1

def main():
    # -1 because Windows adds newlines if anything
    # is printed in the rightmost column.
    width = os.get_terminal_size()[0] - 1

    columnChars = ['.'] * width
    togglers = [] # Tuple of (x position, direction moving)

    while True:
        width = os.get_terminal_size()[0] - 1

        if random.randint(0, 99) < TOGGLER_DENSITY:
            # Add two new togglers
            position = random.randint(0, width)
            togglers.append([position - RIGHT_INCREMENT, LEFT_INCREMENT])
            togglers.append([position, RIGHT_INCREMENT])

        # Remove out of bounds togglers:
        for i in range(len(togglers) - 1, -1, -1):
            if togglers[i][0] < 0 or togglers[i][0] >= width:
                del togglers[i]

        # Move the togglers and toggler the column chars:
        for i in range(len(togglers)):
            togglerPosition = togglers[i][0]
            togglerDirection = togglers[i][1]

            if columnChars[togglerPosition] == '.':
                columnChars[togglerPosition] = '@'
            else:
                columnChars[togglerPosition] = '.'

            togglers[i][0] += togglerDirection  # move the toggler

        print(''.join(columnChars))
        time.sleep(DELAY)

try:
    main()
except KeyboardInterrupt:
    print('Toggler 1, by Al Sweigart al@inventwithpython.com')
