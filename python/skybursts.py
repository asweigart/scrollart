import time, os, random

DELAY = 0.06
WIDTH = os.get_terminal_size()[0] - 1

EMPTY_CHARS = ' '
BURST_PROBABILITY = 0.01
MIN_NUM_STREAMS = 4
MAX_NUM_STREAMS = 10
MIN_STREAM_LENGTH = 4
MAX_STREAM_LENGTH = 12
BURST_CHARS = '@.'

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

print(normalize_img({(-5, -6): '@', (7, 8): '@'}))

def print_img(img, maxx, maxy):
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            if (x, y) in img:
                print(img[(x, y)], end='')
            else:
                print(' ', end='')
        print()


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
        for x, y in line(0, 0, random.randint(-h_radius, h_radius), random.randint(0, v_radius)):
            img[(x, y)] = burst_char
    return img


try:
    next_rows = []
    while True:
        while len(next_rows) < MAX_STREAM_LENGTH + 1:
            next_rows.append([random.choice(EMPTY_CHARS) for i in range(WIDTH)])

        for x in range(WIDTH - (MAX_STREAM_LENGTH * 2 + 1)):
            if random.random() < BURST_PROBABILITY:
                img = get_burst(random.randint(MIN_NUM_STREAMS, MAX_NUM_STREAMS),
                        MAX_STREAM_LENGTH, MAX_STREAM_LENGTH, random.choice(BURST_CHARS))
                img, maxx, maxy = normalize_img(img)
                for ix in range(maxx + 1):
                    for iy in range(maxy + 1):
                        if (ix, iy) in img:
                            next_rows[iy][ix + x] = img[(ix, iy)]
        row = next_rows[0]
        del next_rows[0]
        print(''.join(row))
        time.sleep(DELAY)
except KeyboardInterrupt:
    print('Sky Bursts, by Al Sweigart al@inventwithpython.com 2024')