import random, time, shutil, os

os.system('cls | clear')  # Clear the screen

# Constants for settings:
DELAY = 0.01  # Pause after each row in seconds.
WIDTH = shutil.get_terminal_size()[0] - 1  # Number of columns in output.
NUM_STREAMS = 5  # Number of streams on the screen.
MAX_DISTANCE = NUM_STREAMS * 4  # How many spaces streams must be within each other.
MOVE_CHANCE = 0.75  # How often a stream tries to move left or right, rather than continue straight.

EMPTY_CHAR = ' '
STREAM_CHARS = 'oO@'

"""
SPARK_CHARS = '...,'
SPARK_CHANCE = 0.7
NUM_SPARKS = [1, 1, 1, 2, 3]
SPARK_RANGE = 3  # how many columns outside the leftmost and rightmost streams a spark can appear
"""


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

        """
        # Eh, sparks just don't make it look that good.
        # Add sparks:
        if random.random() < SPARK_CHANCE:
            # Find range where sparks can appear:
            leftmost_spark_column = max(0, min(streams) - SPARK_RANGE)
            rightmost_spark_column = min(WIDTH - 1, max(streams) + SPARK_RANGE)

            # Add sparks:
            for j in range(random.choice(NUM_SPARKS)):
                x = random.randint(leftmost_spark_column, rightmost_spark_column)
                if columns[x] not in STREAM_CHARS:  # Don't overlap a stream with a spark
                    columns[x] = random.choice(SPARK_CHARS)
        """

        print(''.join(columns))
        time.sleep(DELAY)

except KeyboardInterrupt:
    print('Proton Stream, by Al Sweigart al@inventwithpython.com 2024')
