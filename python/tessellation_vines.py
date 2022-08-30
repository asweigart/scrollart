"""
((  )((  )((  )((  )((  )((  )((  )((  )((  )((  )((  )((  )
 ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(
((  )((  )((  )((  )((  )((  )((  )((  )((  )((  )((  )((  )
 ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(
((  )((  )((  )((  )((  )((  )((  )((  )((  )((  )((  )((  )
 ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(
"""

import time, os

DELAY = 0.1

def main():
    while True:
        # -1 because Windows adds newlines if anything
        # is printed in the rightmost column.
        width = os.get_terminal_size()[0] - 1
        segmentWidth = width // 9
        print('((    )  ' * segmentWidth)
        time.sleep(DELAY)
        print(' ))  (   ' * segmentWidth)
        time.sleep(DELAY)


try:
    main()
except KeyboardInterrupt:
    print('Tessellation Vines, by Al Sweigart al@inventwithpython.com')
