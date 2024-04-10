import random, time, os

os.system('cls | clear')  # Clear the screen
WIDTH = 79 #os.get_terminal_size()[0] - 1

DELAY = 0.04

EMPTY_CHARS = '. '
TRAVELER_CHARS = '@Oo'

STAY_IN_MIN = 6
STAY_IN_MAX = 20
MAX_CAPACITY = 22  # max num of travelers
CAPACITY_INC_EVERY = 10
CAPACITY_DEC_EVERY = 3
NEW_TRAVELER_PROB = 0.3


capacity = 1
step = 0
increasing_capacity = True
travelers = []  # [position, destination, duration, direction, char]
try:
    while True:
        step += 1  # next step

        if increasing_capacity and step == CAPACITY_INC_EVERY:
            step = 0
            capacity += 1
            if capacity == MAX_CAPACITY:
                increasing_capacity = False
        elif not increasing_capacity and step >= CAPACITY_DEC_EVERY and len(travelers) < capacity:
            step = 0
            capacity -= 1
            if capacity == 0:
                increasing_capacity = True

        if len(travelers) < capacity and random.random() <= NEW_TRAVELER_PROB:
            if random.randint(0, 1) == 0:
                # Add to left side
                travelers.append([0, random.randint(5, WIDTH - 1 - 5), random.randint(STAY_IN_MIN, STAY_IN_MAX), 'L', random.choice(TRAVELER_CHARS)]) # [current_position, destination_col, time_to_live]
            else:
                # Add to right side
                travelers.append([WIDTH - 1, random.randint(5, WIDTH - 1 - 5), random.randint(STAY_IN_MIN, STAY_IN_MAX), 'R', random.choice(TRAVELER_CHARS)]) # [current_position, destination_col, time_to_live]

        # Print all travelers
        line = [random.choice(EMPTY_CHARS) for i in range(WIDTH)]
        for traveler in travelers:
            line[traveler[0]] = traveler[4]
        #print(''.join(line), len(travelers), capacity, increasing_capacity)
        print(''.join(line))


        # Move all travelers
        to_delete = []
        for i, traveler in enumerate(travelers):
            if (traveler[0] == 0 and traveler[3] == 'L' and traveler[2] == 0) or (traveler[0] == WIDTH - 1 and traveler[3] == 'R' and traveler[2] == 0):
                # traveler is just about to move out of space
                to_delete.append(i)
            elif traveler[0] != traveler[1] and traveler[2] != 0:
                # Move traveler in
                if traveler[3] == 'L':
                    traveler[0] += 1 # move in, from left
                elif traveler[3] == 'R':
                    traveler[0] -= 1 # move in, from right
                else:
                    assert False
            elif traveler[0] != traveler[1] and traveler[2] == 0:
                # Move traveler out
                if traveler[3] == 'L':
                    traveler[0] -= 1 # move out, from left
                elif traveler[3] == 'R':
                    traveler[0] += 1 # move out, from right
                else:
                    assert False
            else:
                # traveler is in and streaming, decrement stay
                traveler[2] -= 1
                #if len(travelers) > capacity:
                #    traveler[2] -= 2  # extra decrease if over capacity
                #    if traveler[2] < 0:
                #        traveler[2] == 0
                if traveler[2] == 0:
                    # Start to move out
                    if traveler[3] == 'L':
                        traveler[0] -= 1
                    elif traveler[3] == 'R':
                        traveler[0] += 1
                    else:
                        assert False

        # Delete outed travelers
        for i in reversed(to_delete):
            del travelers[i]

        time.sleep(DELAY)
except KeyboardInterrupt:
    print('In and Out, by Al Sweigart al@inventwithpython.com 2024')
