import random, time, os


WIDTH = os.get_terminal_size()[0] - 1
DELAY = 0.01

MIN_VERTICAL_SPAN = 10
MAX_VERTICAL_SPAN = 30

EMPTY_CHAR = ' '
STRUT_CHAR = '#'

try:
    while True:
        col = random.randint(0, WIDTH - 1)
        row = [EMPTY_CHAR] * WIDTH
        row[col] = STRUT_CHAR

        row = ''.join(row)
        for i in range(random.randint(MIN_VERTICAL_SPAN, MAX_VERTICAL_SPAN)):
            print(row)
            time.sleep(DELAY)

        # Print horizontal line:
        print(STRUT_CHAR * WIDTH)
        time.sleep(DELAY)

except KeyboardInterrupt:
    print('Vertical Struts by Al Sweigart al@inventwithpython.com 2024')