r"""
   ______
  /     /\
 /     /  \
/_____/    \
\     \    /
 \     \  /
  \     \/

   ______
  /     /\
 /     /\\\
/_____/\\\\\
\     \\\\\/
 \     \\\/
  \     \/

   ______
  /     /\
 /     ///\
/_____/////\
\     \/////
 \     \///
  \     \/
   ______
  ///////\
 ///////  \
/_/_/_/    \
\     \    /
 \     \  /
  \     \/

   ______
  /     /\
 /     /  \
/_____/    \
\\\\\\\    /
 \\\\\\\  /
  \_\_\_\/

   ______
  ///////\
 ///////  \
/_/_/_/    \
\\\\\\\    /
 \\\\\\\  /
  \_\_\_\/

   ______
  /     /\
 /     ///\
/_____/////\
\\\\\\\/////
 \\\\\\\///
  \_\_\_\/

   ______
  /     /\
 /     /\\\
/_____/\\\\\
\\\\\\\\\\\/
 \\\\\\\\\/
  \_\_\_\/

   ______
  ///////\
 /////////\
/_/_/_/////\
\     \/////
 \     \///
  \     \/

   ______
  ///////\
 ///////\\\
/_/_/_/\\\\\
\     \\\\\/
 \     \\\/
  \     \/


   ______
  /     /\
 /  TOP/  \
/_____/SIDE\
\     \    /
 \BOTM \  /
  \     \/
"""


# TODO - for now, we'll just leave side 2 always unshaded, because it's tricky to correctly shade it.
r"""
  /     /\     \SID2/
 /TOP1 /  \BTM2 \  /
/_____/SID1\_____\/
\     \    /     /\
 \BTM1 \  /TOP2 /  \
  \_____\/_____/SID2\
"""

import os, time, random

DELAY = 0.1

def main():
    density = 35

    while True:
        # -1 because Windows adds newlines if anything
        # is printed in the rightmost column.
        width = os.get_terminal_size()[0] - 1
        segmentWidth = width // 21

        row1 = []
        row2 = []
        row3 = []
        row4 = []
        row5 = []
        row6 = []



        for i in range(segmentWidth):

            if random.randint(0, 99) < density:
                top1Shading = '/////'
                top1ShadingBottom = '_/_/_'
            else:
                top1Shading = '     '
                top1ShadingBottom = '_____'
            if random.randint(0, 99) < density:
                top2Shading = '/////'
                top2ShadingBottom = '_/_/_'
            else:
                top2Shading = '     '
                top2ShadingBottom = '_____'
            if random.randint(0, 99) < density:
                bottom1Shading = '\\\\\\\\\\'
                bottom1ShadingBottom = '_\\_\\_'
            else:
                bottom1Shading = '     '
                bottom1ShadingBottom = '_____'
            if random.randint(0, 99) < density:
                bottom2Shading = '\\\\\\\\\\'
                bottom2ShadingBottom = '_\\_\\_'
            else:
                bottom2Shading = '     '
                bottom2ShadingBottom = '_____'

            if random.randint(0, 99) < density:
                if random.randint(0, 1):
                    side1Shading = '\\\\'
                else:
                    side1Shading = '//'
            else:
                side1Shading = '  '


            row1.append(f'  /{top1Shading}/\\{bottom2Shading}\\  ')
            row2.append(f' /{top1Shading}/{side1Shading}\\{bottom2Shading}\\ ')
            row3.append(f'/{top1ShadingBottom}/{side1Shading * 2}\\{bottom2ShadingBottom}\\')
            row4.append(f'\\{bottom1Shading}\\{side1Shading * 2}/{top2Shading}/')
            row5.append(f' \\{bottom1Shading}\\{side1Shading}/{top2Shading}/ ')
            row6.append(f'  \\{bottom1ShadingBottom}\\/{top2ShadingBottom}/  ')


        print(''.join(row1)); time.sleep(DELAY)
        print(''.join(row2)); time.sleep(DELAY)
        print(''.join(row3)); time.sleep(DELAY)
        print(''.join(row4)); time.sleep(DELAY)
        print(''.join(row5)); time.sleep(DELAY)
        print(''.join(row6)); time.sleep(DELAY)


try:
    main()
except KeyboardInterrupt:
    print('Cube Wall, by Al Sweigart al@inventwithpython.com')
