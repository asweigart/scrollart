import random, time, os, sys

os.system('cls | clear')

MESSAGE = 'It was the best of times, it was the worst of times...'
DELAY = 0.01
CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
UNLOCK_CHAR_PROBABILITY = 0.04
SPACER = ' '

try:
    locked_columns = [False] * len(MESSAGE)
    
    while True:
        columns = [random.choice(CHARS) for i in range(len(MESSAGE))]

        if random.random() < UNLOCK_CHAR_PROBABILITY:
            while True:
                r = random.randint(0, len(MESSAGE) - 1)
                if locked_columns[r] == False:
                    locked_columns[r] = True
                    break  # Found an unlocked column, so break out of the loop.

        if all(locked_columns):
            # Done, print the message a few more times and then quit:
            for i in range(10):
                print(SPACER.join(MESSAGE))
                time.sleep(DELAY)
            print('Password Cracker, by Al Sweigart al@inventwithpython.com 2024')
            sys.exit()

        for i, is_locked in enumerate(locked_columns):
            if is_locked:
                columns[i] = MESSAGE[i]

        print(SPACER.join(columns))
        time.sleep(DELAY)

except KeyboardInterrupt:
    print('Password Cracker, by Al Sweigart al@inventwithpython.com 2024')
