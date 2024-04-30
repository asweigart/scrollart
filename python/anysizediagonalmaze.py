# Any Size Diagonal Maze

import random, time, os

os.system('cls | clear')  # Clear the screen

MAZE_SIZE = 4

WIDTH = os.get_terminal_size()[0] - 1
DELAY = 0.1

EMPTY = ' '
FORWARD_SLASH = chr(9585)
BACK_SLASH = chr(9586)

try:
    columns = [FORWARD_SLASH] * (WIDTH // MAZE_SIZE)
    while True:
        # Set up the slashes in columns:
        for i in range(len(columns)):
            if random.randint(0, 1) == 0:
                columns[i] = FORWARD_SLASH
            else:
                columns[i] = BACK_SLASH

        # Print the columns:
        for row_num in range(MAZE_SIZE):
            for i in range(len(columns)):
            
                if columns[i] == FORWARD_SLASH:
                    print(EMPTY * (MAZE_SIZE - row_num - 1) + FORWARD_SLASH + EMPTY * (row_num), end='')
                elif columns[i] == BACK_SLASH:
                    print(EMPTY * (row_num) + BACK_SLASH + EMPTY * (MAZE_SIZE - row_num - 1), end='')
            print()
            time.sleep(DELAY)
except KeyboardInterrupt:
    print('Any Size Diagonal Maze, by Al Sweigart al@inventwithpython.com 2024')

