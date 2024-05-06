import time, shutil

WIDTH = shutil.get_terminal_size()[0] - 1
DELAY = 0.5

WORM_LENGTH = 3

stretched_body = 'o' + ('o' * (WORM_LENGTH * 2)) + 'o'
bunched_body = 'o' + ('O' * WORM_LENGTH) + 'o'
indent = 0
while indent + WORM_LENGTH * 2 + 2 < WIDTH:
    backspaces_str = "\b" * (indent + WORM_LENGTH * 2 + 2)

    indentation_str = ' ' * indent
    print(backspaces_str + indentation_str + stretched_body, flush=True, end='')
    time.sleep(DELAY)

    indent += WORM_LENGTH

    indentation_str = ' ' * indent
    print(backspaces_str + indentation_str + bunched_body, flush=True, end='')
    time.sleep(DELAY)
print()
