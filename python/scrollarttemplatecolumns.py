# This is a template for doing "columns" scroll art, where the output is best
# thought of as each column in the terminal window set to a certain character
# or some bit of data that dictates what this column's character is.
# This particular program is the "Toggler" scroll art piece.

# You want to import at least the following modules:
# time - Using sleep() to adjust the speed of the scrolling.
# shutil - Using get_terminal_size() to get the width of the terminal window.
# random - Most scroll art uses randomness to create dynamic, non-repeating scroll art.
import time, shutil, random

# Scroll art programs make heavy use of constants so that it's easy to adjust
# these for different effects. Almost all scroll art has the following 
# constants:

# DELAY is passed to time.sleep() and sets the general speed of scrolling.
DELAY = 0.05

# WIDTH is the width of the scroll art output. We want to set it to the
# size of the terminal window (which defaults to 80 if this isn't run
# from a terminal window.) In Python, shutil.get_terminal_size() is
# preferable to run over os.get_terminal_size() (see docs for details,
# but they are pretty much the same). This returns (width, height), so
# the [0] is to get the width. The `- 1` part is because printing a
# character in the rightmost column automatically adds a newline on
# Windows and inserts extra blank lines in the output (this doesn't
# happen on macOS and Linux.)
# You can also put this assignment inside the main loop, so that the
# output adjusts if the user resizes the window while the scroll art
# program is running. For simplicity, I just set it once at the start.
WIDTH = shutil.get_terminal_size()[0] - 1

# Several scroll art programs have a probability for how frequently
# some element is printed. It's easiest to set these as a float number
# between 0.0 (0%) and 1.0 (100%).
# Be sure to document the range of values 
TOGGLER_DENSITY = 0.1  # Set between 0.0 and 1.0

# Use constants to make it easy to change the characters printed for 
# experimentation. It's like how CSS lets you easily change the style used
# in HTML web pages.
CHAR_A = '@'
CHAR_B = '.'

# This is a constant specific to this particular program:
DIRECTIONS = [-1, 1]  # Set to a small, nonzero integers (about 1 to 3)


# Since scroll art programs are often short, I often don't use a main()
# function and stick to using global variables. It just makes writing the
# programs easier and, unintuitively, more readable and maintainable.
# I found it quite easy to copy/paste this code with indentation as a
# function into other Python programs.
# The try block here checks for the user pressing Ctrl-C to stop the
# program. This standard way to terminate a running terminal program works
# better than checking for the Esc or Q key press. The user can also always
# just close the terminal window too.
try:
    # I use a list variable named "columns" to either contain literally the
    # single character string printed for this column, or some piece of data
    # that dictates what single character string is printed for this column.
    # Python's list replication with the * operator is useful here:
    columns = [CHAR_B] * WIDTH

    togglers = [] # Tuple of (x position, integer direction)

    while True:
        # We can use random.random() as a simple way to check against a 
        # certain level of probability:
        if random.random() < TOGGLER_DENSITY:
            # Add a new toggler:
            togglers.append({'xpos': random.randint(0, WIDTH - 1), 
                             'dir': random.choice(DIRECTIONS)})

        # When making columns-style scroll art, it's important to never try
        # to print beyond the left-right boundaries of the width of the 
        # scroll art.

        # Remove out of bounds togglers:
        for i in range(len(togglers) - 1, -1, -1):
            if togglers[i]['xpos'] < 0 or togglers[i]['xpos'] >= WIDTH:
                del togglers[i]

        # Move the togglers and toggler the column chars:
        for i in range(len(togglers)):
            togglerPosition = togglers[i]['xpos']
            togglerDirection = togglers[i]['dir']

            if columns[togglerPosition] == CHAR_A:
                columns[togglerPosition] = CHAR_B
            elif columns[togglerPosition] == CHAR_B:
                columns[togglerPosition] = CHAR_A

            togglers[i]['xpos'] += togglerDirection  # Move the toggler.

        # Usually it's the end of main loop where I print the current row
        # and then pause the program:
        print(''.join(columns))
        time.sleep(DELAY)

# Catch the Ctrl-C press and suppress the error. Instead, print the title,
# your name, your contact info, and the year you made the art after the 
# program teriminates. (If you display this at the start of the program, 
# they'll likely forget while watching the scroll art.)
except KeyboardInterrupt:
    print('"Columns" Scroll Art Template, by Al Sweigart al@inventwithpython.com 2024')
