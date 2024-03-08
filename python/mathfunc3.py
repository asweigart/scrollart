import os, sys, time

# Constants for the block characters used to represent pixels:
TOP_BLOCK    = chr(9600)
BOTTOM_BLOCK = chr(9604)
FULL_BLOCK   = chr(9608)

DELAY = 0.05
FUNC = eval('lambda x, y: (x | y) % 7')


y = 0
while True:
    width = os.get_terminal_size()[0] - 2
    for x in range(width):
        topBit = FUNC(x, y)
        bottomBit = FUNC(x, y + 1)

        # Patterns often look better if we use True for the black pixels:
        topBit = not topBit
        bottomBit = not bottomBit

        if topBit and bottomBit:
            print(FULL_BLOCK, end='')
        elif topBit and not bottomBit:
            print(TOP_BLOCK, end='')
        elif not topBit and bottomBit:
            print(BOTTOM_BLOCK, end='')
        else:
            print(' ', end='')
    print(flush=True)

    y += 2
    time.sleep(DELAY)