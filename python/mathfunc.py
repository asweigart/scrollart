r"""Math Func, by Al Sweigart al@inventwithpython.com
Displays the visual output of a function. The function accepts two int
arguments for the x and y parameters, and displays pixels if the function
returns True.

Example (Windows):
C:\>python mathfunc.py "(x ^ y) % 5"
C:\>python mathfunc.py "(x & y) & (x ^ y) % 19"

Example (macOS and Linux):
$ python3 mathfunc.py "(x ^ y) % 5"
$ python3 mathfunc.py "(x & y) & (x ^ y) % 19"
"""

import os, sys, time

# Constants for the block characters used to represent pixels:
TOP_BLOCK    = chr(9600)
BOTTOM_BLOCK = chr(9604)
FULL_BLOCK   = chr(9608)

PAUSE_AMOUNT = 0.05

if len(sys.argv) == 1:
    funcStr = '(x ^ y) % 5'  # Use this as the default function.
else:
    funcStr = sys.argv[1]


# A vague attempt at mitigating malicious input since func is passed to eval(). Don't rely on this for security.
if ';' in funcStr or 'import' in funcStr or 'open' in funcStr:
    raise Exception('funcStr argument as a string must only have a lambda function')

if not funcStr.strip().replace(' ', '').lower().startswith('lambdax,y:'):
    funcStr = 'lambda x, y:' + funcStr
func = eval(funcStr)


print('Math Func, by Al Sweigart al@inventwithpython.com')
print('Ctrl-C to quit.')
time.sleep(2)

y = 0
while True:
    width = os.get_terminal_size()[0] - 2
    for x in range(width):
        topBit = func(x, y)
        bottomBit = func(x, y + 1)

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
    time.sleep(PAUSE_AMOUNT)