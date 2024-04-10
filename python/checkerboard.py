import os
import time

DELAY = 0.1

def main():
    while True:
        width = os.get_terminal_size()[0] - 1
        lineA = ('      OOOOOO') * (width // 12)
        lineB = ('OOOOOO      ') * (width // 12)

        for i in range(3):
            print(lineA)
            time.sleep(DELAY)

        for i in range(3):
            print(lineB)
            time.sleep(DELAY)

try:
    main()
except KeyboardInterrupt:
    print('Checkerboard, by Al Sweigart al@inventwithpython.com')
