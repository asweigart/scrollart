import time

DELAY = 0.1

while True:
    for i in range(7):
        prefix = ' ' * i
        suffix = ' ' * (6 - i)
        line = (prefix + 'OOOOOO' + suffix) * 6
        print(line)
        time.sleep(DELAY)
