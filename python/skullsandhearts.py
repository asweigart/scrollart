import time, os, random


WIDTH = os.get_terminal_size()[0] - 1
DELAY = 0.2
HEART_INTERIOR = ':'

os.system('cls | clear')


r"""

/ ___ \ ^ 
 /   \ VVV
|() ()|   
 \ ^ / ___
\ VVV /   
)|   |() (

   ______
  /      \
 / _    _ \
| (_)  (_) |
|          |
 \   ^^   /
  VVVVVVVV
   \____/


   ______      ______
  /      \    /      \
 / _    _ \  / _    _ \
| (_)  (_) || (_)  (_) |
|          ||          |
 \   ^^   /  \   ^^   / 
  VVVVVVVV    VVVVVVVV  
   \____/      \____/



 |  ______  | (_)  (_)
 | /      \ |         
/ / _    _ \ \   ^^   
 | (_)  (_) | VVVVVVVV
 |          |  \____/
  \   ^^   /   ______
   VVVVVVVV   /      \
\   \____/   /        



._.._
/.\/.\
\..../
.\../
..\/

..__....__
./..\../..\
/....\/....\
\........../
.\......../
..\....../
...\..../
....\../
.....\/

...___......___
../...\..../...\
./.....\../.....\
/.......\/.......\
\................/
.\............../
..\............/
...\........../
....\......../
.....\....../
......\..../
.......\../
........\/
"""
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

#print_img(*normalize_img(get_heart(1)))
#print_img(*normalize_img(get_heart(2)))
#print_img(*normalize_img(get_heart(3)))
#print_img(*normalize_img(get_heart(4)))
#import sys; sys.exit()

MIN_HEART_SIZE = 2
MAX_HEART_SIZE = 4
HEART_PROBABILITY = 0.001

SKULL_TEMPLATE = [
    r'|  ______  | (_)  (_) ', 
    r'| /      \ |          ', 
    r' / _    _ \ \   ^^   /', 
    r'| (_)  (_) | VVVVVVVV ', 
    r'|          |  \____/  ', 
    r' \   ^^   /   ______  ', 
     '  VVVVVVVV   /      \\ ', 
     '   \\____/   / _    _ \\'] 

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
try:    
    while True:
        while len(next_rows) < (MAX_HEART_SIZE * 4 + 1):
            next_rows.append(list(SKULL_TEMPLATE[step % SKULL_TEMPLATE_HEIGHT] * SKULL_X_REPEAT))

            # Make sure the row is long enough for hearts, since we don't have partial skulls in the background:
            next_rows[-1].extend(' ' * (WIDTH - len(next_rows[-1])))
            step += 1

        for x in range(WIDTH - (MAX_HEART_SIZE * 7)):
            if random.random() < HEART_PROBABILITY:
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
        
except KeyboardInterrupt:
    print('Skulls and Hearts, by Al Sweigart al@inventwithpython.com 2024')


