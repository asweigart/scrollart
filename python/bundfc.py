import time, os, random, shutil, math

WIDTH = shutil.get_terminal_size()[0] - 1
CHARS = '@Oo+:.'
BACKGROUND = ' '
DELAY = 0.03
CHANGE_DIV = 40

def get_random_wave(z=0):
    wave = {}

    wave['side'] = 'left'#random.choice(['left', 'left'])
    if z >= len(CHARS):
        wave['side'] = 'right'
        z -= (len(CHARS))


    wave['speed'] = min(random.random() + 0.3, 1.0) * 10
    wave['amplitude'] = random.randint(WIDTH // 6, WIDTH // 2) / (z + 1)
    wave['char'] = CHARS[z] #random.choice(CHARS)

    return wave


waves = [get_random_wave(x) for x in range(len(CHARS) * 2)] #range(random.randint(5, 5))]
step = 42  # Don't start at 0, just to avoid all the waves starting at 0 as well.

try:
    while True:
        row = [BACKGROUND for x in range(WIDTH)]
        for wave in waves:
        #wave = waves[step % len(waves)]

            wave_length = int((math.sin((step / CHANGE_DIV) * wave['speed']) + 1) * wave['amplitude'])
            if wave['side'] == 'left':
                for i in range(0, wave_length):
                    row[i] = wave['char']
            elif wave['side'] == 'right':
                for i in range(WIDTH - 1 - wave_length, WIDTH - 1):
                    row[i] = wave['char']

        print(''.join(row))
        time.sleep(DELAY)
        step += 1
except KeyboardInterrupt:
    print('BundFC by Al Sweigart, 2024')

