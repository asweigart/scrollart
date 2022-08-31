r"""
  /\    /\
_/  \__/  \_
\    /\    /
 \__/  \__/
  /\    /\
_/  \__/  \_
\    /\    /
 \__/  \__/


  /\    /\
_/  \__/  \_
\    /\    /
 \__/  \__/
 _/\_  _/\_
 \__/  \__/
  /\    /\
_/  \__/  \_
\    /\    /
 \__/  \__/

  /\
_/  \_
\    /
 \__/
 _/\_
 \__/

"""

import time, os

DELAY = 0.1

def main():
    while True:
        # -1 because Windows adds newlines if anything
        # is printed in the rightmost column.
        width = os.get_terminal_size()[0] - 1
        segmentWidth = width // 6
        #print('___|' * segmentWidth)
        #time.sleep(DELAY)
        #print('_|__' * segmentWidth)
        #time.sleep(DELAY)
        print(r'  /\  ' * segmentWidth)
        time.sleep(DELAY)
        print(r'_/  \_' * segmentWidth)
        time.sleep(DELAY)
        print(r'\    /' * segmentWidth)
        time.sleep(DELAY)
        print(r' \__/ ' * segmentWidth)
        time.sleep(DELAY)
        print(r' _/\_ ' * segmentWidth)
        time.sleep(DELAY)
        print(r' \__/ ' * segmentWidth)
        time.sleep(DELAY)


try:
    main()
except KeyboardInterrupt:
    print('Tessellation Bricks, by Al Sweigart al@inventwithpython.com')
