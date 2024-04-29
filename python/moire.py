import time, os, random


WIDTH = os.get_terminal_size()[0] - 1
DELAY = 0.2
MOIRE_CHAR = ":"

os.system('cls | clear')


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
        if x > maxx:
            maxx = x
        if y < miny:
            miny = y
        if y > maxy:
            maxy = y

    for x, y in img.keys():
        normalized[(x - minx, y - miny)] = img[(x, y)]

    return normalized, maxx + 1, maxy + 1



def print_img(img, maxx, maxy):
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            if (x, y) in img:
                print(img[(x, y)], end='')
            else:
                print(' ', end='')
        print()

img = {}
for i in range(20):
    img.update(get_moire(i, 20, 20))
#print_img(*normalize_img(img))
print_img(img, 40, 40)
import sys;sys.exit()
try:    
    while True:

        time.sleep(DELAY)
        
except KeyboardInterrupt:
    print('Moire, by Al Sweigart al@inventwithpython.com 2024')


