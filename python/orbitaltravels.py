import random, os, time, math

os.system('cls | clear')  # Clear the screen

EMPTY = ' '
DELAY = 0.05

CHARS = []
SINE_STEP_INCS = []
sine_steps = []
for i in range(random.randint(7, 15)):
    CHARS.append(random.choice('@O0o*.,vV'))
    SINE_STEP_INCS.append(random.random() * 0.1 + 0.0001)
    sine_steps.append(random.random() * math.pi)

WIDTH = 100 #os.get_terminal_size()[0] - 1

try:
    while True:
        row = [EMPTY] * WIDTH

        for i in range(len(CHARS)):
            row[int((math.sin(sine_steps[i]) + 1) / 2 * WIDTH)] = CHARS[i]
            sine_steps[i] += SINE_STEP_INCS[i]

        print(''.join(row))

        time.sleep(DELAY)
except KeyboardInterrupt:
    print('Helix Travels, by Al Sweigart al@inventwithpython.com 2024')