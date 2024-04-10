import os
import time

DELAY = 0.1

def main():
    while True:
        # -1 because Windows adds newlines if anything
        # is printed in the rightmost column.
        width = os.get_terminal_size()[0] - 1
        for i in range(7):
            prefix = ' ' * i
            suffix = ' ' * (6 - i)
            line = (prefix + 'OOOOOO' + suffix) * ((width - 7) // 12)
            print(line)
            time.sleep(DELAY)

try:
    main()
except KeyboardInterrupt:
    print('Diagonal Checkerboard, by Al Sweigart al@inventwithpython.com')
