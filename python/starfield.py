import random, time, os

DELAY = 0.02

def main():
    change_amount = 0.5
    density = 0.0
    while True:
        width = os.get_terminal_size()[0] - 1
        if density < 0 or density > 100:
            change_amount *= -1
        density = density + change_amount

        line = ''
        for i in range(width):
            if random.randint(0, 100) < density:
                line = line + '*'
            else:
                line = line + ' '

        print(line); time.sleep(DELAY)

try:
    main()
except KeyboardInterrupt:
    print('Starfield, by Al Sweigart al@inventwithpython.com')
