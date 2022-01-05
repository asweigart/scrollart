import time, shutil

width = shutil.get_terminal_size()[0]

number = 0

while True:
    numberAsString = str(number)
    print('0' * (width - len(numberAsString) - 1) + numberAsString)

    number += 1
