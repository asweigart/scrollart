import random, time, os, math

WIDTH = os.get_terminal_size()[0] - 1
DELAY = 0.01

steps_before_switch = 20

BLOCK_CHAR = '#'
BLOCK_WIDTH = 14

empty_chars = list('~                                          ')

try:
    pos = 0
    speed = 0
    step = 0
    total_steps = 0
    direction = 'right'
    while True:
        if step > steps_before_switch and direction == 'right':
            speed += 1
            pos += speed
            if pos > WIDTH - BLOCK_WIDTH:
                pos = WIDTH - BLOCK_WIDTH
                step = 0
                speed = 0
                direction = 'left'
                steps_before_switch = random.randint(10, 40)  # was 20, 70
                if len(empty_chars) > 4:
                    empty_chars.pop()
                    empty_chars.pop()
                    empty_chars.pop()
        elif step > steps_before_switch and direction == 'left':
            speed -= 1
            pos += speed
            if pos < 0:
                pos = 0
                step = 0
                speed = 0
                direction = 'right'
                steps_before_switch = random.randint(1, 20)   # was 10, 40
                if len(empty_chars) > 4:
                    empty_chars.pop()
                    empty_chars.pop()
                    empty_chars.pop()

        for i in range(BLOCK_WIDTH // 2):
            columns = [random.choice(empty_chars) for i in range(WIDTH)]
            for i in range(pos, pos + BLOCK_WIDTH):
                columns[i] = BLOCK_CHAR
            print(''.join(columns))
        time.sleep(DELAY)
        
        step += 1
        total_steps += 1
        if total_steps == 1000:
            total_steps = 0
            empty_chars = list('~                                          ')

except KeyboardInterrupt:
    print('Forth and Back by Al Sweigart al@inventwithpython.com 2024')
    
