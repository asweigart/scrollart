 # Press Ctrl-C to stop the program.
import random, time, os

change_amount = 0.5  # How fast the density changes.
density = 0.0

while True:
    width = os.get_terminal_size()[0] - 1
    if density < 0 or density > 100:
        change_amount *= -1  # Reverse the density direction.
    density = density + change_amount

    line = ''  # Create the line of asterisks.
    for i in range(width):
        if random.randint(0, 100) < density:
            line = line + '*'  # Add an asterisk.
        else:
            line = line + ' '  # Add an empty space.

    print(line)
    time.sleep(0.02)