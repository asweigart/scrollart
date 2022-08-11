import random, time

DENSITY_CHANGE = 0.5
DELAY = 0.02

density = 0.0
increaseDensity = True
while True:
    if increaseDensity:
        density = density + DENSITY_CHANGE
        if density > 100:
            density = 100
            increaseDensity = False
    elif not increaseDensity:
        density = density - DENSITY_CHANGE
        if density < 0:
            density = 0
            increaseDensity = True

    line = ''
    for i in range(80):
        if random.randint(0, 99) <= density:
            line = line + '*'
        else:
            line = line + ' '

    print(line)
    time.sleep(DELAY)
