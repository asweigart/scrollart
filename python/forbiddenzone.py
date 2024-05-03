"""
Here's the program I ran on 2024/5/2 at the Recurse Center in Brooklyn, NY 
at the end of my Spring 1 batch. To run it:

Run this forbiddenzone.py program.
Get the control program from https://github.com/asweigart/scrollart/forbiddenzonecontrol.py and run it.
(The two programs need to be in the same folder.)
In the control program, enter the numbers 1 through 30 to try out the different sequences.

The control is a hack: it just writes a number 1 to 30 to `running.txt` and 
the main program is constantly reading this program to know when to switch. 
It was the simplest interprocess communication thing I could come up with. 
It's not a dumb hack if it works for my purposes.

This program is a bit of a mess; I copy/pasted various scroll art programs 
I had written into this one as separate functions. But I just wanted to
throw this code online quickly after the performance for people to play 
around with it.

(I've started looking at YouTube videos to figure out what DJs actually do,
and it turns out I could have made all this a lot simpler if I had known
basic DJing stuff from the start, LOL. Ah well, never to late to learn for
the future.)

Email me questions at al@inventwithpython.com
"""

import time, random, os, sys, math

LAST_RUNNING_CHECK = 0
LAST_RUNNING_MTIME = 0
RUNNING = None

def updateRunning():
    global LAST_RUNNING_MTIME, LAST_RUNNING_CHECK, RUNNING

    # Control this program by modifying the running.txt file in real time.
    if time.time() - LAST_RUNNING_CHECK > 0.1 and os.path.getmtime('running.txt') != LAST_RUNNING_MTIME:
        with open('running.txt') as fp:
            RUNNING = fp.read()
        LAST_RUNNING_CHECK = time.time()
        LAST_RUNNING_MTIME = os.path.getmtime('running.txt')



def normalize_img(img):
    normalized = {}

    if len(img) == 0:
        return {}

    x, y = next(iter(img.keys()))
    minx = maxx = x
    miny = maxy = y

    for x, y in img.keys():
        if x < minx:
            minx = x
        if y < miny:
            miny = y

    for x, y in img.keys():
        normalized[(x - minx, y - miny)] = img[(x, y)]

    for x, y in normalized.keys():
        if x > maxx:
            maxx = x
        if y > maxy:
            maxy = y

    return normalized, maxx + 1, maxy + 1


def move_img(img, movex, movey):
    moved_img = {}
    for x, y in img.keys():
        moved_img[(x + movex, y + movey)] = img[(x, y)]
    return moved_img

def print_img(img, maxx, maxy):
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            if (x, y) in img:
                print(img[(x, y)], end='')
            else:
                print(' ', end='')
        print()


def start():
    #os.system('cls | clear')
    #print('\n' * 100)
    
    change_amount = 0.01
    density = 0.0
    width = os.get_terminal_size()[0] - 1

    # show banner
    banner = r"""
     __ __|  |                ____|              |     _)      |      |                  __  /                     
        |    __ \    _ \      |      _ \    __|  __ \   |   _` |   _` |   _ \  __ \         /    _ \   __ \    _ \ 
        |    | | |   __/      __|   (   |  |     |   |  |  (   |  (   |   __/  |   |       /    (   |  |   |   __/ 
       _|   _| |_| \___|     _|    \___/  _|    _.__/  _| \__,_| \__,_| \___| _|  _|     ____| \___/  _|  _| \___| 
                                                                                                                                 


                                                                                                 
                  |         |    |             ,---.|        ,---.          o               |    
    ,---.,---.,---|,---.,---|    |---.,   .    |---||        `---.. . .,---..,---.,---.,---.|--- 
    |    |   ||   ||---'|   |    |   ||   |    |   ||            || | ||---'||   |,---||    |    
    `---'`---'`---'`---'`---'    `---'`---|    `   '`---'    `---'`-'-'`---'``---|`---^`    `---'
                                      `---'                                  `---'               """.splitlines()
    step = 0
    for line in banner:
        print(line)
        updateRunning()
        if RUNNING != 'start': return
        if step < 6:
            time.sleep(0.6)
        else:
            time.sleep(0.1)

        step += 1

    # show stars
    step = 0
    multiplier = 1
    while RUNNING == 'start':
        updateRunning()
        if density < 0 or density > 1.0:
            change_amount *= -1
        density = density + (change_amount * multiplier)

        line = ''
        for i in range(width):
            if random.random() < density:
                line = line + '*'
            else:
                line = line + ' '

        print(line)

        if step < 6:
            for i in range(6):
                time.sleep(0.1)  # need this loop otherwise it could be too long before returning 
                updateRunning()
                if RUNNING != 'start': return
        else:
            time.sleep(0.1)

        step += 1
        if step > 16:
            step = 0
            multiplier += 0.2



def end():
    global RUNNING
    change_amount = -0.02
    density = 0.5
    width = os.get_terminal_size()[0] - 1

    # show stars
    step = 0
    multiplier = 1
    while RUNNING == 'end':
        updateRunning()
        if density < 0 or density > 1.0:
            #change_amount *= -1
            RUNNING = 'source'  # automatically kick off source code
            source()
            RUNNING = 'standby'
            return

            
        density = density + (change_amount * multiplier)

        line = ''
        for i in range(width):
            if random.random() < density:
                line = line + '*'
            else:
                line = line + ' '

        print(line)

        if step < 6:
            time.sleep(0.6)
        else:
            time.sleep(0.1)

        step += 1
        if step > 16:
            step = 0
            multiplier += 0.2



def thorns():
    import random, math, os, time

    WIDTH = os.get_terminal_size()[0]

    # start with wipe
    for i in range(50):
        print('#' * WIDTH)
        time.sleep(0.01)

    DELAY = 0.005
    THORN_CHAR = '-'

    LEVELS = [1, 1, 1, 1, 1, 1, 1, 3, 6]
    MULTIPLIER = 10

    while RUNNING == 'thorns':
        line_length = int(random.choice(LEVELS) * ((random.random() + 1) * MULTIPLIER))
        line = THORN_CHAR * line_length
        
        if len(line) > WIDTH:
            line = THORN_CHAR * WIDTH

        print(line.center(WIDTH))
        time.sleep(DELAY)
        updateRunning()

