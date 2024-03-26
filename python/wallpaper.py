import time

WALLPAPER = 'angles'

DELAY = 0.4
WIDTH = 80

WALLPAPER_PATTERNS = {  # Change as desired; All rows must be the same length.
    'shining carpet': [
        r'_ \ \ \_/ __',
        r' \ \ \___/ _',
        r'\ \ \_____/ ',
        r'/ / / ___ \_',
        r'_/ / / _ \__',
        r'__/ / / \___',
    ],
    'little hex': [
        r'/ \_',
        r'\_/ ',
    ],
    'big hex': [
        r' /   \    ',
        r'/     \___',
        r'\     /   ',
        r' \___/    ',
    ],
    'hex in hex': [
        r' / __ \ \__/',
        r'/ /  \ \____',
        r'\ \__/ / __ ',
        ' \\____/ /  \\',
    ],
    'bricks': [
        '___|',
        '_|__',
    ],
    'vines': [
        '((   )',
        ' )) ( ',
    ],
    'clover': [
        r'\__   ',
        r'/  \__',
        r'\     ',
        r'/   __',
        r'\__/  ',
        r'/     ',
    ],
    'skull': [
        r'/ ___ \ ^ ',
        r' /   \ VVV',
        r'|() ()|   ',
        r' \ ^ / ___',
        r'\ VVV /   ',
        r')|   |() (',
    ],
    'leaves': [
        r'  /\  ',
        r'_/  \_',
        r'\    /',
        r' \__/ ',
    ],
    'angles': [
        '\\/',
        '/ ',
        '\\ ',
        '/\\',
        ' /',
        ' \\',
    ],
}



wallpaper_rows = WALLPAPER_PATTERNS[WALLPAPER]
x_repeat = WIDTH // len(wallpaper_rows[0])

while True:
    # Display each row in wallpaper_rows:
    for row in wallpaper_rows:
        print(row * x_repeat)
        time.sleep(DELAY)
    