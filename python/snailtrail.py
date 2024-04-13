import random, os, time

os.system('cls | clear')

WIDTH = os.get_terminal_size()[0] - 1
MIN_TRAIL_LEN = 5

try:
    while True:
        trail_length = random.randint(MIN_TRAIL_LEN, WIDTH - 2)
        for i in range(trail_length):
            print('_' * i + '@V', end='', flush=True)
            time.sleep(0.9 / trail_length)  # Use 0.9 instead of 1.0 because printing adds a delay and I want it to be roughly 1 second per snail.
            print('\b' * (i + 2), end='', flush=True)
        print('_' * trail_length + '@V', end='', flush=True)

        print('\n' * random.randint(1, 6))

except KeyboardInterrupt:
    print('Snail Trail, by Al Sweigart al@inventwithpython.com 2024')