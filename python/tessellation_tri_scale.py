r"""
  \__   \__   \__   \__   \__   \__   \__   \__   \__   \__
__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \
  \     \     \     \     \     \     \     \     \     \
__/   __/   __/   __/   __/   __/   __/   __/   __/   __/
  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/
  /     /     /     /     /     /     /     /     /     /
  \__   \__   \__   \__   \__   \__   \__   \__   \__   \__
__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \


  \__   \__
__/  \__/  \
  \     \
__/   __/
  \__/  \__/
  /     /

"""

import os
import time

DELAY = 0.1

def main():
    while True:
        # -1 because Windows adds newlines if anything
        # is printed in the rightmost column.
        width = os.get_terminal_size()[0] - 1
        segmentWidth = width // 12

        print('  \\__   \\__ ' * segmentWidth)
        time.sleep(DELAY)
        print('__/  \\__/  \\' * segmentWidth)
        time.sleep(DELAY)
        print('  \\     \\   ' * segmentWidth)
        time.sleep(DELAY)
        print('__/   __/   ' * segmentWidth)
        time.sleep(DELAY)
        print('  \\__/  \\__/' * segmentWidth)
        time.sleep(DELAY)
        print('  /     /   ' * segmentWidth)
        time.sleep(DELAY)



try:
    main()
except KeyboardInterrupt:
    print('Tessellation Triangular Scales, by Al Sweigart al@inventwithpython.com')
