import time

DELAY = 0.1

lineA = ('      OOOOOO') * 6
lineB = ('OOOOOO      ') * 6

while True:
    print(lineA)
    time.sleep(DELAY)
    print(lineA)
    time.sleep(DELAY)
    print(lineA)
    time.sleep(DELAY)
    print(lineB)
    time.sleep(DELAY)
    print(lineB)
    time.sleep(DELAY)
    print(lineB)
    time.sleep(DELAY)
