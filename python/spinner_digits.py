import sys
import time

DELAY = 0.1
NUM_DIGITS = 5

spinner = ['|', '/', '-', '\\']
states = [0] * NUM_DIGITS


while True:
    print('\b' * NUM_DIGITS, end='')
    for i in range(NUM_DIGITS):
        print(spinner[states[i]], end='')
    sys.stdout.flush()

    states[-1] += 1
    for i in range(NUM_DIGITS - 1, 0, -1):
        if states[i] == 4:
            states[i] = 0
            states[i - 1] += 1
    if states[0] == 4:
        states[0] == 0

    time.sleep(DELAY)
