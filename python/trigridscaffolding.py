import random, time, os

r"""
 /\  /\  /\  /\  /\  /\  /\  /\  /\  /\
/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\
\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /
_\/__\/__\/__\/__\/__\/__\/__\/__\/__\/_
"""

DELAY = 0.1

def main():
    changeAmt = 4
    density = 0

    while True:
        # -1 because Windows adds newlines if anything
        # is printed in the rightmost column.
        width = os.get_terminal_size()[0] - 1
        triangleWidth = (width - 2) // 4

        # Increase/decrease the density of triangles, until you
        # reach 0 or 100, then reverse the direction of density change:
        density += changeAmt
        if density <= 0 or density >= 100:
            changeAmt *= -1

        for j in range(2):
            # On j == 0, handle the two rows of begins-with-rightside-up-triangles:
            #  /\  /\  /\
            # /__\/__\/__\
            if j == 0:
                row1 = []
                row2 = []
            # On j == 1, handle the two rows of begins-with-upside-down-triangles:
            # \  /\  /
            # _\/__\/_
            elif j == 1:
                row1 = ['\\ ']
                row2 = ['_\\']
            for i in range(triangleWidth):
                if random.randint(0, 99) < density:
                    row1.append(' /')
                    row2.append('/')
                else:
                    row1.append('  ')
                    row2.append(' ')

                if random.randint(0, 99) < density:
                    row2.append('__')
                else:
                    row2.append('  ')

                if random.randint(0, 99) < density:
                    row1.append('\\ ')
                    row2.append('\\')
                else:
                    row1.append('  ')
                    row2.append(' ')
            print(''.join(row1)); time.sleep(DELAY)
            print(''.join(row2)); time.sleep(DELAY)


try:
    main()
except KeyboardInterrupt:
    print('Tri Grid Scaffolding, by Al Sweigart al@inventwithpython.com')



