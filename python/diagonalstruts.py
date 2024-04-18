import random, time, os


WIDTH = os.get_terminal_size()[0] - 1
DELAY = 0.008

EMPTY_CHAR = ' '
STRUT_CHAR = '#'

try:
    strut_points = [(0, True)]  # list of (position, going_right_bool)
    next_strut_point_at = random.randint(1, WIDTH - 2)
    

    while True:
        row = [EMPTY_CHAR] * WIDTH

        # There's a buggy case where somehow strut_points can end up empty. Let's just restart it then:
        if len(strut_points) == 0:
            strut_points = [(0, True)]  # list of (position, going_right_bool)
            next_strut_point_at = random.randint(1, WIDTH - 2)

        # Add a new strut point if it is time
        if strut_points[-1][0] == next_strut_point_at:
            strut_points.append((next_strut_point_at, not strut_points[-1][1]))

            if strut_points[-1][1]:
                # next next_strut_point_at between here and right edge
                if (WIDTH - 1) - next_strut_point_at > (WIDTH // 2):
                    # The distance to the right edge is too far, so let's do somewhere closer
                    next_strut_point_at = random.randint(next_strut_point_at, (WIDTH - 1 - next_strut_point_at) // 2 + next_strut_point_at)
                else:
                    next_strut_point_at = random.randint(next_strut_point_at, WIDTH - 1)
            else:
                # next next_strut_point_at between here and left edge
                if next_strut_point_at - 0 > (WIDTH // 2):
                    # the distance to the left edge is too far, so let's do somewhere closer
                    next_strut_point_at = random.randint(next_strut_point_at // 2, next_strut_point_at)
                else:
                    next_strut_point_at = random.randint(0, next_strut_point_at)

        # Create the row characters
        delete_indexes = []
        for i, (pos, going_right) in enumerate(strut_points):
            row[pos] = STRUT_CHAR

            # Move strut points (or mark them for deletion)
            if pos == WIDTH - 1 and going_right:
                delete_indexes.append(i)
            elif pos == 0 and not going_right:
                delete_indexes.append(i)
            elif going_right:
                strut_points[i] = (pos + 1, True)
            elif not going_right:
                strut_points[i] = (pos - 1, False)
            else:
                assert False

        # Remove strut points that have gone off the sides:
        for i in range(len(delete_indexes) - 1, -1, -1):
            del strut_points[delete_indexes[i]]

        print(''.join(row))
        time.sleep(DELAY)

except KeyboardInterrupt:
    print('Vertical Struts by Al Sweigart al@inventwithpython.com 2024')