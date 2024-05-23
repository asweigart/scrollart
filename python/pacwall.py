import random, os, shutil, time

os.system('cls | clear')  # Clear the screen


WIDTH = shutil.get_terminal_size()[0] - 1
DELAY = 0.1
SIZE = 5
EMPTY_CHAR = ' '

CHARS = list('\\/-|')

def pacwall():
    while True:
        columns = []
        for i in range(WIDTH // (SIZE * 2)):
            random_char = random.choice(CHARS)
            for j in range(SIZE):
                columns.append(random_char)
                columns.append(EMPTY_CHAR)

        for j in range(SIZE):
            yield ''.join(columns)


try:
    scroll_iterator = pacwall()
    while True:
        for i in range(SIZE):
            print(next(scroll_iterator))
        time.sleep(DELAY)

except KeyboardInterrupt:
    print('Pacwall, by Al Sweigart al@inventwithpython.com 2024')
