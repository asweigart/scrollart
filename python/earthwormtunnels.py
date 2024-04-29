import random, os, time, math

os.system('cls | clear')  # Clear the screen

EMPTY_CHAR = ' '
DIRT_CHARS = '\\/'
WORM_CHAR = ' '
DELAY = 0.02
GROW_BACK_IN = 30
NUM_WORMS = 8
MAX_MOVE = 4

WIDTH = os.get_terminal_size()[0] - 1

columns_growback = [GROW_BACK_IN] * WIDTH

worms = [random.randint(0, WIDTH - 1) for i in range(NUM_WORMS)]

columns = [random.choice(DIRT_CHARS) for i in range(WIDTH)]
for worm in worms:
    columns[worm] = WORM_CHAR

try:
    while True:
        for i, worm in enumerate(worms):
            direction = random.randint(-MAX_MOVE, MAX_MOVE)
            if worm + direction > 0 and worm + direction < WIDTH:
                columns[worm] = EMPTY_CHAR
                columns_growback[worm] = GROW_BACK_IN

                columns[worm + direction] = WORM_CHAR
                worms[i] += direction
        for i in range(len(columns)):
            if columns_growback[i] > 0 and columns[i] == EMPTY_CHAR:
                columns_growback[i] -= 1
            if columns_growback[i] == 0:
                columns[i] = random.choice(DIRT_CHARS)
                columns_growback[i] = GROW_BACK_IN


        print(''.join(columns))
        time.sleep(DELAY)
except KeyboardInterrupt:
    print('Earthworm Tunnels, by Al Sweigart al@inventwithpython.com 2024')