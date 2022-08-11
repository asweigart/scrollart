import random, time

WIDTH = 70
DELAY = 0.02

while True:
    line = ''
    for i in range(WIDTH):
        if random.randint(0, 1000) <= 4:
            line = line + '*'
        else:
            line = line + ' '

    print(line)
    time.sleep(DELAY)
