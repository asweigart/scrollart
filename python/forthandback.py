import random, time, os, math


WIDTH = os.get_terminal_size()[0] - 1

DELAY = 0.1
BLOCK_CHAR = '#'
BLOCK_HEIGHT = 10
BLOCK_WIDTH = 20
INTERSPACE_HEIGHT = 40

MIN_BOUNCES_PER_CHANGEUP = 1
MAX_BOUNCES_PER_CHANGEUP = 6


def easeOutBounceTween(n):
    if n < (1 / 2.75):
        return 7.5625 * n * n
    elif n < (2 / 2.75):
        n -= 1.5 / 2.75
        return 7.5625 * n * n + 0.75
    elif n < (2.5 / 2.75):
        n -= 2.25 / 2.75
        return 7.5625 * n * n + 0.9375
    else:
        n -= 2.65 / 2.75
        return 7.5625 * n * n + 0.984375

def easeInBounceTween(n):
    return 1 - easeOutBounceTween(1 - n)

try:
    on_left = True
    while True:

        # Bounce to other side:
        if 

except KeyboardInterrupt:
    print('Forth and Back by Al Sweigart al@inventwithpython.com 2024')