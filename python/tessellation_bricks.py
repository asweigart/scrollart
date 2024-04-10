"""
___|___|___|___|___|
_|___|___|___|___|
___|___|___|___|___|
_|___|___|___|___|
"""

import os
import time

DELAY = 0.1

def main():
    while True:
        # -1 because Windows adds newlines if anything
        # is printed in the rightmost column.
        width = os.get_terminal_size()[0] - 1
        segmentWidth = width // 4
        print('___|' * segmentWidth)
        time.sleep(DELAY)
        print('_|__' * segmentWidth)
        time.sleep(DELAY)


try:
    main()
except KeyboardInterrupt:
    print('Tessellation Bricks, by Al Sweigart al@inventwithpython.com')
