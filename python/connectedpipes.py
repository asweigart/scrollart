import random, time, shutil, os

os.system('cls | clear')  # Clear the screen

# Constants for settings:
DELAY = 0.2
WIDTH = shutil.get_terminal_size()[0] - 1
GAP_PROBABILITY = 0.96

# This setting changes the behavior to create the "long vertical style" if greater than 0.0:
VERTICAL_STYLE_FACTOR = 1.0  # Set between 0.0 and 1.0

# Constants for printed characters:
UP_DOWN_CHAR         = chr(9474)  # Character 9474 is '│'
LEFT_RIGHT_CHAR      = chr(9472)  # Character 9472 is '─'
DOWN_RIGHT_CHAR      = chr(9484)  # Character 9484 is '┌'
DOWN_LEFT_CHAR       = chr(9488)  # Character 9488 is '┐'
UP_RIGHT_CHAR        = chr(9492)  # Character 9492 is '└'
UP_LEFT_CHAR         = chr(9496)  # Character 9496 is '┘'
UP_DOWN_RIGHT_CHAR   = chr(9500)  # Character 9500 is '├'
UP_DOWN_LEFT_CHAR    = chr(9508)  # Character 9508 is '┤'
DOWN_LEFT_RIGHT_CHAR = chr(9516)  # Character 9516 is '┬'
UP_LEFT_RIGHT_CHAR   = chr(9524)  # Character 9524 is '┴'
CROSS_CHAR           = chr(9532)  # Character 9532 is '┼'
EMPTY = ' '

# The previous printed row; initialize to up-left-right characters:
prev_row = [UP_LEFT_RIGHT_CHAR] * WIDTH


try:
    while True:  # Main loop
        row = []  # Character strings to print in this row.
        for i, prev_char in enumerate(prev_row):
            # Figure out if we need to connect the left side:
            if i == 0:
                left_connect = False
                # Uncomment this if you do want pipes to sometimes connect off of the left edge:
                #left_connect = random.choice((True, False))
            else:
                if row[i - 1] in (LEFT_RIGHT_CHAR, DOWN_RIGHT_CHAR, UP_RIGHT_CHAR, UP_DOWN_RIGHT_CHAR, DOWN_LEFT_RIGHT_CHAR, UP_LEFT_RIGHT_CHAR, CROSS_CHAR):
                    left_connect = True
                else:
                    left_connect = False

            # Figure out if we need to connect the up side:
            if prev_char in (UP_DOWN_CHAR, DOWN_RIGHT_CHAR, DOWN_LEFT_CHAR, UP_DOWN_RIGHT_CHAR, UP_DOWN_LEFT_CHAR, DOWN_LEFT_RIGHT_CHAR, CROSS_CHAR):
                up_connect = True
            else:
                up_connect = False

            # The downward and right side connection can be either:
            down_connect = random.choice((True, False))
            if random.random() < GAP_PROBABILITY:
                down_connect = False

            if i == WIDTH - 1:
                # make the rightmost column never connect off the right edge:
                right_connect = False
                # Additional check so that we don't make the pipe go off the right edge:
                shape = (up_connect, down_connect, left_connect, right_connect)
                if shape == (False, False, True, False):
                    # Make this a left-down pipe:
                    down_connect = True
                elif shape == (False, True, False, False):
                    # Make this an empty space:
                    down_connect = False
                elif shape == (True, False, False, False):
                    # Make this an up-down pipe:
                    down_connect = True
            else:
                right_connect = random.choice((True, False))
                if random.random() < GAP_PROBABILITY:
                    right_connect = False

            # Override right_connect value if VERTICAL_STYLE_FACTOR is greater than 0.0:
            if random.random() < VERTICAL_STYLE_FACTOR:
                right_connect = False
                # Note that we'll still have right connections sometimes because the dictionary
                # below will sometimes randomly choose it to keep a connected picture.
                # Adding the following code is what will guarantee no right connections ever exist,
                # which means no left connections will ever exist (unless we allow them off the left edge)
                # and therefore only empty spaces are printed:
                ## Additional check so that we don't make the pipe go off the right edge:
                #shape = (up_connect, down_connect, left_connect, right_connect)
                #if shape == (False, False, True, False):
                #    # Make this a left-down pipe:
                #    down_connect = True
                #elif shape == (False, True, False, False):
                #    # Make this an empty space:
                #    down_connect = False
                #elif shape == (True, False, False, False):
                #    # Make this an up-down pipe:
                #    down_connect = True

            # Uncomment this if you do want pipes to sometimes connect off of the right edge:
            # (This disables the IS_LONG_VERTICAL_STYLE effect as well, if it is set.)
            #right_connect = random.choice((True, False))

            # Get the character to print based on the connections to the four other sides:
            shape = (up_connect, down_connect, left_connect, right_connect)
            char = None
            char = {
                # Up   Down  Left  Right
                (True, True, True, True):     CROSS_CHAR,
                (True, True, True, False):    UP_DOWN_LEFT_CHAR,
                (True, True, False, True):    UP_DOWN_RIGHT_CHAR,
                (True, True, False, False):   UP_DOWN_CHAR,
                (True, False, True, True):    UP_LEFT_RIGHT_CHAR,
                (True, False, True, False):   UP_LEFT_CHAR,
                (True, False, False, True):   UP_RIGHT_CHAR,
                (True, False, False, False):  random.choice((UP_DOWN_RIGHT_CHAR, UP_DOWN_CHAR, UP_RIGHT_CHAR)),
                (False, True, True, True):    DOWN_LEFT_RIGHT_CHAR,
                (False, True, True, False):   DOWN_LEFT_CHAR,
                (False, True, False, True):   DOWN_RIGHT_CHAR,
                (False, True, False, False):  DOWN_RIGHT_CHAR, # This is forced to be down right
                (False, False, True, True):   LEFT_RIGHT_CHAR,
                (False, False, True, False):  random.choice((DOWN_LEFT_RIGHT_CHAR, DOWN_LEFT_CHAR, LEFT_RIGHT_CHAR)),
                (False, False, False, True):  DOWN_RIGHT_CHAR, # This is forced to be down right
                (False, False, False, False): EMPTY,
            }[shape]
            assert char is not None
            row.append(char)
        assert len(row) == len(prev_row) == WIDTH
        print(''.join(row))
        prev_row = row
        time.sleep(DELAY)



except KeyboardInterrupt:
    print('Connected Pipes, by Al Sweigart al@inventwithpython.com 2024')
