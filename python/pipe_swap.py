"""
|     |
|     |
|     |
+-----------+
      |     |
   +--+     |
   |        |
   |        |
"""

import random, time

# Use ASCII characters:
HORIZONTAL_PIPE = '-'
VERTICAL_PIPE = '|'
DOWN_RIGHT_ELBOW_PIPE = '+'
DOWN_LEFT_ELBOW_PIPE = '+'
UP_RIGHT_ELBOW_PIPE = '+'
UP_LEFT_ELBOW_PIPE = '+'
EMPTY = ' '

# Use box-drawing characters:

HORIZONTAL_PIPE = chr(9472)  # '─'
VERTICAL_PIPE = chr(9474)  # '│'
DOWN_RIGHT_ELBOW_PIPE = chr(9484)  # '┌'
DOWN_LEFT_ELBOW_PIPE = chr(9488)  # '┐'
UP_RIGHT_ELBOW_PIPE = chr(9492)  # '└'
UP_LEFT_ELBOW_PIPE = chr(9496)  # '┘'
EMPTY = ' '

# Art parameters:
WIDTH = 80
PAUSE = 0.03
NUM_PIPES = 26
SWAP_CHANCE = 0.8
SWAP_MAX_DISTANCE = 20
SWAP_MIN_DISTANCE = 6


# Set up initial pipe locations:
pipes = set()
while len(pipes) < NUM_PIPES:
    pipes.add(random.randint(0, WIDTH - 1))

try:
    # Main loop:
    while True:
        # Start with a blank row:
        row = [EMPTY] * WIDTH

        # Fill in pipes:
        for pipe in pipes:
            row[pipe] = VERTICAL_PIPE


        if random.random() >= SWAP_CHANCE:
            print(''.join(row))
            time.sleep(PAUSE)
            continue  # Don't swap.

        # Select a pipe to swap:
        swap_pipe = random.choice(tuple(pipes))

        # Select new destination column not used by any other pipe:
        destination = random.randint(0, WIDTH - 1)
        while destination in pipes or abs(swap_pipe - destination) > SWAP_MAX_DISTANCE or abs(swap_pipe - destination) < SWAP_MIN_DISTANCE:
            destination = random.randint(0, WIDTH - 1)

        # Update pipes data structure:
        pipes.remove(swap_pipe)
        pipes.add(destination)

        # Check which elbow pipe characters to set:
        if swap_pipe < destination:
            row[swap_pipe] = UP_RIGHT_ELBOW_PIPE
            row[destination] = DOWN_LEFT_ELBOW_PIPE
        else:
            row[swap_pipe] = UP_LEFT_ELBOW_PIPE
            row[destination] = DOWN_RIGHT_ELBOW_PIPE

        # Set horizontal pipe:
        for i in range(min(swap_pipe, destination) + 1, max(swap_pipe, destination)):
            if row[i] == EMPTY or random.random() < 0.5:
                row[i] = HORIZONTAL_PIPE

        # Print the row:
        print(''.join(row))
        time.sleep(PAUSE)

except KeyboardInterrupt:
    print('Pipe Swap, by Al Sweigart al@inventwithpython.com 2025')


