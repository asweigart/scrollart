import time, os, random, math


WIDTH = os.get_terminal_size()[0] - 1
DELAY = 0.15

SHIFT_ATTEMPTS = 3
SHIFT_PROB  = 0.2
RESIZE_PROB = 0.1
RESET_STEP = 1000
STARTING_CHARS = list('_|' * 10)



os.system('cls | clear')
step = 0
try:
    while True:
        if step % RESET_STEP == 0:
            step = 0
            columns = []
            CHARS = STARTING_CHARS[:]
            for i in range(len(CHARS)):
                columns.extend(list(CHARS[i] * (math.ceil(WIDTH / len(CHARS)))))

            while len(columns) > WIDTH:
                columns.pop()



        # Shifting
        for i in range(SHIFT_ATTEMPTS):
            if random.random() < SHIFT_PROB:
                columns.insert(0, columns.pop())
            if random.random() < SHIFT_PROB:
                columns.append(columns.pop(0))

        # Widening / Shrinking
        for i in range(len(columns) - 1):
            if columns[i] != columns[i + 1] and random.random() < RESIZE_PROB:
                if random.randint(0, 1) == 0:
                    columns[i] = columns[i + 1]
                else:
                    columns[i + 1] = columns[i]

        print(''.join(columns))
        step += 1
        if step % random.randint(5, 10) == 0:
            time.sleep(DELAY)
        
except KeyboardInterrupt:
    print('Candlelight, by Al Sweigart al@inventwithpython.com 2026')