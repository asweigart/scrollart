import random, os, time

WIDTH = os.get_terminal_size()[0] - 1
DELAY = 0.0075
AFTER_TOWER_DELAY = 0.75

EMPTY_CHAR = ' '
CORNER_CHAR = '+'
TOP_CHAR = '-'
SIDE_CHAR = '|'
INTERIOR_CHARS = ':|. '

MIN_TOWER_WIDTH = 8
MAX_TOWER_WIDTH = 20

MIN_TOWER_HEIGHT = 4
MAX_TOWER_HEIGHT = 17

TOWER_HEIGHT_MAX_DIFF = 8

WIPE_AFTER = 8


try:
    step = 1
    columns = [EMPTY_CHAR] * WIDTH
    while True:
        if step % WIPE_AFTER == 0:
            for i in range(60):
                print()
                time.sleep(DELAY)
            time.sleep(AFTER_TOWER_DELAY)
            columns = [EMPTY_CHAR] * WIDTH

        # Tower 1 top (tower 1 is slightly higher than tower 2):
        tower1_left = random.randint(0, (WIDTH // 2) - MAX_TOWER_WIDTH)
        tower1_width = random.randint(MIN_TOWER_WIDTH, MAX_TOWER_WIDTH)
        columns[tower1_left] = CORNER_CHAR
        columns[tower1_left + tower1_width] = CORNER_CHAR
        for i in range(tower1_left + 1, tower1_left + tower1_width):
            columns[i] = TOP_CHAR

        print(''.join(columns))
        time.sleep(DELAY)

        # Tower 1 top body that is above tower 2's top:
        columns[tower1_left] = SIDE_CHAR
        columns[tower1_left + tower1_width] = SIDE_CHAR
        interior_char = INTERIOR_CHARS[step % len(INTERIOR_CHARS)]#random.choice(INTERIOR_CHARS)
        for i in range(tower1_left + 1, tower1_left + tower1_width):
            columns[i] = interior_char

        for i in range(random.randint(1,TOWER_HEIGHT_MAX_DIFF)):
            print(''.join(columns))
            time.sleep(DELAY)
        
        # Tower 2 top:
        tower2_left = random.randint(0, WIDTH - MAX_TOWER_WIDTH)
        tower2_width = random.randint(MIN_TOWER_WIDTH, MAX_TOWER_WIDTH)
        columns[tower2_left] = CORNER_CHAR
        columns[tower2_left + tower2_width] = CORNER_CHAR
        for i in range(tower2_left + 1, tower2_left + tower2_width):
            columns[i] = TOP_CHAR
        
        print(''.join(columns))
        time.sleep(DELAY)

        # Tower 2 body (and 1):
        columns[tower2_left] = SIDE_CHAR
        columns[tower2_left + tower2_width] = SIDE_CHAR
        interior_char = INTERIOR_CHARS[step % len(INTERIOR_CHARS)]#random.choice(INTERIOR_CHARS)
        for i in range(tower2_left + 1, tower2_left + tower2_width):
            columns[i] = interior_char


        for i in range(random.randint(MIN_TOWER_HEIGHT, MAX_TOWER_HEIGHT)):
            print(''.join(columns))
            time.sleep(DELAY)

        time.sleep(AFTER_TOWER_DELAY)
        step += 1
        



except KeyboardInterrupt:
    print('Towers and Towers by Al Sweigart al@inventwithpython.com 2024')