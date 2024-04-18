import random, time, os


WIDTH = os.get_terminal_size()[0] - 1
FILL_CHARS = '#@O.:!'
EMPTY_CHARS = ' '
DELAY = 0.004
HEIGHT = 40

SIMULTANEOUS_STRIPES = WIDTH // 10
BLOCK_MODE = False
MAX_WIPES = 99

def get_contiguous_columns_of_length(columns_left, length):
    contiguous_columns = set()
    for i in range(WIDTH):
        if all([i + x in columns_left for x in range(length)]):
            contiguous_columns.add(i)
    return contiguous_columns

try:
    columns = [random.choice(EMPTY_CHARS)] * WIDTH
    makeEmpty = False

    while True:
        columns_left = set(range(WIDTH))
        if makeEmpty:
            new_char = random.choice(EMPTY_CHARS)
        else:
            new_char = random.choice(FILL_CHARS)

        current_wipe_num = 1
        while len(columns_left):
            if current_wipe_num >= MAX_WIPES:
                # change ALL of the remaining columns
                columns = [new_char] * WIDTH
                columns_left = set()
            else:
                if BLOCK_MODE:
                    # Find contiguous columns (at least SIMULTAENOUS_STRIPES in length)
                    for desired_length in range(SIMULTANEOUS_STRIPES, 0, -1):
                        
                        contiguous_columns = get_contiguous_columns_of_length(columns_left, desired_length)
                        #print('desired_length', desired_length)
                        #print('columns_left', columns_left)
                        #print('contiguous_columns', contiguous_columns)
                        if len(contiguous_columns) != 0:
                            break
                    col = random.choice(list(contiguous_columns))

                    # Remove several contiguous columns:
                    #col = random.choice(list(columns_left))
                    for i in range(SIMULTANEOUS_STRIPES):
                        if col + i in columns_left:
                            columns_left.remove(col + i)
                            columns[col + i] = new_char
                else:
                    # Remove several random columns:
                    for i in range(SIMULTANEOUS_STRIPES):
                        if len(columns_left) == 0: break
                        col = random.choice(list(columns_left))
                        columns_left.remove(col)
                        columns[col] = new_char

            # Print columns with the new_char
            for i in range(HEIGHT):
                print(''.join(columns))
                time.sleep(DELAY)

            current_wipe_num += 1
        makeEmpty = not makeEmpty


except KeyboardInterrupt:
    print('Stripe Out by Al Sweigart al@inventwithpython.com 2024')