def proton():
    WIDTH = os.get_terminal_size()[0] - 1
    EMPTY_CHAR = ' '
    COL_WIDTH = WIDTH // 5
    STREAM_BOUNDARIES = [0, COL_WIDTH, COL_WIDTH * 2, COL_WIDTH * 3, COL_WIDTH * 4, WIDTH]
    streams = [COL_WIDTH // 2, -1, -1, -1, -1]
    step = 0

    STEPS_UNTIL_NEXT_STREAM = 70

    while RUNNING == 'proton':
        columns = [EMPTY_CHAR] * WIDTH
        for i in range(5):
            if streams[i] != -1:
                # move stream left or right
                streams[i] += random.randint(-1, 1)
                if streams[i] < STREAM_BOUNDARIES[i]:
                    streams[i] = STREAM_BOUNDARIES[i]
                if streams[i] >= STREAM_BOUNDARIES[i + 1]:
                    streams[i] = STREAM_BOUNDARIES[i + 1] - 1
                columns[streams[i]] = 'O'
        print(''.join(columns))
        time.sleep(0.01)
        updateRunning()

        step += 1
        if step == STEPS_UNTIL_NEXT_STREAM * 1:
            streams[4] = int(COL_WIDTH * 4.5)
        if step == STEPS_UNTIL_NEXT_STREAM * 2:
            streams[1] = int(COL_WIDTH * 1.5)
        if step == STEPS_UNTIL_NEXT_STREAM * 3:
            streams[3] = int(COL_WIDTH * 3.5)
        if step == STEPS_UNTIL_NEXT_STREAM * 4:
            streams[2] = int(COL_WIDTH * 2.5)
        if step == STEPS_UNTIL_NEXT_STREAM * 5:
            break # break out of this loop and start moving streams to center

    while RUNNING == 'proton':
        columns = [EMPTY_CHAR] * WIDTH
        if streams[0] <= STREAM_BOUNDARIES[2]:
            streams[0] += 1
        if streams[1] <= STREAM_BOUNDARIES[2]:
            streams[1] += 1
        if streams[3] >= STREAM_BOUNDARIES[3] - 1:
            streams[3] -= 1
        if streams[4] >= STREAM_BOUNDARIES[3] - 1:
            streams[4] -= 1

        for i in range(5):
            if streams[i] > STREAM_BOUNDARIES[2] and streams[i] < STREAM_BOUNDARIES[3]:
                # move stream left or right
                streams[i] += random.randint(-1, 1)
                if streams[i] <= STREAM_BOUNDARIES[2]:
                    streams[i] = STREAM_BOUNDARIES[2] + 1
                if streams[i] >= STREAM_BOUNDARIES[3]:
                    streams[i] = STREAM_BOUNDARIES[3] - 1
            columns[streams[i]] = 'O'
        print(''.join(columns))
        time.sleep(0.01)
        updateRunning()


def forthandback():
    WIDTH = os.get_terminal_size()[0] - 1
    DELAY = 0.01

    steps_before_switch = 20

    BLOCK_CHAR = '#'
    BLOCK_WIDTH = 14

    EMPTY_CHARS = list('~                                      ')

    pos = 0
    speed = 0
    step = 0
    direction = 'right'
    while RUNNING == 'forth':
        if step > steps_before_switch and direction == 'right':
            speed += 1
            pos += speed
            if pos > WIDTH - BLOCK_WIDTH:
                pos = WIDTH - BLOCK_WIDTH
                step = 0
                speed = 0
                direction = 'left'
                steps_before_switch = random.randint(10, 40)  # was 20, 70
                if len(EMPTY_CHARS) > 4:
                    EMPTY_CHARS.pop()
                    EMPTY_CHARS.pop()
                    EMPTY_CHARS.pop()
        elif step > steps_before_switch and direction == 'left':
            speed -= 1
            pos += speed
            if pos < 0:
                pos = 0
                step = 0
                speed = 0
                direction = 'right'
                steps_before_switch = random.randint(1, 20)   # was 10, 40
                if len(EMPTY_CHARS) > 4:
                    EMPTY_CHARS.pop()
                    EMPTY_CHARS.pop()
                    EMPTY_CHARS.pop()

        for i in range(BLOCK_WIDTH // 2):
            columns = [random.choice(EMPTY_CHARS) for i in range(WIDTH)]
            for i in range(pos, pos + BLOCK_WIDTH):
                columns[i] = BLOCK_CHAR
            print(''.join(columns))
        time.sleep(DELAY)
        updateRunning()
        step += 1

def stripeout():
    WIDTH = os.get_terminal_size()[0] - 1
    FILL_CHARS = '#@O.:!'
    EMPTY_CHARS = ' '
    DELAY = 0.002
    HEIGHT = 40

    SIMULTANEOUS_STRIPES = WIDTH // 10
    BLOCK_MODE = False
    MAX_WIPES = 99

    def get_contiguous_columns_of_length(columns_left, length):
        contiguous_columns = set()
        for i in range(WIDTH):
            if all([i + x in columns_left for x in range(length)]):
                contiguous_columns.add(i)
        return contiguous_columns

    columns = [random.choice(EMPTY_CHARS)] * WIDTH
    makeEmpty = False
    iteration = 0

    while RUNNING == 'stripeout':
        columns_left = set(range(WIDTH))
        if makeEmpty:
            new_char = random.choice(EMPTY_CHARS)
        else:
            new_char = random.choice(FILL_CHARS)

        current_wipe_num = 1
        while len(columns_left):
            if current_wipe_num >= MAX_WIPES:
                # change ALL of the remaining columns
                columns = [new_char] * WIDTH
                columns_left = set()
                current_wipe_num = 1
            else:
                if BLOCK_MODE:
                    # Find contiguous columns (at least SIMULTAENOUS_STRIPES in length)
                    for desired_length in range(SIMULTANEOUS_STRIPES, 0, -1):
                        
                        contiguous_columns = get_contiguous_columns_of_length(columns_left, desired_length)
                        #print('desired_length', desired_length)
                        #print('columns_left', columns_left)
                        #print('contiguous_columns', contiguous_columns)
                        if len(contiguous_columns) != 0:
                            break
                    col = random.choice(list(contiguous_columns))

                    # Remove several contiguous columns:
                    #col = random.choice(list(columns_left))
                    for i in range(SIMULTANEOUS_STRIPES):
                        if col + i in columns_left:
                            columns_left.remove(col + i)
                            columns[col + i] = new_char
                else:
                    # Remove several random columns:
                    for i in range(SIMULTANEOUS_STRIPES):
                        if len(columns_left) == 0: break
                        col = random.choice(list(columns_left))
                        columns_left.remove(col)
                        columns[col] = new_char

            # Print columns with the new_char
            for i in range(HEIGHT):
                print(''.join(columns))
                time.sleep(DELAY)
                updateRunning()
                if RUNNING != 'stripeout': break

            current_wipe_num += 1
        makeEmpty = not makeEmpty
        iteration += 1
        if iteration % 2 == 0:
            BLOCK_MODE = not BLOCK_MODE


def moire():
    WIDTH = os.get_terminal_size()[0] - 1
    DELAY = 0.04
    MOIRE_CHAR = ":"
    EMPTY_CHAR = ' '
    MIN_CIRCLE_RADIUS = 2
    MAX_CIRCLE_RADIUS = 8
    CIRCLE_DENSITY = 0.3

    SINE_CHAR = '_'
    SINE_WIDTH = 25
    sine_step = 0.0
    sine_inc = 0.1

    def get_moire(radius, centerx, centery):
        switch = 3 - (2 * radius)
        cx = 0
        cy = radius

        img = {}  # keys are (x, y), values are 'X'

        while cx <= cy:
            # first quarter first octant
            img[(cx + centerx,-cy + centery)] = MOIRE_CHAR
            # first quarter 2nd octant
            img[(cy + centerx,-cx + centery)] = MOIRE_CHAR
            # second quarter 3rd octant
            img[(cy + centerx,cx + centery)] = MOIRE_CHAR
            # second quarter 4.octant
            img[(cx + centerx,cy + centery)] = MOIRE_CHAR
            # third quarter 5.octant
            img[(-cx + centerx,cy + centery)] = MOIRE_CHAR
            # third quarter 6.octant
            img[(-cy + centerx,cx + centery)] = MOIRE_CHAR
            # fourth quarter 7.octant
            img[(-cy + centerx,-cx + centery)] = MOIRE_CHAR
            # fourth quarter 8.octant
            img[(-cx + centerx,-cy + centery)] = MOIRE_CHAR
            if switch < 0:
                switch = switch + (4 * cx) + 6
            else:
                switch = switch + (4 * (cx - cy)) + 10
                cy = cy - 1
            cx = cx + 1

        return img

    next_columns = []
    while RUNNING == 'moire':
        while len(next_columns) < MAX_CIRCLE_RADIUS * 2 + 1:
            next_columns.append([EMPTY_CHAR] * WIDTH)

        if random.random() < CIRCLE_DENSITY:
            moire_img = {}
            for i in range(MAX_CIRCLE_RADIUS - MIN_CIRCLE_RADIUS):
                circle_img = get_moire(random.randint(MIN_CIRCLE_RADIUS, MAX_CIRCLE_RADIUS), MAX_CIRCLE_RADIUS, MAX_CIRCLE_RADIUS)
                moire_img.update(circle_img)
            norm_img, maxx, maxy = normalize_img(moire_img)
            moved_img = move_img(norm_img, random.randint(0, WIDTH - (MAX_CIRCLE_RADIUS * 2) - 1), 0)
            #print(moved_img)

            for x, y in moved_img.keys():
                next_columns[y][x] = MOIRE_CHAR

        # Add sine wave to columns
        sine_pos = int(((math.sin(sine_step) + 1) / 2) * (WIDTH - SINE_WIDTH))
        for i in range(SINE_WIDTH):
            next_columns[0][sine_pos + i] = SINE_CHAR   
        sine_step += sine_inc

        print(''.join(next_columns[0]))
        del next_columns[0]
        time.sleep(DELAY)
        updateRunning()



def maze():
    maze_size = 4
    isIncreasing = False

    WIDTH = os.get_terminal_size()[0] - 1
    DELAY = 0.04

    EMPTY = ' '
    FORWARD_SLASH = chr(9585)
    BACK_SLASH = chr(9586)

    step = 0

    columns = [FORWARD_SLASH] * (WIDTH // maze_size)
    while RUNNING == 'maze':
        # Set up the slashes in columns:
        for i in range(len(columns)):
            if random.randint(0, 1) == 0:
                columns[i] = FORWARD_SLASH
            else:
                columns[i] = BACK_SLASH

        # Print the columns:
        for row_num in range(maze_size):
            for i in range(len(columns)):
            
                if columns[i] == FORWARD_SLASH:
                    print(EMPTY * (maze_size - row_num - 1) + FORWARD_SLASH + EMPTY * (row_num), end='')
                elif columns[i] == BACK_SLASH:
                    print(EMPTY * (row_num) + BACK_SLASH + EMPTY * (maze_size - row_num - 1), end='')
            print()
            time.sleep(DELAY)
            updateRunning()

            step += 1
            if step == 12:
                step = 0
                if isIncreasing:
                    if maze_size == 4:
                        isIncreasing = False
                        maze_size = 3
                    else:
                        maze_size += 1
                    
                else:
                    if maze_size == 1:
                        isIncreasing = True
                        maze_size = 2
                    else:
                        maze_size -= 1
                columns = [FORWARD_SLASH] * (WIDTH // maze_size)
                break




def diagsweep(direction):
    WIDTH = os.get_terminal_size()[0] - 1
    DELAY = 0.002

    EMPTY_CHAR = ' '
    SWEEP_CHAR = '@'

    if direction == 'ltr':
        pos = 0
    elif direction == 'rtl':
        pos = WIDTH - 1
    
    columns = [EMPTY_CHAR] * WIDTH
    sweepOn = True
    while RUNNING == 'ltr' or RUNNING == 'rtl':
        if sweepOn:
            columns[pos] = SWEEP_CHAR
        else:
            columns[pos] = EMPTY_CHAR

        if direction == 'rtl':
            pos -= 1
            if pos <= 0:
                pos = WIDTH - 1
                sweepOn = not sweepOn
        if direction == 'ltr':
            pos += 1
            if pos >= WIDTH:
                pos = 0
                sweepOn = not sweepOn

        print(''.join(columns))
        time.sleep(DELAY)
        updateRunning()



def mathfunc(funcString):
    # Constants for the block characters used to represent pixels:
    TOP_BLOCK    = chr(9600)
    BOTTOM_BLOCK = chr(9604)
    FULL_BLOCK   = chr(9608)
    DELAY = 0.05
    FUNC = eval(funcString)

    y = 0
    while RUNNING.startswith('math'):
        width = os.get_terminal_size()[0] - 2
        for x in range(width):
            topBit = FUNC(x, y)
            bottomBit = FUNC(x, y + 1)

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
        time.sleep(DELAY)
        updateRunning()

def vertstrut():
    WIDTH = os.get_terminal_size()[0] - 1
    DELAY = 0.0125

    MIN_VERTICAL_SPAN = 10
    MAX_VERTICAL_SPAN = 30

    EMPTY_CHAR = ' '
    STRUT_CHAR = '#'

    while RUNNING == 'vert':
        col = random.randint(0, WIDTH - 1)
        row = [EMPTY_CHAR] * WIDTH
        row[col] = STRUT_CHAR

        row = ''.join(row)
        for i in range(random.randint(MIN_VERTICAL_SPAN, MAX_VERTICAL_SPAN)):
            print(row)
            time.sleep(DELAY)

        # Print horizontal line:
        print(STRUT_CHAR * WIDTH)
        time.sleep(DELAY)
        updateRunning()


def diagstrut():
    WIDTH = os.get_terminal_size()[0] - 1
    DELAY = 0.006

    EMPTY_CHAR = ' '
    STRUT_CHAR = '#'

    strut_points = [(0, True)]  # list of (position, going_right_bool)
    next_strut_point_at = random.randint(1, WIDTH // 2)
    

    while RUNNING == 'diag':
        row = [EMPTY_CHAR] * WIDTH

        # There's a buggy case where somehow strut_points can end up empty. Let's just restart it then:
        if len(strut_points) == 0:
            strut_points = [(0, True)]  # list of (position, going_right_bool)
            next_strut_point_at = random.randint(1, WIDTH // 2)

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
        updateRunning()



def stripedtri():
    DELAY = 0.05

    density = 0
    changeAmt = 10
    while RUNNING == 'stripedtri':
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
        print(''.join(row1))
        time.sleep(DELAY)
        updateRunning()
        if RUNNING != 'stripedtri': return
        print(''.join(row2))
        time.sleep(DELAY)
        updateRunning()
        if RUNNING != 'stripedtri': return
        print(''.join(row3))
        time.sleep(DELAY)
        updateRunning()
        if RUNNING != 'stripedtri': return


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

        print(''.join(row1))
        time.sleep(DELAY)
        updateRunning()
        if RUNNING != 'stripedtri': return
        print(''.join(row2))
        time.sleep(DELAY)
        updateRunning()
        if RUNNING != 'stripedtri': return
        print(''.join(row3))
        time.sleep(DELAY)
        updateRunning()
        if RUNNING != 'stripedtri': return


def cubewall():
    DELAY = 0.1
    density = 35
    step = 0

    while RUNNING == 'cubewall':
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


        print(''.join(row1))
        if random.random() < 0.2:
            time.sleep(DELAY)
            updateRunning()
            if RUNNING != 'cubewall': return

        print(''.join(row2))
        if random.random() < 0.2:
            time.sleep(DELAY)
            updateRunning()
            if RUNNING != 'cubewall': return

        print(''.join(row3))
        if random.random() < 0.2:
            time.sleep(DELAY)
            updateRunning()
            if RUNNING != 'cubewall': return

        print(''.join(row4))
        if random.random() < 0.2:
            time.sleep(DELAY)
            updateRunning()
            if RUNNING != 'cubewall': return

        print(''.join(row5))
        if random.random() < 0.2:
            time.sleep(DELAY)
            updateRunning()
            if RUNNING != 'cubewall': return

        print(''.join(row6))
        if random.random() < 0.2:
            time.sleep(DELAY)
            updateRunning()
            if RUNNING != 'cubewall': return


        step += 1


def diamondsky():
    # Constants for settings:
    DELAY = 0.05  # Pause after each row in seconds.
    WIDTH = os.get_terminal_size()[0] - 1  # Number of columns in output.
    MIN_DIAMOND_SIZE = 1
    MAX_DIAMOND_SIZE = 8

    CHANCE_FOR_FILLED_DIAMOND = 0.2  # Set between 0.0 and 1.0

    NUM_DIAMONDS_PER_ROW = 2

    EMPTY = '                ...,'  # The characters in this string are used to fill outside the squares.

    def get_outline_diamond(size):
        assert size > 0
        rows = []
        # Make the top half of the diamond:
        for i in range(size):
            rows.append(([None] * (size - i - 1)) + ['/'] + ([' '] * (i * 2)) + ['\\'])

        # Make the bottom half of the diamond:
        for i in range(size):
            rows.append(([None] * i) + ['\\'] + ([' '] * ((size - i - 1) * 2)) + ['/'])
        return rows


    def get_filled_diamond(size):
        assert size > 0
        rows = []
        # Make the top half of the diamond:
        for i in range(size):
            rows.append(([None] * (size - i - 1)) + (['/'] * (i + 1)) + (['\\'] * (i + 1)))
            
        # Make the bottom half of the diamond:
        for i in range(size):
            rows.append(([None] * i) + (['\\'] * (size - i)) + (['/'] * (size - i)))
        return rows

    next_rows = []
    while RUNNING == 'diamondsky':
        for j in range(NUM_DIAMONDS_PER_ROW):
            size = random.randint(MIN_DIAMOND_SIZE, MAX_DIAMOND_SIZE)

            if random.random() < CHANCE_FOR_FILLED_DIAMOND:
                diamond = get_filled_diamond(size)
            else:
                diamond = get_outline_diamond(size)

            x_start = random.randint(0, WIDTH - 1 - (size * 2))

            # Make sure there are enough rows in `next_rows`:
            while len(next_rows) < size * 2:
                next_rows.append([random.choice(EMPTY) for i in range(WIDTH)])

            # Add the diamond to `next_rows`
            for y, row in enumerate(diamond):
                for x, char in enumerate(row):
                    if char is None:
                        continue  # Don't print anything for the None "characters"; this is effectively a transparent space in the diamond.
                    next_rows[y][x + x_start] = char

        # Print the row and then remove it:
        print(''.join(next_rows[0]))
        del next_rows[0]
        time.sleep(DELAY)
        updateRunning()



def toggler1():
    DELAY = 0.01
    TOGGLER_DENSITY = 10

    RIGHT_INCREMENT = 1  # Try changing this to a different integer.
    LEFT_INCREMENT = RIGHT_INCREMENT * -1

    # -1 because Windows adds newlines if anything
    # is printed in the rightmost column.
    width = os.get_terminal_size()[0] - 1

    columnChars = ['.'] * width
    togglers = [] # Tuple of (x position, direction moving)

    while RUNNING == 'tog1':
        width = os.get_terminal_size()[0] - 1

        if random.randint(0, 99) < TOGGLER_DENSITY:
            # Add a new toggler
            togglers.append([random.randint(0, width), random.choice((LEFT_INCREMENT, RIGHT_INCREMENT))])

        # Remove out of bounds togglers:
        for i in range(len(togglers) - 1, -1, -1):
            if togglers[i][0] < 0 or togglers[i][0] >= width:
                del togglers[i]

        # Move the togglers and toggler the column chars:
        for i in range(len(togglers)):
            togglerPosition = togglers[i][0]
            togglerDirection = togglers[i][1]

            if columnChars[togglerPosition] == '.':
                columnChars[togglerPosition] = '@'
            else:
                columnChars[togglerPosition] = '.'

            togglers[i][0] += togglerDirection  # move the toggler

        print(''.join(columnChars))
        time.sleep(DELAY)
        updateRunning()


def toggler2():
    DELAY = 0.01
    TOGGLER_DENSITY = 10

    RIGHT_INCREMENT = 3  # Try changing this to a different integer.
    LEFT_INCREMENT = RIGHT_INCREMENT * -1

    # -1 because Windows adds newlines if anything
    # is printed in the rightmost column.
    width = os.get_terminal_size()[0] - 1

    columnChars = ['.'] * width
    togglers = [] # Tuple of (x position, direction moving)

    while RUNNING == 'tog2':
        width = os.get_terminal_size()[0] - 1

        if random.randint(0, 99) < TOGGLER_DENSITY:
            # Add two new togglers
            position = random.randint(0, width)
            togglers.append([position - RIGHT_INCREMENT, LEFT_INCREMENT])
            togglers.append([position, RIGHT_INCREMENT])

        # Remove out of bounds togglers:
        for i in range(len(togglers) - 1, -1, -1):
            if togglers[i][0] < 0 or togglers[i][0] >= width:
                del togglers[i]

        # Move the togglers and toggler the column chars:
        for i in range(len(togglers)):
            togglerPosition = togglers[i][0]
            togglerDirection = togglers[i][1]

            if columnChars[togglerPosition] == '.':
                columnChars[togglerPosition] = '@'
            else:
                columnChars[togglerPosition] = '.'

            togglers[i][0] += togglerDirection  # move the toggler

        print(''.join(columnChars))
        time.sleep(DELAY)
        updateRunning()





def skull():

    WIDTH = os.get_terminal_size()[0] - 1
    DELAY = 0.3
    HEART_INTERIOR = ':'
    startTime = time.time()


    def get_heart(size):
        img = {}  # keys are (x, y), values are 'X'

        for x in range(size, size * 2):
            img[(x, 0)] = '_'  # left top of heart
            img[(size * 3 + x, 0)] = '_'  # right top of heart

        for i in range(size):
            img[(size - 1 - i, i + 1)] = '/'  # left side of left side top
            img[(size - 1 - i + (size * 3), i + 1)] = '/'  #left side of right side top
            img[(size * 2 + i, i + 1)] = '\\'  # right side of left side top
            img[(size * 2 + i + (size * 3), i + 1)] = '\\'  # right side of right side top

        for i in range(size * 3):
            img[(i, i + size + 1)] = '\\'  # left side bottom slant of heart
            img[(size * 6 - i - 1, i + size + 1)] = '/'  # right side bottom slant of heart

        # Interior of heart:
        for i in range(size):
            for j in range(size):
                img[(size + i, j + 1)] = HEART_INTERIOR  # left side top
                img[(size * 4 + i, j + 1)] = HEART_INTERIOR  # right side top
       
            for j in range(i):
                img[(i, size - j)] = HEART_INTERIOR
                img[(size * 2 + (size - i - 1), size - j)] = HEART_INTERIOR 

                img[(size * 3 + i, size - j)] = HEART_INTERIOR
                img[(size * 5 + (size - i - 1), size - j)] = HEART_INTERIOR 

        for j in range(size * 3):
            for i in range(size * 3 - 1 - j):
                img[((size * 3) - i - 1, j + size + 1)] = HEART_INTERIOR
                img[((size * 3) + i, j + size + 1)] = HEART_INTERIOR


        return img

    MIN_HEART_SIZE = 2
    MAX_HEART_SIZE = 4
    HEART_PROBABILITY = 0.001


    SKULL_TEMPLATE = [
        r'|          ______          | (_)  (_) ', 
        r'|         /      \         |          ', 
        r'         / _    _ \         \   ^^   /', 
        r'        | (_)  (_) |         VVVVVVVV ', 
        r'        |          |          \____/  ', 
        r'         \   ^^   /           ______  ', 
         '          VVVVVVVV           /      \\ ', 
         '           \\____/           / _    _ \\'] 
    SKULL_TEMPLATE_HEIGHT = len(SKULL_TEMPLATE)
    SKULL_TEMPLATE_WIDTH = len(SKULL_TEMPLATE[0])


    SKULL_X_REPEAT = WIDTH // SKULL_TEMPLATE_WIDTH
    next_rows = []
    step = 0
   
    while RUNNING == 'skull':

        while len(next_rows) < (MAX_HEART_SIZE * 4 + 1):
            next_rows.append(list(SKULL_TEMPLATE[step % SKULL_TEMPLATE_HEIGHT] * SKULL_X_REPEAT))
            
            # Make sure the row is long enough for hearts, since we don't have partial skulls in the background:
            next_rows[-1].extend(' ' * (WIDTH - len(next_rows[-1])))
            
            step += 1

        for x in range(WIDTH - (MAX_HEART_SIZE * 7)):
            # only show hearts starting after 3 seconds (before then it's only skulls)
            if time.time() - startTime > 3.0 and random.random() < HEART_PROBABILITY:
                heart_size = random.randint(MIN_HEART_SIZE, MAX_HEART_SIZE)
                img, maxx, maxy = normalize_img(get_heart(heart_size))
                for ix in range(maxx + 1):
                    for iy in range(maxy + 1):
                        if (ix, iy) in img:
                            next_rows[iy][ix + x] = img[(ix, iy)]

        row = next_rows[0]
        del next_rows[0]
        print(''.join(row))
        if step % 10 == 0:  # Print 10 rows at a time before pause
            time.sleep(DELAY)
            updateRunning()


def orbital():
    EMPTY = ' '
    DELAY = 0.04

    CHARS = []
    SINE_STEP_INCS = []
    sine_steps = []
    for i in range(random.randint(7, 15)):
        CHARS.append(random.choice('@O0o*.,vV'))
        SINE_STEP_INCS.append(random.random() * 0.1 + 0.0001)
        sine_steps.append(random.random() * math.pi)

    WIDTH = os.get_terminal_size()[0] - 1

    while RUNNING == 'orbital':
        row = [EMPTY] * WIDTH

        for i in range(len(CHARS)):
            row[int((math.sin(sine_steps[i]) + 1) / 2 * WIDTH)] = CHARS[i]
            sine_steps[i] += SINE_STEP_INCS[i]

        print(''.join(row))

        time.sleep(DELAY)
        updateRunning()


def towers():
    WIDTH = os.get_terminal_size()[0] - 1
    DELAY = 0.0075
    AFTER_TOWER_DELAY = 0.75

    EMPTY_CHAR = ' '
    CORNER_CHAR = '+'
    TOP_CHAR = '-'
    SIDE_CHAR = '|'
    INTERIOR_CHARS = ':|. '

    MIN_TOWER_WIDTH = 8
    MAX_TOWER_WIDTH = 20

    MIN_TOWER_HEIGHT = 4
    MAX_TOWER_HEIGHT = 17

    TOWER_HEIGHT_MAX_DIFF = 8

    WIPE_AFTER = 8


    step = 1
    columns = [EMPTY_CHAR] * WIDTH
    while RUNNING == 'towers':
        if step % WIPE_AFTER == 0:
            for i in range(60):
                print()
                time.sleep(DELAY)
            time.sleep(AFTER_TOWER_DELAY)
            columns = [EMPTY_CHAR] * WIDTH

        # Tower 1 top (tower 1 is slightly higher than tower 2):
        tower1_left = random.randint(0, (WIDTH // 2) - MAX_TOWER_WIDTH)
        tower1_width = random.randint(MIN_TOWER_WIDTH, MAX_TOWER_WIDTH)
        columns[tower1_left] = CORNER_CHAR
        columns[tower1_left + tower1_width] = CORNER_CHAR
        for i in range(tower1_left + 1, tower1_left + tower1_width):
            columns[i] = TOP_CHAR

        print(''.join(columns))
        time.sleep(DELAY)
        updateRunning()
        if RUNNING != 'towers': return

        # Tower 1 top body that is above tower 2's top:
        columns[tower1_left] = SIDE_CHAR
        columns[tower1_left + tower1_width] = SIDE_CHAR
        interior_char = INTERIOR_CHARS[step % len(INTERIOR_CHARS)]#random.choice(INTERIOR_CHARS)
        for i in range(tower1_left + 1, tower1_left + tower1_width):
            columns[i] = interior_char

        for i in range(random.randint(1,TOWER_HEIGHT_MAX_DIFF)):
            print(''.join(columns))
            time.sleep(DELAY)
            updateRunning()
            if RUNNING != 'towers': return
        
        # Tower 2 top:
        tower2_left = random.randint(0, WIDTH - MAX_TOWER_WIDTH)
        tower2_width = random.randint(MIN_TOWER_WIDTH, MAX_TOWER_WIDTH)
        columns[tower2_left] = CORNER_CHAR
        columns[tower2_left + tower2_width] = CORNER_CHAR
        for i in range(tower2_left + 1, tower2_left + tower2_width):
            columns[i] = TOP_CHAR
        
        print(''.join(columns))
        time.sleep(DELAY)
        updateRunning()
        if RUNNING != 'towers': return

        # Tower 2 body (and 1):
        columns[tower2_left] = SIDE_CHAR
        columns[tower2_left + tower2_width] = SIDE_CHAR
        interior_char = INTERIOR_CHARS[step % len(INTERIOR_CHARS)]#random.choice(INTERIOR_CHARS)
        for i in range(tower2_left + 1, tower2_left + tower2_width):
            columns[i] = interior_char


        for i in range(random.randint(MIN_TOWER_HEIGHT, MAX_TOWER_HEIGHT)):
            print(''.join(columns))
            time.sleep(DELAY)
            updateRunning()
            if RUNNING != 'towers': return

        time.sleep(AFTER_TOWER_DELAY)
        updateRunning()
        if RUNNING != 'towers': return
        step += 1



mona = """
                                                                      ...,;:c:.                     
                                                             ....'',;;:ccllool.                     
                                                  ......',;;:ccllllllllooooddd;                     
                                       ....'',;::cccllllllloooooooooooooddddddl.                    
                             ....'',;::cllloooooooooooolooooooooooddddddddddxxd,                    
                    ....'',;:cllllllooooooddooddddddddddodddddddddxxddxxxddxxkxc.                   
         ....'',;;::cclllllllooooooooddddddddddddddddxdddddxxxxxxxxxxxxkxxxxkkkd'                   
...',,;:cclllooooooooooooooooooddddxxxxxxxdddxxxxxxxxxxxxxxxxxxkkxxxkkkkkkkkkkxx:                   
cllllllooooooooooooooooodddddddddxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkkkkkkkkkkkkkko.                  
:oooooooooooddddddddddddxxxxxxxxxxxxdlc;;;,;;::cldxxxxkkkkkkkkOOOkkOkkkkkkkkkkkkx;                  
'oddddddddddxxxxxxxxxxxxkxkkkkkkkdc;'.............';ldkkkkkkkkOOOOOOOOOOOkkkkkkOOl.                 
.cxxxxxxxxxxxxxkkkkkkkkkkkkkkkkxl,...........  ......,lxkkOOOOOOOOkkkOOOOkkkkxkkkd'                 
 ;xkkxkkkkkkkkkkOOOOOOOOOOOkkkxc...,:c::;;'............;dkkkkkkkkkkkkkkkkkkkxxdxxd;                 
 'dOOkkOOkkOOOOOOO00OOOOOOOOkkl'.:odxxxdolc:,'........ .,ldddoddddddxkkkkkkkxdddddc.                
 .lOOOOOOOOO000OO0000OOOOkkkkd,.;oxxkxxxdooc:;,'......  .,cclloooolloxkkkkkxdddoddo'                
  ;k00000OOO000000OOOOOOOkkkxl..;ldxxxxddoollc:,...   ....;::ccccc::cldxxxdddoooool;                
  .dOOOOOOOO00OOOOOOOOOOOkkkd:..;loooddl:;;;,,''......  ..';;::c::;;;:loooollccllc:,.               
   :kOO0OkkOOOOOkkkkkkkkOkkko,..';;,,:c;.','.';c;'....   ..,:ccccc::::cllcc:;;,;,,,,.               
   .okkkxdodxxxdooooodxkkkkxl,...','';c;';lloodl:'......  ..;;::::;;,,;;,,,,;;,',',,'               
    ;lollllllolcc:::cclxxdddl,. .colllol:coxxxoc,.......  ...',;;;,,,,,,,,;;,,,,,,,,,.              
    .;:cccllll:::;,;;::ccc:::;...;oxdodo:;cddoc;'.......   ...,;;;;;;;,,;;,,,,,,,,',,.              
     ':ccllllc:;;,,,,,,,;;;,,'....;loll:..,cccc;'.......   ...,::::::;;;;,,,,,,,,,,,,'              
     .:cccccc:;;;;;;,,;;;;;,'......,:cc:,'',:cc;'......     ..'::::::;;,,,''''',,'',,'.             
     .::;;;:;;;;;;;::;;::;;;,'......';clc:::::,'...........  ..,;;;;;;,,,,,,,,;,,,'','.             
      ';,,,;;;;;;;;;;;;;;;;;;;'.......':loc;,............... ...,;::;;;;;;;;::;,,,''.'..            
      .''',;;;;;;;;;;;;;:;:::c;'.....  .................... .....'''''''''';::,,,,'''''.            
       .'',;;;;;;;,,,,;;;::clll;'....     .','...''',,'........  ....'',:::::;,,,,,,,''.            
       ..''''',;;;,,,;;::clllolc;.....    .,:::;;;:::::;'.............',:ccc:::;;:::;;,'.           
        ..''''',;;;::cccllllllc:;....    .';clcccllllllc,...............',;::cc:cccccc:;'           
        ...'''',,;::::;;;;:;;,,'........';coooooooddoolc;...... ..''.......''',,,,,;:ccc:.          
        ..',;;;::::;,,',,'.............,loddxddddddddoll:'......,;::;'..............';;;;.          
         .,;:::::;;,'',,,'............'codxxddddddxddool:'...';:c:;,'.....................          
         .,,;;,',,,,,,;,'..''........';lodddddddddddddolc;,,,,,,'.................''...'..          
         .',,'''',;;;;;,,''','......,:loddoooodxxxxxxddolc;,'..............................         
          .,'','.',;;::;;,,,'......';lodddolodxxxxxxddoc:;'......'''.......................         
          .''''......',,,,;;'......';:cccc::cllllllcc::,'.......',''',;,,,'................         
           .'''''.''''',;;;'.......,,,,,,'',,''''..'',,...........',;::;;,............','...        
           .....'',,,,,,,'........',,'.''',,'''.....''............'';::;'...................        
            ...'',,'',,,,'........'''....'''''...................''';;,.............. .......       
            .....''''',,,'.......................................',''...............   ......       
             ....................................................''.................    ......      
             ......'''',,'......................'...................................     .....      
              ...',,,,;;,......................'''''................................     .....      
              ..''''''''.......................'''...................................      ...      
              ................''..............','....................................       ...     
               ..............'''.................................................. ...      ...     
               ................................................................. .  ..       ...    
               ................................................................    ...       ...    
                ..........''''',,''...';;;;,''...................................  ...       ...    
                .........'',;;,,;,,,;ldxxdoolcccc::;,''.............',,,,,''....  .....      ....   
                .........',;,,,,''',:loooooooooollllllllc;'...,;,,,,,,;;,'......   .         .....  
                 .   .......'''.'...';:;;;::cllllllll:;;:::;,,;,,',,,,,'.........  .         .....  
                 ..  ....................'',;;:::::::::;,'''',,,'''''''..........           ......  
                  .       .............';;,''',,;;:::;;;;;;,......................   ..... ..  ...  
                  ..        .....  ..,,;ccc:,...'',,,;;,''',,,'..................     .....    .... 
                   .  ..      ..   .''',;:cc;'.....................................    .....    ... 
                              .... .....';:;'.......................................    .....  .....
                       .................',,.............................       .......  ............
                                 .......................................       ..............       
                                        ...   ............       .......       .....                
                                               ........  .      ........                            
                                                ...... ..                                           
                                                 ....                                               
                                 ....                                                               
""".splitlines()

scream = """
                       .;,.....                                                                     
                       .;:;,'.'',;:c:;,,''...                                                       
                       .......',;:::::;:::;;;,,,,'''......                                          
                      .:::,,''...............',;;;;;;;;;;;;,......                                  
                      .,;:c::;,''..........''',,'...'',,;:c:;;,''...    .....                       
                      ...'',,;,,'......'''''................'''''........;l:'.                      
                     .,,,;,,,,,'...''......'''........';:cccccc:,'......,::,'..              .      
                     .,,;;:clooolllc:,'.',,,'.....',coxxkOOOO00Okxdc;'...',,;;,'..       ..'........
                    .,,,;;;:cllllc:;;;::;,......;lodxxxxkkOOO00OOOOOko;..',,,;:;;;'.   .','....''''.
                    :xdl:;;cllc:;;:ccc;'...''..:dkkkkkxxkkkOOOOOOOOOOOko,.',;,'',,'...','....';;;;;.
                   .cdxkkd:,;cc:::c:,....,lo;.:dxkkkkkkkkkOOOOOOOO0K00OOd,.,,'','...';,....,:lc::l:.
                   'odocldxc,',;:;,'...':xkl':xkkkkkkkOOOO00OOOOOOkO00OOkc........',;,'',:cccccoxx: 
                   ,odddooxOd:,,,''...';d0x;'lkkkkkkkOOkxk000OOOOOOkO000Ol.'....'',,,,;cllc::okOkd, 
                   .,ldddooxOd;,,''...'cO0x,,dkkxdxxOOOOkkO00O00KK0OO00OOl;l:...,,,,;lool:;:xOkxko. 
                   ...;lddlclol:,''''.'o00x,'okOOxdk0000kkkOO00000KKKK0Oxclx:..',,,cddoc::cdOkdxd,  
                  ......:dxdl;;:c;,''.'lO0k:'lk0K0O0000OkkkO000OkO0KKK0Oxoxx;..'';lxkdc::coxxdl:'.  
                 .;......,lxxdc,,,'....cO0Oo,ckOKXXK00kdkOO00KKK0O00000Odokx,..',:lxxol::cddl:,'.   
                .cdc.......:dkkdc,.....:k00k:;dkO0KK0Oxld0Oxk00OOOOOO00xldOd'.,',:dkxdoc:odl;..'.   
                .dko,.......'lxkkdc'...'o000d;:xkO000Okxdk000OkkkkkxkkdlokOl',,';dOOxxocldo;'''.    
                :kko;'..... ..;oxkkdc'..;x00Oo;lxkOOkkdc::oOOkkkkkkkxdook0d;,,',lO00OOdldxl,''..    
                cOOko;,,;'.....'cdkkkdc''lO00Oo:o0KOxxc:xl:xkkkkkOOdodxOOl'','':k0KKK0odOxc,,''.    
                .ck0Odlc::;'.....;oxkOkd::x0K0OllOX0kd;ckdcdOOOOOkooxk0k:..''',oOKKK0xoxOxc;,;,.    
                 .;x00kdool:'....'cxOOkd,'o0KKOlcOX0kd;.:c:x0OOOxloxO0xc'..'',;dO0KOl,cxko:,,:'     
                 ..'oO0Okdol;..':llccc;...o0KKx;;kX0kkl;,;lO00KOolx00xlc,..';;:dk0Kd''clll:,;;.     
              .......ck00ko:,..::'.. ....,x00Oc.'o0OkxkkkO00O00dldO0dcc;...;c:cox0Kd,,:;,coc:'      
              'cc,....,d00kl'....   .....cO00d'..;ldOkOO0000K0dclk0k:;;...'cdlclx00o;::'.:do:.      
             .cooo;.....ck0d'...    ....;x00k:...;::lxOO000OxlccoO0l,,....;oxoloxOkl:c:,,:oo;.      
             'lddddl,....;dc.        ..,oOOd:....cxdodxkOOkc,',;d0O:''...,:dxdoodkdc;,,;:coo,       
             'ldxxxxdc'...'......   ..'lkOd'.....;oxOOO0OOkc'...o0O:....,:codddoodo:;',cclxo.       
             'cddxxxxxl,.........   ..lxkkd,.....':okkOOxo;.   .:kOl....':ccloooloolc;;llld:        
           .;cooodxxxxxd:.......   ...:xxxo' ......:xOdc,..    .;xOd,.....,:ccclldkxlc:lddl.        
           .oddolodxkxxxd;......   ...',;,. ........;:'....     'dxc.......',,,;cdkxdolldxc.        
           ;xxxdooodxkkkd, ....   .......  .............        .''...,;'.......,cxxxxdddd,         
          .oOkxdl;coxkkxc. ....  ...      ... .........           ....'oo:'......,codxxxxl.         
           ;xOxxo:',oxdc'. .... ...      ...  .........           ..'..lxxo:'.....';lddxd;          
           .;xkddo:':do,.  .......  ..  ...   ........           ......:dxkxo:,..'.';codo'          
          ...:xxddoc,,'.  .......  ... ...   .........           ......;dxkkkko:,'''',:c;.          
          ....:xxddd:...........  ...  ..    ........            ......'lddxkkkxo:,',;;:.           
          .....:dxdl'........... ..  ....   .........           .........;cloxkkkxo:,,;;.           
         .......,ol'..............   ....   ........            ...........;cloxkOOxl:,.            
        ...   ......  ............   ...   .........           ....'...... ..;cldkkkkxl.            
        .'..  ..     ............    .   ..........  ..       ....''.. ........;loxkOOo.            
       .'....  .    ............        .........   ...      ...................,coddx:             
       ,;''....    ............        ................      .........:l;....'....;lol.             
      .cc;'.....    .........        .... ............       ........;odc'....,'....;,              
      cxol:'.....   ........        ....  ...........           .  .;oooc.   ..','...               
     .dkdooc,'....                ..................               .;ooc,..   ...',,.               
     ,xOkdooc,'.....             ..................       ...  ...'.'cc..    .. ...'.               
    .cxkOxool;,'.... .    ..    .................      ........;lddl,,,..  ...... ..                
    ,xkxkkdoc;,'... ...  ...   .''......... ....       ........:dkxxdc,...........                  
    ,xOxxxxdl:''.. ...  ...   ..,.. ...... ....      .''........;dxdxOkl::;.......                  
   .cdxkxkkdc;''.....  ....   .,'.  ..''.  ...      .:c;'........:oddxO0Oxdl:,;;,'.                 
   ,odddxxxd:'... ..  ..'.   .',.. ...'.  ...    ...:ll:,.........;lodxkO0xdooooll,                 
  .cdooxkxdl:''.....  ....   .,'.  ..'.  ...    ..,:llcc:,.........,cldxdkOkdloool.                 
  .oxdod0Od:,'.. ..  ..'..  ..'.  ..... ...     .;lclcc::;,..........;ldxdxkkdllo:.                 
  ,oooookKOl,'. ...  .''.   ...   ........     ..'',,::;;;;;'.........;ldxxdxxxol'                  
 .cooooookKOc,. ..   .''.   ...   ........    .cc'....,;;;;;;'.........,coddddxxo.                  
 ,doodddooOKx, ... ...'.         ....  ..    .'okc'....,;,,,,,'.........':oxxddd:.                  
.ldoodkxoldOk, ..  ...'. .       ....   .    .,cxxd:....,;,;;,,'..........;ldxxo'                   
'xklldkxdoodo' ..  ...'. .       ..    ..  ..'::lxOkc....;;;;:;,,'.........':ldc.                   
c0Oo:lxxxdol:.....  ....       ....    .   ..,llcldkkc...,:::cccc:'..........;c,                    
d0KOoclxxkkd:....   .,.  ...   ...    ..  ...'oxoc:lkk:...,:clllll:,............                    
k00K0xodxkkxc.......',.. .,... ...   ..    ...cxdl::lkk:...':cccc::;,.........                      
;cldxkkdddxdc'... ..'''...;,,,....  ....   ...,lddoolokk:....,;colc:::,.......                      
    .....',,'.  . ..',,'';coddc'........   ....;lkOOOkkOk:.....ckkxoclo;......                      
                    ....';coxOko,......    ....';dk0K0OO0Ol,...'lO00kddd:....                       
                          ..',;;'''......  .....'cokK0kkO0Od:...'oO00kxxd:...                       
                                            .....,;o0K0kkkOOkl'..:xkkdoddo:.                        
                                                  ..;coolodOOxl,.'cdxxddllo:.                       
                                                          ..'','..':ldxxoll:.                       
                                                                    ..,:cc:'                        
""".splitlines()
def roll_ascii_art(img):
    delay = 0.01
    indentation = 20
    # show top half
    for i in range(len(img) // 2):
        print(' ' * indentation + img[i])
        time.sleep(delay)
        delay *= 1.05

    updateRunning()
    if RUNNING != 'mona' and RUNNING != 'scream': return

    # show bottom half
    for i in range(len(img) // 2, len(img)):
        print(' ' * indentation + img[i])
        time.sleep(delay)
        delay *= 0.93

    # show full image
    while RUNNING == 'mona' or RUNNING == 'scream':
        for i in range(len(img)):
            print(' ' * indentation + img[i])
            time.sleep(delay)
            updateRunning()
            if delay > 0.005:
                delay *= 0.99

    print('\n' * 50)




def hexportals():
    WIDTH = os.get_terminal_size()[0] - 1
    DELAY = 0.3
    EMPTY_CHARS = '/\\_    '
    DENSITY = 0.0025
    INTERIOR_CHARS = '.                   '
    INTERIOR_DENSITY = 1.0
    MIN_SIZE = 4
    MAX_SIZE = 10

    next_rows = []
    step = 0 
    while RUNNING == 'hex':    
        # Make sure there are enough rows in `next_rows`:
        for i in range((MAX_SIZE * 2 + 2) - len(next_rows)):
            next_rows.append([random.choice(EMPTY_CHARS) for i in range(WIDTH)])

        for pos in range(0, WIDTH - (MAX_SIZE * 4 + 1)):
            if random.random() >= DENSITY:
                # Don't create a hexagon here.
                continue

            size = random.randint(MIN_SIZE, MAX_SIZE)

            # Draw new hexagon to next_rows:
            for i in range(pos + 1 + size, pos + 1 + size + (2 * size + 1)):
                next_rows[0][i] = '_'  # Top row of underscores
                next_rows[size * 2][i] = '_'  # Bottom row of underscores
            for i in range(size):
                next_rows[size - i][pos + 1 + i] = '/'  # Top left slashes
                next_rows[size + 1 + i][pos + 1 + i] = '\\'  # Bottom left slashes

                next_rows[size - i][pos + 1 + (size * 3) + 1 + (size - i - 1)] = '\\'  # Top right slashes
                next_rows[size + 1 + i][pos + 1 + (size * 3) + 1 + (size - i - 1)] = '/'  # Bottom right slashes

            if INTERIOR_CHARS is not None:
                # Draw interior characters on inside of hexagon
                for i in range(1, size + 1):
                    for j in range(size - i + 2, size * 3 + 1 + i):
                        if random.random() < INTERIOR_DENSITY:
                            next_rows[i][pos + j] = random.choice(INTERIOR_CHARS)
                        if random.random() < INTERIOR_DENSITY and i != 1:
                            next_rows[size * 2 - i + 1][pos + j] = random.choice(INTERIOR_CHARS)

        # Display the next rows:
        print(''.join(next_rows[0]))
        del next_rows[0]
        if step % 8 == 0:
            time.sleep(DELAY)
            updateRunning()
        step += 1


def worms():

    EMPTY_CHAR = ' '
    DIRT_CHARS = '\\/'
    WORM_CHAR = ' '
    DELAY = 0.02
    GROW_BACK_IN = 30
    NUM_WORMS = 8
    MAX_MOVE = 4

    WIDTH = os.get_terminal_size()[0] - 1

    columns_growback = [GROW_BACK_IN] * WIDTH

    worms = [random.randint(0, WIDTH - 1) for i in range(NUM_WORMS)]

    columns = [random.choice(DIRT_CHARS) for i in range(WIDTH)]
    for worm in worms:
        columns[worm] = WORM_CHAR

    while RUNNING == 'worms':
        for i, worm in enumerate(worms):
            direction = random.randint(-MAX_MOVE, MAX_MOVE)
            if worm + direction > 0 and worm + direction < WIDTH:
                columns[worm] = EMPTY_CHAR
                columns_growback[worm] = GROW_BACK_IN

                columns[worm + direction] = WORM_CHAR
                worms[i] += direction
        for i in range(len(columns)):
            if columns_growback[i] > 0 and columns[i] == EMPTY_CHAR:
                columns_growback[i] -= 1
            if columns_growback[i] == 0:
                columns[i] = random.choice(DIRT_CHARS)
                columns_growback[i] = GROW_BACK_IN

        print(''.join(columns))
        time.sleep(DELAY)
        updateRunning()



def source():
    global RUNNING
    sourceCode = open('forbiddenzone.py').readlines()
    for i in range(0, len(sourceCode), 50):
        for j in range(50):
            if i + j >= len(sourceCode): 
                RUNNING = ''
                return
            print(sourceCode[i + j], end='')
            time.sleep(0.01)
            updateRunning()
            if RUNNING != 'source': return
        time.sleep(0.6)
        updateRunning()
        if RUNNING != 'source': return
        

def twists(speed='normal'):
    WIDTH = os.get_terminal_size()[0] - 1

    #if speed == 'normal':
    #    DELAY = 0.008
    #elif speed == 'fast':
    #    DELAY = 0.001

    NUM_COLUMNS = 6
    COLUMN_WIDTH = 12

    COLUMN_CHAR = '|'
    EMPTY_CHAR = ' '

    GAP_SIZE = (WIDTH - COLUMN_WIDTH) // (NUM_COLUMNS + 1)
    BETWEEN_TWIST_LENGTH = 0
    TWIST_LENGTH = 50

    SINE_STEP_INC = (math.pi / 2) / TWIST_LENGTH

    to_twist = random.randint(1, NUM_COLUMNS - 1)

    while RUNNING in ('twists', 'twistsfast'):
        # This is a bit redundant to the speed param, but I need it since twistsfast immediately follows twists:
        if RUNNING == 'twists':
            DELAY = 0.008
        elif RUNNING == 'twistsfast':
            DELAY = 0.002

        # Set up straight columns:
        columns = [EMPTY_CHAR] * WIDTH
        i = GAP_SIZE
        for i in range(1, NUM_COLUMNS + 1):
            for j in range(COLUMN_WIDTH):
                columns[(i * GAP_SIZE) + j] = COLUMN_CHAR

        # Print straight columns:
        for i in range(BETWEEN_TWIST_LENGTH):
            print(''.join(columns))
            time.sleep(DELAY)
            updateRunning()
            if RUNNING not in ('twists', 'twistsfast'): return

        # Select two adjacent columns to twist:
        #to_twist = random.randint(1, NUM_COLUMNS - 1)
        to_twist += random.randint(-1, 1)
        if to_twist == 0:
            to_twist = 2
        if to_twist == NUM_COLUMNS:
            to_twist = NUM_COLUMNS - 2
        
        
        for sine_step in range(TWIST_LENGTH):
            columns = [EMPTY_CHAR] * WIDTH

            in_transit_pos_left  = (to_twist     * GAP_SIZE) + int(math.sin(sine_step * SINE_STEP_INC) * GAP_SIZE)
            in_transit_pos_right = ((to_twist+1) * GAP_SIZE) - int(math.sin(sine_step * SINE_STEP_INC) * GAP_SIZE)
            for j in range(COLUMN_WIDTH):
                columns[in_transit_pos_left + j] = COLUMN_CHAR
                columns[in_transit_pos_right + j] = COLUMN_CHAR

            # Print straight columns (that are not being twisted currently):
            i = GAP_SIZE
            for i in range(1, NUM_COLUMNS + 1):
                if i == to_twist or i == to_twist + 1:
                    continue
                for j in range(COLUMN_WIDTH):
                    columns[(i * GAP_SIZE) + j] = COLUMN_CHAR
                

            print(''.join(columns))
            time.sleep(DELAY)   
            updateRunning()  
            if RUNNING not in ('twists', 'twistsfast'): return        



def skybursts():
    DELAY = 0.02
    WIDTH = os.get_terminal_size()[0] - 1

    EMPTY_CHARS = ' '
    BURST_PROBABILITY = 0.001
    MIN_NUM_STREAMS = 4
    MAX_NUM_STREAMS = 10
    MIN_STREAM_LENGTH = 4
    MAX_STREAM_LENGTH = 12
    BURST_CHARS = '@.:O'


    def line(x1, y1, x2, y2):
        """Returns a list of points in a line between the given points.

        Uses the Bresenham line algorithm. More info at:
        https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm"""
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # TODO - Do we want this line?

        isSteep = abs(y2-y1) > abs(x2-x1)
        if isSteep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
        isReversed = x1 > x2

        if isReversed:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

            deltax = x2 - x1
            deltay = abs(y2-y1)
            error = int(deltax / 2)
            y = y2
            ystep = None
            if y1 < y2:
                ystep = 1
            else:
                ystep = -1
            for x in range(x2, x1 - 1, -1):
                if isSteep:
                    yield (y, x)
                else:
                    yield (x, y)
                error -= deltay
                if error <= 0:
                    y -= ystep
                    error += deltax
        else:
            deltax = x2 - x1
            deltay = abs(y2-y1)
            error = int(deltax / 2)
            y = y1
            ystep = None
            if y1 < y2:
                ystep = 1
            else:
                ystep = -1
            for x in range(x1, x2 + 1):
                if isSteep:
                    yield (y, x)
                else:
                    yield (x, y)
                error -= deltay
                if error < 0:
                    y += ystep
                    error += deltax


    def get_burst(num_streams, h_radius, v_radius, burst_char):
        img = {}
        for i in range(num_streams):
            for x, y in line(0, 0, random.randint(-h_radius, h_radius), random.randint(-v_radius, v_radius)):
                img[(x, y)] = burst_char
        return img


    next_rows = []
    while RUNNING == 'skybursts':
        while len(next_rows) < (MAX_STREAM_LENGTH * 2 + 1):
            next_rows.append([random.choice(EMPTY_CHARS) for i in range(WIDTH)])

        for x in range(WIDTH - (MAX_STREAM_LENGTH * 4 + 1)):
            if random.random() < BURST_PROBABILITY:
                img = get_burst(random.randint(MIN_NUM_STREAMS, MAX_NUM_STREAMS),
                        MAX_STREAM_LENGTH*2, MAX_STREAM_LENGTH, random.choice(BURST_CHARS))
                img, maxx, maxy = normalize_img(img)
                for ix in range(maxx + 1):
                    for iy in range(maxy + 1):
                        if (ix, iy) in img:
                            next_rows[iy][ix + x] = img[(ix, iy)]
        row = next_rows[0]
        del next_rows[0]
        print(''.join(row))
        time.sleep(DELAY)
        updateRunning()




def ducklings():
    PAUSE = 0.2  # (!) Try changing this to 1.0 or 0.0.
    DENSITY = 0.025  # (!) Try changing this to anything from 0.0 to 1.0.

    DUCKLING_WIDTH = 5
    LEFT = 'left'
    RIGHT = 'right'
    BEADY = 'beady'
    WIDE = 'wide'
    HAPPY = 'happy'
    ALOOF = 'aloof'
    CHUBBY = 'chubby'
    VERY_CHUBBY = 'very chubby'
    OPEN = 'open'
    CLOSED = 'closed'
    OUT = 'out'
    DOWN = 'down'
    UP = 'up'
    HEAD = 'head'
    BODY = 'body'
    FEET = 'feet'

    # Get the size of the terminal window:
    WIDTH = os.get_terminal_size()[0] - 1

    class Duckling:
        def __init__(self):
            """Create a new duckling with random body features."""
            self.direction = random.choice([LEFT, RIGHT])
            self.body = random.choice([CHUBBY, VERY_CHUBBY])
            self.mouth = random.choice([OPEN, CLOSED])
            self.wing = random.choice([OUT, UP, DOWN])

            if self.body == CHUBBY:
                # Chubby ducklings can only have beady eyes.
                self.eyes = BEADY
            else:
                self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])

            self.partToDisplayNext = HEAD

        def getHeadStr(self):
            """Returns the string of the duckling's head."""
            headStr = ''
            if self.direction == LEFT:
                # Get the mouth:
                if self.mouth == OPEN:
                    headStr += '>'
                elif self.mouth == CLOSED:
                    headStr += '='

                # Get the eyes:
                if self.eyes == BEADY and self.body == CHUBBY:
                    headStr += '"'
                elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                    headStr += '" '
                elif self.eyes == WIDE:
                    headStr += "''"
                elif self.eyes == HAPPY:
                    headStr += '^^'
                elif self.eyes == ALOOF:
                    headStr += '``'

                headStr += ') '  # Get the back of the head.

            if self.direction == RIGHT:
                headStr += ' ('  # Get the back of the head.

                # Get the eyes:
                if self.eyes == BEADY and self.body == CHUBBY:
                    headStr += '"'
                elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                    headStr += ' "'
                elif self.eyes == WIDE:
                    headStr += "''"
                elif self.eyes == HAPPY:
                    headStr += '^^'
                elif self.eyes == ALOOF:
                    headStr += '``'

                # Get the mouth:
                if self.mouth == OPEN:
                    headStr += '<'
                elif self.mouth == CLOSED:
                    headStr += '='

            if self.body == CHUBBY:
                # Get an extra space so chubby ducklings are the same
                # width as very chubby ducklings.
                headStr += ' '

            return headStr

        def getBodyStr(self):
            """Returns the string of the duckling's body."""
            bodyStr = '('  # Get the left side of the body.
            if self.direction == LEFT:
                # Get the interior body space:
                if self.body == CHUBBY:
                    bodyStr += ' '
                elif self.body == VERY_CHUBBY:
                    bodyStr += '  '

                # Get the wing:
                if self.wing == OUT:
                    bodyStr += '>'
                elif self.wing == UP:
                    bodyStr += '^'
                elif self.wing == DOWN:
                    bodyStr += 'v'

            if self.direction == RIGHT:
                # Get the wing:
                if self.wing == OUT:
                    bodyStr += '<'
                elif self.wing == UP:
                    bodyStr += '^'
                elif self.wing == DOWN:
                    bodyStr += 'v'

                # Get the interior body space:
                if self.body == CHUBBY:
                    bodyStr += ' '
                elif self.body == VERY_CHUBBY:
                    bodyStr += '  '

            bodyStr += ')'  # Get the right side of the body.

            if self.body == CHUBBY:
                # Get an extra space so chubby ducklings are the same
                # width as very chubby ducklings.
                bodyStr += ' '

            return bodyStr

        def getFeetStr(self):
            """Returns the string of the duckling's feet."""
            if self.body == CHUBBY:
                return ' ^^  '
            elif self.body == VERY_CHUBBY:
                return ' ^ ^ '

        def getNextBodyPart(self):
            """Calls the appropriate display method for the next body
            part that needs to be displayed. Sets partToDisplayNext to
            None when finished."""
            if self.partToDisplayNext == HEAD:
                self.partToDisplayNext = BODY
                return self.getHeadStr()
            elif self.partToDisplayNext == BODY:
                self.partToDisplayNext = FEET
                return self.getBodyStr()
            elif self.partToDisplayNext == FEET:
                self.partToDisplayNext = None
                return self.getFeetStr()


    #print('Duckling Screensaver, by Al Sweigart')
    #print('Press Ctrl-C to quit...')
    #time.sleep(2)

    ducklingLanes = [None] * (WIDTH // DUCKLING_WIDTH)
    step = 0
    while RUNNING == 'ducklings':  # Main program loop.
        for laneNum, ducklingObj in enumerate(ducklingLanes):
            # See if we should create a duckling in this lane:
            if (ducklingObj == None and random.random() <= DENSITY):
                    # Place a duckling in this lane:
                    ducklingObj = Duckling()
                    ducklingLanes[laneNum] = ducklingObj

            if ducklingObj != None:
                # Draw a duckling if there is one in this lane:
                print(ducklingObj.getNextBodyPart(), end='')
                # Delete the duckling if we've finished drawing it:
                if ducklingObj.partToDisplayNext == None:
                    ducklingLanes[laneNum] = None
            else:
                # Draw five spaces since there is no duckling here.
                print(' ' * DUCKLING_WIDTH, end='')

        print()  # Print a newline.
        sys.stdout.flush()  # Make sure text appears on the screen.
        if (step % 4 == 0):
            time.sleep(PAUSE)
            updateRunning()
        step += 1


def pipes():
    # Constants for settings:
    DELAY = 0.2
    WIDTH = os.get_terminal_size()[0] - 1

    GAP_PROBABILITY = 0.96

    # This setting changes the behavior to create the "long vertical style" if greater than 0.0:
    VERTICAL_STYLE_FACTOR = 1.0  # Set between 0.0 and 1.0

    # Constants for printed characters:
    UP_DOWN_CHAR         = chr(9474)  # Character 9474 is '│'
    LEFT_RIGHT_CHAR      = chr(9472)  # Character 9472 is '─'
    DOWN_RIGHT_CHAR      = chr(9484)  # Character 9484 is '┌'
    DOWN_LEFT_CHAR       = chr(9488)  # Character 9488 is '┐'
    UP_RIGHT_CHAR        = chr(9492)  # Character 9492 is '└'
    UP_LEFT_CHAR         = chr(9496)  # Character 9496 is '┘'
    UP_DOWN_RIGHT_CHAR   = chr(9500)  # Character 9500 is '├'
    UP_DOWN_LEFT_CHAR    = chr(9508)  # Character 9508 is '┤'
    DOWN_LEFT_RIGHT_CHAR = chr(9516)  # Character 9516 is '┬'
    UP_LEFT_RIGHT_CHAR   = chr(9524)  # Character 9524 is '┴'
    CROSS_CHAR           = chr(9532)  # Character 9532 is '┼'
    EMPTY = ' '

    # The previous printed row; initialize to up-left-right characters:
    prev_row = [UP_LEFT_RIGHT_CHAR] * WIDTH

    step = 0
    while RUNNING == 'pipes':  # Main loop
        row = []  # Character strings to print in this row.
        for i, prev_char in enumerate(prev_row):
            # Figure out if we need to connect the left side:
            if i == 0:
                left_connect = False
                # Uncomment this if you do want pipes to sometimes connect off of the left edge:
                #left_connect = random.choice((True, False))
            else:
                if row[i - 1] in (LEFT_RIGHT_CHAR, DOWN_RIGHT_CHAR, UP_RIGHT_CHAR, UP_DOWN_RIGHT_CHAR, DOWN_LEFT_RIGHT_CHAR, UP_LEFT_RIGHT_CHAR, CROSS_CHAR):
                    left_connect = True
                else:
                    left_connect = False

            # Figure out if we need to connect the up side:
            if prev_char in (UP_DOWN_CHAR, DOWN_RIGHT_CHAR, DOWN_LEFT_CHAR, UP_DOWN_RIGHT_CHAR, UP_DOWN_LEFT_CHAR, DOWN_LEFT_RIGHT_CHAR, CROSS_CHAR):
                up_connect = True
            else:
                up_connect = False

            # The downward and right side connection can be either:
            down_connect = random.choice((True, False))
            if random.random() < GAP_PROBABILITY:
                down_connect = False

            if i == WIDTH - 1:
                # make the rightmost column never connect off the right edge:
                right_connect = False
                # Additional check so that we don't make the pipe go off the right edge:
                shape = (up_connect, down_connect, left_connect, right_connect)
                if shape == (False, False, True, False):
                    # Make this a left-down pipe:
                    down_connect = True
                elif shape == (False, True, False, False):
                    # Make this an empty space:
                    down_connect = False
                elif shape == (True, False, False, False):
                    # Make this an up-down pipe:
                    down_connect = True
            else:
                right_connect = random.choice((True, False))
                if random.random() < GAP_PROBABILITY:
                    right_connect = False

            # Override right_connect value if VERTICAL_STYLE_FACTOR is greater than 0.0:
            if random.random() < VERTICAL_STYLE_FACTOR:
                right_connect = False
                # Note that we'll still have right connections sometimes because the dictionary
                # below will sometimes randomly choose it to keep a connected picture.
                # Adding the following code is what will guarantee no right connections ever exist,
                # which means no left connections will ever exist (unless we allow them off the left edge)
                # and therefore only empty spaces are printed:
                ## Additional check so that we don't make the pipe go off the right edge:
                #shape = (up_connect, down_connect, left_connect, right_connect)
                #if shape == (False, False, True, False):
                #    # Make this a left-down pipe:
                #    down_connect = True
                #elif shape == (False, True, False, False):
                #    # Make this an empty space:
                #    down_connect = False
                #elif shape == (True, False, False, False):
                #    # Make this an up-down pipe:
                #    down_connect = True

            # Uncomment this if you do want pipes to sometimes connect off of the right edge:
            # (This disables the IS_LONG_VERTICAL_STYLE effect as well, if it is set.)
            #right_connect = random.choice((True, False))

            # Get the character to print based on the connections to the four other sides:
            shape = (up_connect, down_connect, left_connect, right_connect)
            char = None
            char = {
                # Up   Down  Left  Right
                (True, True, True, True):     CROSS_CHAR,
                (True, True, True, False):    UP_DOWN_LEFT_CHAR,
                (True, True, False, True):    UP_DOWN_RIGHT_CHAR,
                (True, True, False, False):   UP_DOWN_CHAR,
                (True, False, True, True):    UP_LEFT_RIGHT_CHAR,
                (True, False, True, False):   UP_LEFT_CHAR,
                (True, False, False, True):   UP_RIGHT_CHAR,
                (True, False, False, False):  random.choice((UP_DOWN_RIGHT_CHAR, UP_DOWN_CHAR, UP_RIGHT_CHAR)),
                (False, True, True, True):    DOWN_LEFT_RIGHT_CHAR,
                (False, True, True, False):   DOWN_LEFT_CHAR,
                (False, True, False, True):   DOWN_RIGHT_CHAR,
                (False, True, False, False):  DOWN_RIGHT_CHAR, # This is forced to be down right
                (False, False, True, True):   LEFT_RIGHT_CHAR,
                (False, False, True, False):  random.choice((DOWN_LEFT_RIGHT_CHAR, DOWN_LEFT_CHAR, LEFT_RIGHT_CHAR)),
                (False, False, False, True):  DOWN_RIGHT_CHAR, # This is forced to be down right
                (False, False, False, False): EMPTY,
            }[shape]
            assert char is not None
            row.append(char)
        assert len(row) == len(prev_row) == WIDTH
        print(''.join(row))
        prev_row = row
        if step % 4 == 0:
            time.sleep(DELAY)
        updateRunning()
        step += 1


def writeRunning():
    with open('running.txt', 'w') as fp:
        fp.write(RUNNING)


def main():
    global RUNNING

    RUNNING = 'standby'
    writeRunning()

    try:
        step = 0
        while True:
            updateRunning()
            if RUNNING in 'start' or RUNNING.startswith('1 '):
                RUNNING = 'start'; writeRunning()
                start()
            elif RUNNING == 'thorns' or RUNNING.startswith('2 '):
                RUNNING = 'thorns'; writeRunning()
                thorns()
            elif RUNNING == 'proton' or RUNNING.startswith('3 '):
                RUNNING = 'proton'; writeRunning()
                proton()
            elif RUNNING == 'forth' or RUNNING.startswith('4 '):
                RUNNING = 'forth'; writeRunning()
                forthandback()
            elif RUNNING == 'stripeout' or RUNNING.startswith('5 '):
                RUNNING = 'stripeout'; writeRunning()
                stripeout()
            elif RUNNING == 'moire' or RUNNING.startswith('6 '):
                RUNNING = 'moire'; writeRunning()
                moire()
            elif RUNNING == 'mona' or RUNNING.startswith('7 '):
                RUNNING = 'mona'; writeRunning()
                roll_ascii_art(mona)
            elif RUNNING == 'rtl' or RUNNING.startswith('8 '):
                RUNNING = 'rtl'; writeRunning()
                diagsweep('rtl')
            elif RUNNING == 'scream' or RUNNING.startswith('9 '):
                RUNNING = 'scream'; writeRunning()
                roll_ascii_art(scream)
            elif RUNNING == 'ltr' or RUNNING.startswith('10 '):
                RUNNING = 'ltr'; writeRunning()
                diagsweep('ltr')
            elif RUNNING == 'maze' or RUNNING.startswith('11 '):
                RUNNING = 'maze'; writeRunning()
                maze()
            elif RUNNING == 'math1' or RUNNING.startswith('12 '):
                RUNNING = 'math1'; writeRunning()
                mathfunc('lambda x, y: ((x | y) % 7)')
            elif RUNNING == 'hex' or RUNNING.startswith('13 '):
                RUNNING = 'hex'; writeRunning()
                hexportals()
            elif RUNNING == 'vert' or RUNNING.startswith('14 '):
                RUNNING = 'vert'; writeRunning()
                vertstrut()
            elif RUNNING == 'diag' or RUNNING.startswith('15 '):
                RUNNING = 'diag'; writeRunning()
                diagstrut()
            elif RUNNING == 'stripedtri' or RUNNING.startswith('16 '):
                RUNNING = 'stripedtri'; writeRunning()
                stripedtri()
            elif RUNNING == 'cubewall' or RUNNING.startswith('17 '):
                RUNNING = 'cubewall'; writeRunning()
                cubewall()
            elif RUNNING == 'towers' or RUNNING.startswith('18 '):
                RUNNING = 'towers'; writeRunning()
                towers()
            elif RUNNING == 'diamondsky' or RUNNING.startswith('19 '):
                RUNNING = 'diamondsky'; writeRunning()
                diamondsky()
            elif RUNNING == 'tog1' or RUNNING.startswith('20 '):
                RUNNING = 'tog1'; writeRunning()
                toggler1()
            elif RUNNING == 'skull' or RUNNING.startswith('21 '):
                RUNNING = 'skull'; writeRunning()
                skull()
            elif RUNNING == 'tog2' or RUNNING.startswith('22 '):
                RUNNING = 'tog2'; writeRunning()
                toggler2()
            elif RUNNING == 'worms' or RUNNING.startswith('23 '):
                RUNNING = 'worms'; writeRunning()
                worms()
            elif RUNNING == 'twists' or RUNNING.startswith('24 '):
                RUNNING = 'twists'; writeRunning()
                twists()
            elif RUNNING == 'twistsfast' or RUNNING.startswith('25 '):
                RUNNING = 'twistsfast'; writeRunning()
                twists('fast')
            elif RUNNING == 'skybursts' or RUNNING.startswith('26 '):
                RUNNING = 'skybursts'; writeRunning()
                skybursts()
            elif RUNNING == 'orbital' or RUNNING.startswith('27 '):
                RUNNING = 'orbital'; writeRunning()
                orbital()
            elif RUNNING == 'pipes' or RUNNING.startswith('28 '):
                RUNNING = 'pipes'; writeRunning()
                pipes()
            elif RUNNING == 'ducklings' or RUNNING.startswith('29 '):
                RUNNING = 'ducklings'; writeRunning()
                ducklings()
            elif RUNNING == 'end' or RUNNING.startswith('30 '):
                RUNNING = 'end'; writeRunning()
                end()
            elif RUNNING == 'source' or RUNNING.startswith('31 '):
                RUNNING = 'source'; writeRunning()
                source()



            elif RUNNING == 'clear':
                os.system('clear | cls')
                RUNNING = ''
            else:
                if step % 100 == 0:
                    print('standby...')
                time.sleep(0.01)
                step += 1
    except KeyboardInterrupt:
        pass



if __name__ == '__main__':
    main()
