import time

chars = ['|', '/', '-', '\\']

i = 0
while True:
    print(chars[i % 4], end='', flush=True)
    time.sleep(0.1)
    print('\b', end='', flush=True)

    i += 1