import time, os


WIDTH = os.get_terminal_size()[0] - 1
DELAY = 0.002



EMPTY_CHAR = ' '
SWEEP_CHAR = '@'

os.system('cls | clear')

try:
    pos = 0
    
    columns = [EMPTY_CHAR] * WIDTH
    sweepOn = True
    while True:
        if sweepOn:
            columns[pos] = SWEEP_CHAR
        else:
            columns[pos] = EMPTY_CHAR

        pos += 1
        if pos >= WIDTH:
            pos = 0
            sweepOn = not sweepOn

        print(''.join(columns))
        time.sleep(DELAY)
        
except KeyboardInterrupt:
    print('Diagonal Sweep, by Al Sweigart al@inventwithpython.com 2024')