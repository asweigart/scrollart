import random, os, time

os.system('cls | clear')



WIDTH = os.get_terminal_size()[0] - 1
DELAY = 0.1
EMPTY_CHARS = '/\\_    '
DENSITY = 0.0025
INTERIOR_CHARS = '.                   '
INTERIOR_DENSITY = 1.0
MIN_SIZE = 4
MAX_SIZE = 10

def pr(rows):
    for row in rows:
        print(''.join(row))

r"""
   _______
  /       \
 /         \
/           \
\           / 
 \         /
  \_______/
  _____
 /     \
/       \
\       /
 \_____/
 """
try:
    next_rows = []
    while True:    
        # Make sure there are enough rows in `next_rows`:
        for i in range((MAX_SIZE * 2 + 2) - len(next_rows)):
            next_rows.append([random.choice(EMPTY_CHARS) for i in range(WIDTH)])

        for pos in range(0, WIDTH - (MAX_SIZE * 4 + 1)):
            if random.random() >= DENSITY:
                # Don't create a hexagon here.
                continue

            size = random.randint(MIN_SIZE, MAX_SIZE)

            # Draw new hexagon to next_rows:
            for i in range(pos + 1 + size, pos + 1 + size + (2 * size + 1)):
                next_rows[0][i] = '_'  # Top row of underscores
                next_rows[size * 2][i] = '_'  # Bottom row of underscores
            for i in range(size):
                next_rows[size - i][pos + 1 + i] = '/'  # Top left slashes
                next_rows[size + 1 + i][pos + 1 + i] = '\\'  # Bottom left slashes

                next_rows[size - i][pos + 1 + (size * 3) + 1 + (size - i - 1)] = '\\'  # Top right slashes
                next_rows[size + 1 + i][pos + 1 + (size * 3) + 1 + (size - i - 1)] = '/'  # Bottom right slashes

            if INTERIOR_CHARS is not None:
                # Draw interior characters on inside of hexagon
                for i in range(1, size + 1):
                    for j in range(size - i + 2, size * 3 + 1 + i):
                        if random.random() < INTERIOR_DENSITY:
                            next_rows[i][pos + j] = random.choice(INTERIOR_CHARS)
                        if random.random() < INTERIOR_DENSITY and i != 1:
                            next_rows[size * 2 - i + 1][pos + j] = random.choice(INTERIOR_CHARS)

        # Display the next rows:
        print(''.join(next_rows[0]))
        del next_rows[0]
        time.sleep(DELAY)

except KeyboardInterrupt:
    print('Hex Portals by Al Sweigart al@inventwithpython.com 2024')
