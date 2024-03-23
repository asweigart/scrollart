"""

"""

import random, time, shutil, os

os.system('cls | clear')  # Clear the screen

DELAY = 0.01
WIDTH = shutil.get_terminal_size()[0] - 1
NUM_STREAMS = 5  # Number of streams on the screen.
MAX_DISTANCE = NUM_STREAMS * 4  # How many spaces streams must be within each other.

MOVE_CHANCE = 0.75  # How often a stream tries to move left or right, rather than continue straight.

EMPTY_CHAR = ' '
STREAM_CHARS = ['o', 'O', '@']

streams = [WIDTH // 2] * NUM_STREAMS


try:
    while True:
        columns = [EMPTY_CHAR] * WIDTH

        for i, stream in enumerate(streams):
            if random.random() < MOVE_CHANCE:
                # Move stream:
                if random.random() < 0.5:  # There seems to be some bias to random.random() where 0.5 doesn't work as a 50/50?
                    if stream > 0 and all([abs((stream - 1) - other) <= MAX_DISTANCE for other in streams]):
                        # Move stream left:
                        streams[i] -= 1
                else:
                    if stream < WIDTH - 1 and all([abs((stream + 1) - other) <= MAX_DISTANCE for other in streams]):
                        # Move stream right:
                        streams[i] += 1

        for i, stream in enumerate(streams):
            columns[stream] = STREAM_CHARS[i % len(STREAM_CHARS)]

        print(''.join(columns))
        time.sleep(DELAY)

except KeyboardInterrupt:
    print('Proton Stream, by Al Sweigart al@inventwithpython.com')
