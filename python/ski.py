"""Ski, by Al Sweigart
Use the left/right arrow keys (or A/D keys) to move the skier."""

import bext, time, random

print('Ski, by Al Sweigart')
print('Use the left/right arrow keys (or A/D keys) to move the skier.')
print('Ctrl-C to quit.')
time.sleep(2)

skier = 20
TREE = chr(9650)

bext.bg('white')
direction = 'straight'

while True:
    for i in range(skier):
        if random.randint(1, 100) == 1:
            bext.fg('green')
            print(TREE, end='')
        else:
            print(' ', end='')

    bext.fg('black')
    if direction == 'straight':
        print('||', end='')
    elif direction == 'left':
        print('//', end='')
    elif direction == 'right':
        print('\\\\', end='')

    for i in range(bext.width() - skier - 2):
        if random.randint(1, 100) == 1:
            bext.fg('green')
            print(TREE, end='')
        else:
            print(' ', end='')


    keyPress = bext.getKey(blocking=False)
    if (keyPress == 'left' or keyPress.lower() == 'a') and skier > 0:
        skier -= 1
        direction = 'left'
    elif (keyPress == 'right' or keyPress.lower() == 'd') and skier < bext.width() - 1:
        skier += 1
        direction = 'right'
    else:
        direction = 'straight'

    time.sleep(0.1)
