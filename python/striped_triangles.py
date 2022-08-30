import random, time, os

r"""
  \        /      \ \ \    / / /
 \ \      / /      \ \      / /
\ \ \    / / /      \        /
"""

DELAY = 0.1
changeAmt = 4

def main():
    density = 0
    while True:
        # -1 because Windows adds newlines if anything
        # is printed in the rightmost column.
        width = os.get_terminal_size()[0] - 1

        # The width of a pair of triangles is 7 characters:
        #   /\ \ \
        #  / /\ \
        # / / /\
        # 123456
        numTrianglePairs = (width - 2) // 6

        # Increase/decrease the density of triangles, until you
        # reach 0 or 100, then reverse the direction of density change:
        density += changeAmt
        if density <= 0 or density >= 100:
            changeAmt *= -1

        # Draw a row that starts with an upright triangle on the left side.
        row1 = ['  ']
        row2 = [' ']
        row3 = []
        for i in range(numTrianglePairs):
            if random.randint(0, 99) < density:
                if random.randint(0, 1):
                    row1.append('\\')
                    row2.append('\\ \\')
                    row3.append('\\ \\ \\')
                else:
                    row1.append('/')
                    row2.append('/ /')
                    row3.append('/ / /')
            else:
                row1.append(' ')
                row2.append('   ')
                row3.append('     ')

            if random.randint(0, 99) < density:
                if random.randint(0, 1):
                    row1.append('\\ \\ \\')
                    row2.append('\\ \\')
                    row3.append('\\')
                else:
                    row1.append('/ / /')
                    row2.append('/ /')
                    row3.append('/')
            else:
                row1.append('     ')
                row2.append('   ')
                row3.append(' ')
        print(''.join(row1)); time.sleep(DELAY)
        print(''.join(row2)); time.sleep(DELAY)
        print(''.join(row3)); time.sleep(DELAY)


        # Draw a row that starts with an upside down triangle on the left side.
        row1 = []
        row2 = [' ']
        row3 = ['  ']
        for i in range(numTrianglePairs):
            if random.randint(0, 99) < density:
                if random.randint(0, 1):
                    row1.append('\\ \\ \\')
                    row2.append('\\ \\')
                    row3.append('\\')
                else:
                    row1.append('/ / /')
                    row2.append('/ /')
                    row3.append('/')
            else:
                row1.append('     ')
                row2.append('   ')
                row3.append(' ')

            if random.randint(0, 99) < density:
                if random.randint(0, 1):
                    row1.append('\\')
                    row2.append('\\ \\')
                    row3.append('\\ \\ \\')
                else:
                    row1.append('/')
                    row2.append('/ /')
                    row3.append('/ / /')
            else:
                row1.append(' ')
                row2.append('   ')
                row3.append('     ')

        print(''.join(row1)); time.sleep(DELAY)
        print(''.join(row2)); time.sleep(DELAY)
        print(''.join(row3)); time.sleep(DELAY)

try:
    main()
except KeyboardInterrupt:
    print('Striped Triangles, by Al Sweigart al@inventwithpython.com')

