import math, time

WIDTH = 70
MESSAGE = 'Hello!'
DELAY = 0.1
STEP_INCREASE = 0.2

step = 0.0
multiplier = (WIDTH - len(MESSAGE)) / 2
while True:  # Main program loop.
    sinOfStep = math.sin(step)
    padding = ' ' * int((sinOfStep + 1) * multiplier)
    print(padding + MESSAGE)
    time.sleep(DELAY)
    step += STEP_INCREASE
