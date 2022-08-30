import random, time, os

DELAY = 0.1

FORWARD_SLASH = chr(9585)
BACK_SLASH = chr(9586)

def main():
    while True:
        width = os.get_terminal_size()[0] - 1
        for x in range(width):
            if random.randint(0, 1) == 1:
                print(FORWARD_SLASH, end='')
            else:
                print(BACK_SLASH, end='')
        print(flush=True)
        time.sleep(DELAY)

try:
    main()
except KeyboardInterrupt:
    print('Diagonal Maze in Python, by Al Sweigart al@inventwithpython.com')
