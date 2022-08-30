import time

DELAY = 0.1
while True:
    print('\b|', end='', flush=True)
    time.sleep(DELAY)
    print('\b/', end='', flush=True)
    time.sleep(DELAY)
    print('\b-', end='', flush=True)
    time.sleep(DELAY)
    print('\b\\', end='', flush=True)
    time.sleep(DELAY)
