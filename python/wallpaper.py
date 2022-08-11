"""Wallpaper, by Al Sweigart al@inventwithpython.com"""

import os, time, random

PAUSE_AMOUNT = 0.05

print('Wallpaper, by Al Sweigart al@inventwithpython.com')
print('Ctrl-C to quit.')
time.sleep(2)

bigHex = []
bigHex.append(r' /   \    ')
bigHex.append(r'/     \___')
bigHex.append(r'\     /   ')
bigHex.append(r' \___/    ')

innerHex = []
innerHex.append(r' / __ \ \__/')
innerHex.append(r'/ /  \ \____')
innerHex.append(r'\ \__/ / __ ')
innerHex.append(' \\____/ /  \\')  # Python can't have raw strings that end with a backslash (weird bug)

tri = []
tri.append(r'\__   ')
tri.append(r'/  \__')
tri.append(r'\     ')
tri.append(r'/   __')
tri.append(r'\__/  ')
tri.append(r'/     ')

skull = []
skull.append(r'/ ___ \ ^ ')
skull.append(r' /   \ VVV')
skull.append(r'|() ()|   ')
skull.append(r' \ ^ / ___')
skull.append(r'\ VVV /   ')
skull.append(r')|   |() (')

patterns = [bigHex, innerHex, tri, skull
]

i = 0
patternNum = 3
while True:
    #if random.randint(1, 1000) == 1:
    #    patternNum = random.randint(0, len(patterns) - 1)


    width = os.get_terminal_size()[0]

    currentPattern = patterns[patternNum]
    currentLine = currentPattern[i % len(currentPattern)]
    x = 0
    while x < width - 1:
        print(currentLine[x % len(currentLine)], end='')
        x += 1
    i += 1
    print(flush=True)
    time.sleep(PAUSE_AMOUNT)





r"""




"""