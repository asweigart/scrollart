import os, random, time, math

WIDTH = os.get_terminal_size()[0] - 1
DELAY = 0.008

NUM_COLUMNS = 5
COLUMN_WIDTH = 4

COLUMN_CHAR = '@'
EMPTY_CHAR = ' '

GAP_SIZE = (WIDTH - COLUMN_WIDTH) // (NUM_COLUMNS + 1)
BETWEEN_TWIST_LENGTH = 0
TWIST_LENGTH = 50

SINE_STEP_INC = (math.pi / 2) / TWIST_LENGTH

try:
    while True:
        # Set up straight columns:
        columns = [EMPTY_CHAR] * WIDTH
        i = GAP_SIZE
        for i in range(1, NUM_COLUMNS + 1):
            for j in range(COLUMN_WIDTH):
                columns[(i * GAP_SIZE) + j] = COLUMN_CHAR

        # Print straight columns:
        for i in range(BETWEEN_TWIST_LENGTH):
            print(''.join(columns))
            time.sleep(DELAY)

        # Select two adjacent columns to twist:
        to_twist = random.randint(1, NUM_COLUMNS - 1)
        
        
        for sine_step in range(TWIST_LENGTH):
            columns = [EMPTY_CHAR] * WIDTH

            in_transit_pos_left  = (to_twist     * GAP_SIZE) + int(math.sin(sine_step * SINE_STEP_INC) * GAP_SIZE)
            in_transit_pos_right = ((to_twist+1) * GAP_SIZE) - int(math.sin(sine_step * SINE_STEP_INC) * GAP_SIZE)
            for j in range(COLUMN_WIDTH):
                columns[in_transit_pos_left + j] = '@'
                columns[in_transit_pos_right + j] = '@'

            # Print straight columns (that are not being twisted currently):
            i = GAP_SIZE
            for i in range(1, NUM_COLUMNS + 1):
                if i == to_twist or i == to_twist + 1:
                    continue
                for j in range(COLUMN_WIDTH):
                    columns[(i * GAP_SIZE) + j] = COLUMN_CHAR
                

            print(''.join(columns))
            time.sleep(DELAY)            

except KeyboardInterrupt:
    print('Twists, by Al Sweigart al@inventwithpython.com 2024')

