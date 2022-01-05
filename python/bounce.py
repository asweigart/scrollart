"""Bounce, by Al Sweigart al@inventwithpython.com

"""

import os, time, random, bext

PAUSE_AMOUNT = 0.05

NUM_BOUNCERS = 8
ALL_COLORS = ['red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white']
print('Bounce, by Al Sweigart al@inventwithpython.com')
print('Ctrl-C to quit.')
time.sleep(2)

WIDTH = os.get_terminal_size()[0] - 2

# Create the bouncers by filling in the positions, directions, and colors lists:
positions = []
directions = []
colors = []
for i in range(NUM_BOUNCERS):
    directions.append(random.choice(['L', 'R']))

    while True:
        # Keep generating starting positions until you find a position that isn't already taken:
        startingPosition = random.randint(0, WIDTH - 1)
        if startingPosition not in positions:
            positions.append(startingPosition)
            break
    colors.append(random.choice(ALL_COLORS))

while True:
    # Check if anything bounces off each other:
    for i in range(NUM_BOUNCERS):
        for j in range(i + 1, NUM_BOUNCERS):
            if directions[i] == 'L' and directions[j] == 'R' and (positions[i] == positions[j] + 1 or positions[i] == positions[j]):
                directions[i] = 'R'
                directions[j] = 'L'
            elif directions[i] == 'R' and directions[j] == 'L' and (positions[i] == positions[j] - 1 or positions[i] == positions[j]):
                directions[i] = 'L'
                directions[j] = 'R'

    # Bounce off the edges of the terminal window:
    for i in range(NUM_BOUNCERS):
        if positions[i] == 0:
            directions[i] = 'R'
        if positions[i] == WIDTH - 1:
            directions[i] = 'L'

    for i in range(NUM_BOUNCERS):
        if directions[i] == 'L':
            positions[i] -= 1
        elif directions[i] == 'R':
            positions[i] += 1


    # Print the bouncers:
    for x in range(WIDTH):
        bouncerPrinted = False
        for i in range(NUM_BOUNCERS):
            if positions[i] == x:
                bext.fg(colors[i])
                if directions[i] == 'L':
                    print('/', end='')
                elif directions[i] == 'R':
                    print('\\', end='')
                bouncerPrinted = True
                break
        if not bouncerPrinted:
            print(' ', end='')
    print(flush=True)

    time.sleep(PAUSE_AMOUNT)
