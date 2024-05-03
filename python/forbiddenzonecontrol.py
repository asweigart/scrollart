"""
Put this program and the main forbiddenzone.py program in the same folder.
Run them both from separate terminal windows, and then type numbers 1 
through 30 in the control program to start different sequences.
"""

import time

while True:
    response = input('> ')
    if response.isdigit():
        response += ' '  # add space since one is expected, this was a hack needed because I check the value with startswith() instead of == and both, like, 1 and 10 start with 1.
    with open('running.txt', 'w') as fp:
        fp.write(response)
