
import math
import os
import time

DELAY = 0.1

def main():
    while True:
        for i in range(1, int(math.sqrt(os.get_terminal_size()[0] - 1))):
            print('-' * (i*i))
            time.sleep(DELAY)
        for i in range(int(math.sqrt(os.get_terminal_size()[0] - 1)), 1, -1):
            print('-' * (i*i))
            time.sleep(DELAY)


try:
    main()
except KeyboardInterrupt:
    print('Spike, by Al Sweigart al@inventwithpython.com')
