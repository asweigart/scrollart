"""River, by Al Sweigart al@inventwithpython.com
An animation of a winding river.
"""
import random, sys, time
import bext

# Set up the constants:
WIDTH = 70  # (!) Try changing this to 10 or 30.
PAUSE_AMOUNT = 0.05  # (!) Try changing this to 0 or 1.0.

print('River, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to stop.')
time.sleep(2)

leftWidth = 20
gapWidth = 10

while True:
    # Display the left bank of the river:
    print(' ' * leftWidth, end='')

    # Display a row of the river:
    for i in range(gapWidth):
        if random.randint(0, 1) == 0:
            bext.fg('blue')
        else:
            bext.fg('cyan')

        if random.randint(0, 1) == 0:
            print('~', end='')
        else:
            print('-', end='')
    print()

    # Check for Ctrl-C press during the brief pause:
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.

    # Adjust the left side width:
    diceRoll = random.randint(1, 3)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1  # Decrease left side width.
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth = leftWidth + 1  # Increase left side width.
    else:
        pass  # Do nothing; no change in left side width.

    # Adjust the gap width:
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and gapWidth > 1:
        gapWidth = gapWidth - 1  # Decrease gap width.
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        gapWidth = gapWidth + 1  # Increase gap width.
    else:
        pass  # Do nothing; no change in gap width.
