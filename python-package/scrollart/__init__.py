"""
A module that contains several implementations of various scroll art.

Individual functions implement scroll art, and make use of the WIDTH and DELAY global variables.

The *_simple() functions are variations whose code is more understandable to beginners and has a fixed configuration.
"""

# TODO - Add the -1 adjustment to width for Windows platforms.

import os, sys, random, shutil, time, argparse, math

def main():
    parser = argparse.ArgumentParser(
        description="ScrollArt - Various animated scroll art displays",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''Available commands:
  starfield         - Animated starfield with pulsing density of stars
  stripeout         - Alternating fill/empty effect with block or random patterns  
  twists            - Vertical columns that twist around each other
  tsuro             - Infinite maze-like patterns using interconnected tiles
  pipe_swap         - Vertical pipes that occasionally swap positions
  skybursts         - Random firework-like bursts radiating from points
  forth_and_back    - Block that bounces back and forth with acceleration
  moire             - Overlapping circles with sine wave creating moire patterns
  skulls_and_hearts - Hearts floating over a background of skull patterns
  pac_wall          - Vertical columns of alternating characters and spaces
  inchworm          - Animated worm that stretches and bunches as it moves
  connected_pipes   - Network of connected pipes using box-drawing characters
  diagonal_sweep    - Diagonal sweep pattern that alternates between on and off
  earthworm_tunnels - Worms digging tunnels through dirt that grows back
  towers_and_towers - Animated tower construction with overlapping structures
  any_size_diagonal_maze - Diagonal maze pattern with random forward and back slashes
  thorns             - Random length thorn lines centered on screen
  triangle_hall      - Animated strut points creating triangular patterns
  vertical_struts    - Vertical struts with horizontal crossbeams at random positions
  hex_portals        - Hexagonal portals with optional interior patterns
  toggler1           - Moving togglers that flip characters between two states
  toggler2           - Paired togglers creating triangular wave patterns
  tri_grid_scaffold  - Triangular grid scaffolding with varying density
  orbital_travels    - Multiple characters orbiting in sine wave patterns
  snail_trail        - Animated snails leaving trails as they crawl across
  password_cracker   - Matrix-style password cracking animation
  dna                - Animated DNA double helix structure
  spike              - Growing and shrinking spike pattern using terminal width
  zigzag             - Simple zig zag animation that bounces left and right
  diamond_sky        - Falling diamonds of various sizes with random patterns
  ducklings          - Screensaver of many adorable ducklings
  full_of_squares    - Falling squares using Unicode box-drawing characters
  in_and_out         - Travelers moving in and out from screen edges with dynamic capacity
  matrix             - Matrix-style digital rain with falling streams of characters
  sine_message       - Message that oscillates horizontally using sine wave motion
  proton_stream      - Multiple streams that move while maintaining distance constraints
  striped_triangles  - Animated triangular patterns with changing density
  math_func          - Mathematical visualization using Unicode block characters
  cube_wall          - Wall of 3D cubes with random shading patterns
  bundfc             - Architectural waves inspired by Shanghai's Bund Financial Center''')
    parser.add_argument('command', nargs='?', choices=['starfield', 'stripeout', 'twists', 'tsuro', 'pipe_swap', 'skybursts', 'forth_and_back', 'moire', 'skulls_and_hearts', 'pac_wall', 'inchworm', 'connected_pipes', 'diagonal_sweep', 'earthworm_tunnels', 'towers_and_towers', 'any_size_diagonal_maze', 'thorns', 'triangle_hall', 'vertical_struts', 'hex_portals', 'toggler1', 'toggler2', 'tri_grid_scaffold', 'orbital_travels', 'snail_trail', 'password_cracker', 'dna', 'spike', 'zigzag', 'diamond_sky', 'ducklings', 'full_of_squares', 'in_and_out', 'matrix', 'sine_message', 'proton_stream', 'striped_triangles', 'math_func', 'cube_wall', 'bundfc'], 
                       help='The scroll art command to run')
    
    args = parser.parse_args()
    
    credit = ''
    try:
        if args.command == 'starfield':
            credit = 'Starfield by Al Sweigart al@inventwithpython.com 2024'
            starfield()
        elif args.command == 'stripeout':
            credit = 'Stripe Out by Al Sweigart al@inventwithpython.com 2024'
            stripeout()
        elif args.command == 'twists':
            credit = 'Twists, by Al Sweigart al@inventwithpython.com 2024'
            twists()
        elif args.command == 'tsuro':
            credit = 'Tsuro Scroll, by Al Sweigart al@inventwithpython.com'
            tsuro()
        elif args.command == 'pipe_swap':
            credit = 'Pipe Swap, by Al Sweigart al@inventwithpython.com 2025'
            pipe_swap()
        elif args.command == 'skybursts':
            credit = 'Sky Bursts, by Al Sweigart al@inventwithpython.com 2024'
            skybursts()
        elif args.command == 'forth_and_back':
            credit = 'Forth and Back by Al Sweigart al@inventwithpython.com 2024'
            forth_and_back()
        elif args.command == 'moire':
            credit = 'Moire, by Al Sweigart al@inventwithpython.com 2024'
            moire()
        elif args.command == 'skulls_and_hearts':
            credit = 'Skulls and Hearts, by Al Sweigart al@inventwithpython.com 2024'
            skulls_and_hearts()
        elif args.command == 'pac_wall':
            credit = 'Pacwall, by Al Sweigart al@inventwithpython.com 2024'
            pac_wall()
        elif args.command == 'inchworm':
            credit = 'Inchworm, by Al Sweigart al@inventwithpython.com 2024'
            inchworm()
        elif args.command == 'connected_pipes':
            credit = 'Connected Pipes, by Al Sweigart al@inventwithpython.com 2024'
            connected_pipes()
        elif args.command == 'diagonal_sweep':
            credit = 'Diagonal Sweep, by Al Sweigart al@inventwithpython.com 2024'
            diagonal_sweep()
        elif args.command == 'earthworm_tunnels':
            credit = 'Earthworm Tunnels, by Al Sweigart al@inventwithpython.com 2024'
            earthworm_tunnels()
        elif args.command == 'towers_and_towers':
            credit = 'Towers and Towers, by Al Sweigart al@inventwithpython.com 2024'
            towers_and_towers()
        elif args.command == 'any_size_diagonal_maze':
            credit = 'Any Size Diagonal Maze, by Al Sweigart al@inventwithpython.com 2024'
            any_size_diagonal_maze()
        elif args.command == 'thorns':
            credit = 'Thorns, by Al Sweigart al@inventwithpython.com 2024'
            thorns()
        elif args.command == 'triangle_hall':
            credit = 'Triangle Hall, by Al Sweigart al@inventwithpython.com 2024'
            triangle_hall()
        elif args.command == 'vertical_struts':
            credit = 'Vertical Struts, by Al Sweigart al@inventwithpython.com 2024'
            vertical_struts()
        elif args.command == 'hex_portals':
            credit = 'Hex Portals, by Al Sweigart al@inventwithpython.com 2024'
            hex_portals()
        elif args.command == 'toggler1':
            credit = 'Toggler 1, by Al Sweigart al@inventwithpython.com 2024'
            toggler1()
        elif args.command == 'toggler2':
            credit = 'Toggler 2, by Al Sweigart al@inventwithpython.com 2024'
            toggler2()
        elif args.command == 'tri_grid_scaffold':
            credit = 'Tri Grid Scaffolding, by Al Sweigart al@inventwithpython.com 2024'
            tri_grid_scaffold()
        elif args.command == 'orbital_travels':
            credit = 'Orbital Travels, by Al Sweigart al@inventwithpython.com 2024'
            orbital_travels()
        elif args.command == 'snail_trail':
            credit = 'Snail Trail, by Al Sweigart al@inventwithpython.com 2024'
            snail_trail()
        elif args.command == 'password_cracker':
            credit = 'Password Cracker, by Al Sweigart al@inventwithpython.com 2024'
            password_cracker()
        elif args.command == 'dna':
            credit = 'DNA, by Al Sweigart al@inventwithpython.com 2024'
            dna()
        elif args.command == 'spike':
            credit = 'Spike, by Al Sweigart al@inventwithpython.com 2024'
            spike()
        elif args.command == 'zigzag':
            credit = 'Zigzag, by Al Sweigart al@inventwithpython.com'
            zigzag()
        elif args.command == 'diamond_sky':
            credit = 'Diamond Sky, by Al Sweigart al@inventwithpython.com 2024'
            diamond_sky()
        elif args.command == 'ducklings':
            credit = 'Ducklings, by Al Sweigart al@inventwithpython.com 2021'
            ducklings()
        elif args.command == 'full_of_squares':
            credit = 'Full of Squares, by Al Sweigart al@inventwithpython.com 2024'
            full_of_squares()
        elif args.command == 'in_and_out':
            credit = 'In and Out, by Al Sweigart al@inventwithpython.com 2024'
            in_and_out()
        elif args.command == 'matrix':
            credit = 'Matrix Screensaver, by Al Sweigart al@inventwithpython.com 2021'
            matrix()
        elif args.command == 'sine_message':
            credit = 'Sine Message, by Al Sweigart al@inventwithpython.com 2021'
            sine_message()
        elif args.command == 'proton_stream':
            credit = 'Proton Stream, by Al Sweigart al@inventwithpython.com 2024'
            proton_stream()
        elif args.command == 'striped_triangles':
            credit = 'Striped Triangles, by Al Sweigart al@inventwithpython.com'
            striped_triangles()
        elif args.command == 'math_func':
            credit = 'Math Function Visualization, by Al Sweigart al@inventwithpython.com'
            math_func()
        elif args.command == 'cube_wall':
            credit = 'Cube Wall, by Al Sweigart al@inventwithpython.com 2022'
            cube_wall()
        elif args.command == 'bundfc':
            credit = 'BundFC by Al Sweigart al@inventwithpython.com 2024'
            bundfc()
        else:
            parser.print_help()
    except KeyboardInterrupt:
        print(credit)


def starfield(change_amount=0.005, delay=0.02, star_char='*', empty_char=' ', width=None, max_rows=None):
    density = 0.0
    row_count = 0

    while True:
        if width is None:
            _width = shutil.get_terminal_size()[0]
        else:
            _width = width
        if sys.platform == 'win32':
            _width -= 1  # Windows terminals insert a newline if something is printed in the last column

        if density < 0 or density > 1.0:
            change_amount *= -1
        density = density + change_amount

        line = []
        for i in range(_width):
            if random.random() < density:
                line.append(star_char)
            else:
                line.append(empty_char)

        print(''.join(line))
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
        time.sleep(delay)


def starfield_simple():
    change_amount = 0.005
    density = 0.0
    width = 80
    while True:
        if density < 0 or density > 1.0:
            change_amount *= -1
        density = density + change_amount

        line = ''
        for i in range(width):
            if random.random() < density:
                line = line + '*'
            else:
                line = line + ' '

        print(line)
        time.sleep(0.02)


def stripeout_simple():
    """A simplified version of stripeout with fixed configuration for beginners."""
    fill_chars = '#@O.:!'
    empty_chars = ' '
    delay = 0.004
    height = 40
    max_wipes = 99
    width = 80
    
    simultaneous_stripes = width // 10
    block_mode = False
    
    def get_contiguous_columns_of_length(columns_left, length):
        contiguous_columns = set()
        for i in range(width):
            if all([i + x in columns_left for x in range(length)]):
                contiguous_columns.add(i)
        return contiguous_columns

    columns = [random.choice(empty_chars)] * width
    make_empty = False
    iteration = 0

    while True:
        columns_left = set(range(width))
        if make_empty:
            new_char = random.choice(empty_chars)
        else:
            new_char = random.choice(fill_chars)

        current_wipe_num = 1
        while len(columns_left):
            if current_wipe_num >= max_wipes:
                # change ALL of the remaining columns
                columns = [new_char] * width
                columns_left = set()
                current_wipe_num = 1
            else:
                if block_mode:
                    # Find contiguous columns (at least simultaneous_stripes in length)
                    for desired_length in range(simultaneous_stripes, 0, -1):
                        contiguous_columns = get_contiguous_columns_of_length(columns_left, desired_length)
                        if len(contiguous_columns) != 0:
                            break
                    col = random.choice(list(contiguous_columns))

                    # Remove several contiguous columns:
                    for i in range(simultaneous_stripes):
                        if col + i in columns_left:
                            columns_left.remove(col + i)
                            columns[col + i] = new_char
                else:
                    # Remove several random columns:
                    for i in range(simultaneous_stripes):
                        if len(columns_left) == 0: 
                            break
                        col = random.choice(list(columns_left))
                        columns_left.remove(col)
                        columns[col] = new_char

            # Print columns with the new_char
            for i in range(height):
                print(''.join(columns))
                time.sleep(delay)

            current_wipe_num += 1
        make_empty = not make_empty
        iteration += 1
        if iteration % 2 == 0:
            block_mode = not block_mode


def stripeout(fill_chars='#@O.:!', empty_chars=' ', delay=0.004, height=40, max_wipes=99, width=None, max_rows=None):
    """Creates an animated stripe-out effect that alternates between filling and emptying the screen."""
    
    block_mode = False
    
    def get_contiguous_columns_of_length(columns_left, length):
        contiguous_columns = set()
        for i in range(_width):
            if all([i + x in columns_left for x in range(length)]):
                contiguous_columns.add(i)
        return contiguous_columns

    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
                
    simultaneous_stripes = _width // 10
    columns = [random.choice(empty_chars)] * _width
    make_empty = False
    iteration = 0
    row_count = 0

    while True:
        columns_left = set(range(_width))
        if make_empty:
            new_char = random.choice(empty_chars)
        else:
            new_char = random.choice(fill_chars)

        current_wipe_num = 1
        while len(columns_left):
            if current_wipe_num >= max_wipes:
                # change ALL of the remaining columns
                columns = [new_char] * _width
                columns_left = set()
                current_wipe_num = 1
            else:
                if block_mode:
                    # Find contiguous columns (at least simultaneous_stripes in length)
                    for desired_length in range(simultaneous_stripes, 0, -1):
                        contiguous_columns = get_contiguous_columns_of_length(columns_left, desired_length)
                        if len(contiguous_columns) != 0:
                            break
                    col = random.choice(list(contiguous_columns))

                    # Remove several contiguous columns:
                    for i in range(simultaneous_stripes):
                        if col + i in columns_left:
                            columns_left.remove(col + i)
                            columns[col + i] = new_char
                else:
                    # Remove several random columns:
                    for i in range(simultaneous_stripes):
                        if len(columns_left) == 0: 
                            break
                        col = random.choice(list(columns_left))
                        columns_left.remove(col)
                        columns[col] = new_char

            # Print columns with the new_char
            for i in range(height):
                print(''.join(columns))
                row_count += 1
                if max_rows and row_count >= max_rows:
                    return
                time.sleep(delay)

            current_wipe_num += 1
        make_empty = not make_empty
        iteration += 1
        if iteration % 2 == 0:
            block_mode = not block_mode


def twists_simple():
    """A simplified version of twists with fixed configuration for beginners."""
    delay = 0.008
    num_columns = 5
    column_width = 8
    column_char = '|'
    empty_char = ' '
    between_twist_length_min = 0
    between_twist_length_max = 50
    twist_length = 50
    width = 80
    
    gap_size = (width - column_width) // (num_columns + 1)
    between_twist_length = random.randint(between_twist_length_min, between_twist_length_max)
    sine_step_inc = (math.pi / 2) / twist_length
    
    to_twist = random.randint(1, num_columns - 1)

    while True:
        # Set up straight columns:
        columns = [empty_char] * width
        for i in range(1, num_columns + 1):
            for j in range(column_width):
                columns[(i * gap_size) + j] = column_char

        # Print straight columns:
        for i in range(between_twist_length):
            print(''.join(columns))
            time.sleep(delay)

        # Select two adjacent columns to twist:
        to_twist += random.randint(-1, 1)
        if to_twist == 0:
            to_twist = 2
        if to_twist == num_columns:
            to_twist = num_columns - 2
        
        # Perform the twist animation
        for sine_step in range(twist_length):
            columns = [empty_char] * width

            in_transit_pos_left  = (to_twist * gap_size) + int(math.sin(sine_step * sine_step_inc) * gap_size)
            in_transit_pos_right = ((to_twist + 1) * gap_size) - int(math.sin(sine_step * sine_step_inc) * gap_size)
            
            for j in range(column_width):
                if 0 <= in_transit_pos_left + j < width:
                    columns[in_transit_pos_left + j] = column_char
                if 0 <= in_transit_pos_right + j < width:
                    columns[in_transit_pos_right + j] = column_char

            # Print straight columns (that are not being twisted currently):
            for i in range(1, num_columns + 1):
                if i == to_twist or i == to_twist + 1:
                    continue
                for j in range(column_width):
                    if 0 <= (i * gap_size) + j < width:
                        columns[(i * gap_size) + j] = column_char

            print(''.join(columns))
            time.sleep(delay)


def twists(delay=0.008, num_columns=6, column_width=12, column_char='|', empty_char=' ', 
           between_twist_length_min=0, between_twist_length_max=50, twist_length=50, width=None, max_rows=None):
    """Creates an animated twist effect with columns that twist around each other."""
    
    between_twist_length = random.randint(between_twist_length_min, between_twist_length_max)
    sine_step_inc = (math.pi / 2) / twist_length
    
    to_twist = random.randint(1, num_columns - 1)
    row_count = 0

    while True:
        if width is None:
            _width = shutil.get_terminal_size()[0]
        else:
            _width = width
        if sys.platform == 'win32':
            _width -= 1  # Windows terminals insert a newline if something is printed in the last column
        gap_size = (_width - column_width) // (num_columns + 1)

        # Set up straight columns:
        columns = [empty_char] * _width
        for i in range(1, num_columns + 1):
            for j in range(column_width):
                columns[(i * gap_size) + j] = column_char

        # Print straight columns:
        for i in range(between_twist_length):
            print(''.join(columns))
            row_count += 1
            if max_rows and row_count >= max_rows:
                return
            time.sleep(delay)

        # Select two adjacent columns to twist:
        to_twist += random.randint(-1, 1)
        if to_twist == 0:
            to_twist = 2
        if to_twist == num_columns:
            to_twist = num_columns - 2
        
        # Perform the twist animation
        for sine_step in range(twist_length):
            columns = [empty_char] * _width

            in_transit_pos_left  = (to_twist * gap_size) + int(math.sin(sine_step * sine_step_inc) * gap_size)
            in_transit_pos_right = ((to_twist + 1) * gap_size) - int(math.sin(sine_step * sine_step_inc) * gap_size)
            
            for j in range(column_width):
                if 0 <= in_transit_pos_left + j < _width:
                    columns[in_transit_pos_left + j] = column_char
                if 0 <= in_transit_pos_right + j < _width:
                    columns[in_transit_pos_right + j] = column_char

            # Print straight columns (that are not being twisted currently):
            for i in range(1, num_columns + 1):
                if i == to_twist or i == to_twist + 1:
                    continue
                for j in range(column_width):
                    if 0 <= (i * gap_size) + j < _width:
                        columns[(i * gap_size) + j] = column_char

            print(''.join(columns))
            row_count += 1
            if max_rows and row_count >= max_rows:
                return
            time.sleep(delay)


def tsuro(delay=0.1, width=None, max_rows=None):
    """Draws convoluted and twisting routes using tile patterns infinitely."""
    
    TILE_MAP = {
        '0': ' ',
        '1': chr(9472),  # '─'
        '2': chr(9474),  # '│'
        '3': chr(9484),  # '┌'
        '4': chr(9488),  # '┐'
        '5': chr(9492),  # '└'
        '6': chr(9496),  # '┘'
        '7': chr(9608),  # '█'
    }

    ROTATE_MAP = {
        '0': '0', # ' ' becomes ' '
        '1': '2', # '─' becomes '│'
        '2': '1', # '│' becomes '─'
        '3': '4', # '┌' becomes '┐'
        '4': '6', # '┐' becomes '┘'
        '5': '3', # '└' becomes '┌'
        '6': '5', # '┘' becomes '└'
        '7': '7', # '█' becomes '█'
    }

    # Tile patterns with checksums
    TILES = ['02360452115121411245036209', '05420145210202012451025408',
             '02020423115111411625020204', '02020454512054060051031406',
             '02020451212002060051031409', '02360122110220016231036204',
             '05160143110220012631020207', '36360636033603660363036360',
             '05420402232326262205025407', '02020420512200062031020204',
             '05420432633211662203515464', '05160400032000260005031408',
             '36020140512200062031020208', '05364112433112660251036366',
             '05160111110000011143031261', '02020160510000014031020200',
             '05454402052020011111545404', '32160620310202012111020202',
             '02020420512200012111521402', '02020423632514211625540208',
             '02020121113216065111031406', '32160620310202045121540208',
             '05160140310202045121540201', '02020423212521411625540204',
             '05420402515121414205025401', '05114111650000043111521403',
             '02360116310511443165521405', '02020111210202016051031405',
             '05124114323126263165025401', '36360216312316062031020201',
             '02020111210202012111020206', '02020420232202262025020208',
             '05420112633111663211025400', '05420145113116065111031404',
             '36020214232022260512031263']

    # Validate and clean tiles (remove checksum)
    for i, tile in enumerate(TILES):
        assert len(tile) == 26, f'Tile {tile!r} has an incorrect length {len(tile)}.'
        total = sum(int(digit) for digit in tile)
        assert total % 10 == 0, f'Tile {tile!r} has wrong checksum.'
        TILES[i] = tile[:25]  # Remove checksum digit

    def rotate_tile_clockwise(tile, rotations):
        """Rotate a tile clockwise by the specified number of 90-degree increments."""
        assert len(tile) == 25
        assert tile.isdecimal() and '8' not in tile and '9' not in tile

        rotations = rotations % 4
        t = tile

        for _ in range(rotations):
            rt = [' '] * 25

            # Rotate positions clockwise 90 degrees
            rt[0], rt[4],  rt[24], rt[20] = t[20], t[0], t[4],  t[24]
            rt[1], rt[9],  rt[23], rt[15] = t[15], t[1], t[9],  t[23]
            rt[2], rt[14], rt[22], rt[10] = t[10], t[2], t[14], t[22]
            rt[3], rt[19], rt[21], rt[5]  = t[5],  t[3], t[19], t[21]

            rt[6], rt[8],  rt[18], rt[16] = t[16], t[6], t[8],  t[18]
            rt[7], rt[13], rt[17], rt[11] = t[11], t[7], t[13], t[17]

            rt[12] = t[12]  # Center doesn't change position

            # Rotate the individual characters
            for i in range(25):
                rt[i] = ROTATE_MAP[rt[i]]

            t = ''.join(rt)

        return t

    # Generate and print tiles infinitely, row by row
    current_tile_row = []  # Store current row of tiles being processed
    tile_row_index = 0     # Which row within the 5x5 tiles we're currently printing
    row_count = 0
    
    while True:
        if width is None:
            _width = shutil.get_terminal_size()[0]
        else:
            _width = width
        if sys.platform == 'win32':
            _width -= 1  # Windows terminals insert a newline if something is printed in the last column

        # When starting a new set of tiles (every 5 rows)
        if tile_row_index == 0:
            current_tile_row = []
            # Generate a new row of tiles
            for x in range(0, _width, 5):
                tile = rotate_tile_clockwise(random.choice(TILES), random.randint(0, 3))
                current_tile_row.append(tile)
        
        # Build the current line from all tiles in the current tile row
        row = []
        for x in range(_width):
            tile_index = x // 5  # Which tile this column belongs to
            if tile_index < len(current_tile_row):
                tile = current_tile_row[tile_index]
                tile_x = x % 5  # Position within the 5x5 tile
                char_index = tile_x + (5 * tile_row_index)
                if char_index < len(tile):
                    row.append(TILE_MAP[tile[char_index]])
                else:
                    row.append(' ')
            else:
                row.append(' ')
        
        print(''.join(row))
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
        time.sleep(delay)
        
        # Move to next row within the 5x5 tiles
        tile_row_index = (tile_row_index + 1) % 5


def pipe_swap(width=None, delay=0.03, num_pipes=26, swap_chance=0.8, 
              swap_max_distance=20, swap_min_distance=6, max_rows=None):
    """Animated display of pipes that occasionally swap positions with connecting segments."""
    
    # Use box-drawing characters
    HORIZONTAL_PIPE = chr(9472)  # '─'
    VERTICAL_PIPE = chr(9474)    # '│'
    DOWN_RIGHT_ELBOW_PIPE = chr(9484)  # '┌'
    DOWN_LEFT_ELBOW_PIPE = chr(9488)   # '┐'
    UP_RIGHT_ELBOW_PIPE = chr(9492)    # '└'
    UP_LEFT_ELBOW_PIPE = chr(9496)     # '┘'
    EMPTY = ' '
    
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
    
    # Set up initial pipe locations:
    pipes = set()
    while len(pipes) < num_pipes:
        pipes.add(random.randint(0, _width - 1))
    
    row_count = 0
    
    # Main loop:
    while True:
        # Start with a blank row:
        row = [EMPTY] * _width

        # Fill in pipes:
        for pipe in pipes:
            if 0 <= pipe < _width:
                row[pipe] = VERTICAL_PIPE

        if random.random() >= swap_chance:
            print(''.join(row))
            row_count += 1
            if max_rows and row_count >= max_rows:
                return
            time.sleep(delay)
            continue  # Don't swap.

        # Select a pipe to swap:
        swap_pipe = random.choice(tuple(pipes))

        # Select new destination column not used by any other pipe:
        destination = random.randint(0, _width - 1)
        while (destination in pipes or 
               abs(swap_pipe - destination) > swap_max_distance or 
               abs(swap_pipe - destination) < swap_min_distance):
            destination = random.randint(0, _width - 1)

        # Update pipes data structure:
        pipes.remove(swap_pipe)
        pipes.add(destination)

        # Check which elbow pipe characters to set:
        if swap_pipe < destination:
            if 0 <= swap_pipe < _width:
                row[swap_pipe] = UP_RIGHT_ELBOW_PIPE
            if 0 <= destination < _width:
                row[destination] = DOWN_LEFT_ELBOW_PIPE
        else:
            if 0 <= swap_pipe < _width:
                row[swap_pipe] = UP_LEFT_ELBOW_PIPE
            if 0 <= destination < _width:
                row[destination] = DOWN_RIGHT_ELBOW_PIPE

        # Set horizontal pipe:
        for i in range(min(swap_pipe, destination) + 1, max(swap_pipe, destination)):
            if 0 <= i < _width and (row[i] == EMPTY or random.random() < 0.5):
                row[i] = HORIZONTAL_PIPE

        # Print the row:
        print(''.join(row))
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
        time.sleep(delay)


def skybursts(delay=0.02, burst_probability=0.01, min_num_streams=4, max_num_streams=10,
              min_stream_length=4, max_stream_length=12, burst_chars='@.', empty_chars=' ', width=None, max_rows=None):
    """Creates firework-like bursts that radiate from random points across the screen."""
    
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
    
    def normalize_img(img):
        """Normalize image coordinates to start from (0,0)."""
        normalized = {}

        if len(img) == 0:
            return {}, 0, 0

        x, y = next(iter(img.keys()))
        minx = maxx = x
        miny = maxy = y

        for x, y in img.keys():
            if x < minx:
                minx = x
            if y < miny:
                miny = y

        for x, y in img.keys():
            normalized[(x - minx, y - miny)] = img[(x, y)]

        for x, y in normalized.keys():
            if x > maxx:
                maxx = x
            if y > maxy:
                maxy = y

        return normalized, maxx + 1, maxy + 1

    def line(x1, y1, x2, y2):
        """Returns a list of points in a line between the given points using Bresenham's algorithm."""
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        isSteep = abs(y2-y1) > abs(x2-x1)
        if isSteep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
        isReversed = x1 > x2

        if isReversed:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

            deltax = x2 - x1
            deltay = abs(y2-y1)
            error = int(deltax / 2)
            y = y2
            ystep = 1 if y1 < y2 else -1
            for x in range(x2, x1 - 1, -1):
                if isSteep:
                    yield (y, x)
                else:
                    yield (x, y)
                error -= deltay
                if error <= 0:
                    y -= ystep
                    error += deltax
        else:
            deltax = x2 - x1
            deltay = abs(y2-y1)
            error = int(deltax / 2)
            y = y1
            ystep = 1 if y1 < y2 else -1
            for x in range(x1, x2 + 1):
                if isSteep:
                    yield (y, x)
                else:
                    yield (x, y)
                error -= deltay
                if error < 0:
                    y += ystep
                    error += deltax

    def get_burst(num_streams, h_radius, v_radius, burst_char):
        """Generate a burst pattern with radiating streams."""
        img = {}
        for i in range(num_streams):
            for x, y in line(0, 0, random.randint(-h_radius, h_radius), random.randint(0, v_radius)):
                img[(x, y)] = burst_char
        return img

    next_rows = []
    row_count = 0
    
    while True:
        # Ensure we have enough buffered rows
        while len(next_rows) < max_stream_length + 1:
            next_rows.append([random.choice(empty_chars) for i in range(_width)])

        # Generate bursts at random locations
        for x in range(_width - (max_stream_length * 2 + 1)):
            if random.random() < burst_probability:
                img = get_burst(random.randint(min_num_streams, max_num_streams),
                              max_stream_length, max_stream_length, random.choice(burst_chars))
                img, maxx, maxy = normalize_img(img)
                for ix in range(maxx):
                    for iy in range(maxy):
                        if (ix, iy) in img and iy < len(next_rows) and (ix + x) < _width:
                            next_rows[iy][ix + x] = img[(ix, iy)]
        
        # Output the top row and remove it
        row = next_rows[0]
        del next_rows[0]
        print(''.join(row))
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
        time.sleep(delay)


def forth_and_back(width=None, delay=0.01, block_char='#', block_width=14, 
                   initial_steps_before_switch=20, reset_interval=1000, max_rows=None):
    """A block that bounces back and forth with acceleration and deceleration."""
    
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
    
    steps_before_switch = initial_steps_before_switch
    empty_chars = list('~                                          ')
    
    pos = 0
    speed = 0
    step = 0
    total_steps = 0
    direction = 'right'
    row_count = 0
    
    while True:
        if step > steps_before_switch and direction == 'right':
            speed += 1
            pos += speed
            if pos > _width - block_width:
                pos = _width - block_width
                step = 0
                speed = 0
                direction = 'left'
                steps_before_switch = random.randint(10, 40)
                if len(empty_chars) > 4:
                    empty_chars.pop()
                    empty_chars.pop() 
                    empty_chars.pop()
        elif step > steps_before_switch and direction == 'left':
            speed -= 1
            pos += speed
            if pos < 0:
                pos = 0
                step = 0
                speed = 0
                direction = 'right'
                steps_before_switch = random.randint(1, 20)
                if len(empty_chars) > 4:
                    empty_chars.pop()
                    empty_chars.pop()
                    empty_chars.pop()

        for i in range(block_width // 2):
            columns = [random.choice(empty_chars) for j in range(_width)]
            for j in range(max(0, pos), min(_width, pos + block_width)):
                columns[j] = block_char
            print(''.join(columns))
            row_count += 1
            if max_rows and row_count >= max_rows:
                return
        
        time.sleep(delay)
        
        step += 1
        total_steps += 1
        if total_steps == reset_interval:
            total_steps = 0
            empty_chars = list('~                                          ')


def moire(width=None, delay=0.04, moire_char=':', empty_char=' ', min_circle_radius=2, 
          max_circle_radius=8, circle_density=0.3, sine_char='_', sine_width=25, 
          sine_inc=0.1, max_rows=None):
    """Creates overlapping circles with sine wave producing moire interference patterns."""
    
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
    
    def normalize_img(img):
        """Normalize image coordinates to start from (0,0)."""
        normalized = {}

        if len(img) == 0:
            return {}, 0, 0

        x, y = next(iter(img.keys()))
        minx = maxx = x
        miny = maxy = y

        for x, y in img.keys():
            if x < minx:
                minx = x
            if y < miny:
                miny = y

        for x, y in img.keys():
            normalized[(x - minx, y - miny)] = img[(x, y)]

        for x, y in normalized.keys():
            if x > maxx:
                maxx = x
            if y > maxy:
                maxy = y

        return normalized, maxx + 1, maxy + 1

    def move_img(img, movex, movey):
        """Move image by specified offset."""
        moved_img = {}
        for x, y in img.keys():
            moved_img[(x + movex, y + movey)] = img[(x, y)]
        return moved_img
        
    def get_moire(radius, centerx, centery):
        """Generate a circle using Bresenham's circle algorithm."""
        switch = 3 - (2 * radius)
        cx = 0
        cy = radius

        img = {}  # keys are (x, y), values are moire_char

        while cx <= cy:
            # Draw all 8 octants of the circle
            img[(cx + centerx, -cy + centery)] = moire_char
            img[(cy + centerx, -cx + centery)] = moire_char
            img[(cy + centerx, cx + centery)] = moire_char
            img[(cx + centerx, cy + centery)] = moire_char
            img[(-cx + centerx, cy + centery)] = moire_char
            img[(-cy + centerx, cx + centery)] = moire_char
            img[(-cy + centerx, -cx + centery)] = moire_char
            img[(-cx + centerx, -cy + centery)] = moire_char
            
            if switch < 0:
                switch = switch + (4 * cx) + 6
            else:
                switch = switch + (4 * (cx - cy)) + 10
                cy = cy - 1
            cx = cx + 1

        return img

    next_columns = []
    sine_step = 0.0
    row_count = 0
    
    while True:
        # Ensure we have enough buffered columns
        while len(next_columns) < max_circle_radius * 2 + 1:
            next_columns.append([empty_char] * _width)

        # Generate moire circles at random locations
        if random.random() < circle_density:
            moire_img = {}
            for i in range(max_circle_radius - min_circle_radius):
                circle_img = get_moire(random.randint(min_circle_radius, max_circle_radius), 
                                     max_circle_radius, max_circle_radius)
                moire_img.update(circle_img)
            
            norm_img, maxx, maxy = normalize_img(moire_img)
            if _width > (max_circle_radius * 2):
                move_x = random.randint(0, _width - (max_circle_radius * 2) - 1)
                moved_img = move_img(norm_img, move_x, 0)

                for (x, y), char in moved_img.items():
                    if 0 <= y < len(next_columns) and 0 <= x < _width:
                        next_columns[y][x] = char

        # Add sine wave to the top row
        if _width > sine_width:
            sine_pos = int(((math.sin(sine_step) + 1) / 2) * (_width - sine_width))
            for i in range(sine_width):
                if sine_pos + i < _width:
                    next_columns[0][sine_pos + i] = sine_char   
        sine_step += sine_inc

        # Output the top row and remove it
        print(''.join(next_columns[0]))
        del next_columns[0]
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
        time.sleep(delay)


def skulls_and_hearts(width=None, delay=0.2, heart_interior=':', min_heart_size=2, 
                     max_heart_size=4, heart_probability=0.001, batch_size=9, max_rows=None):
    """Hearts floating over a repeating background pattern of skulls."""
    
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
    
    SKULL_TEMPLATE = [
        r'|          ______          | (_)  (_) ', 
        r'|         /      \         |          ', 
        r'         / _    _ \         \   ^^   /', 
        r'        | (_)  (_) |         VVVVVVVV ', 
        r'        |          |          \____/  ', 
        r'         \   ^^   /           ______  ', 
         '          VVVVVVVV           /      \\ ', 
         '           \\____/           / _    _ \\'] 
    
    SKULL_TEMPLATE_HEIGHT = len(SKULL_TEMPLATE)
    SKULL_TEMPLATE_WIDTH = len(SKULL_TEMPLATE[0])
    
    def get_heart(size):
        """Generate a heart shape of the specified size."""
        img = {}  # keys are (x, y), values are characters

        for x in range(size, size * 2):
            img[(x, 0)] = '_'  # left top of heart
            img[(size * 3 + x, 0)] = '_'  # right top of heart

        for i in range(size):
            img[(size - 1 - i, i + 1)] = '/'  # left side of left side top
            img[(size - 1 - i + (size * 3), i + 1)] = '/'  # left side of right side top
            img[(size * 2 + i, i + 1)] = '\\'  # right side of left side top
            img[(size * 2 + i + (size * 3), i + 1)] = '\\'  # right side of right side top

        for i in range(size * 3):
            img[(i, i + size + 1)] = '\\'  # left side bottom slant of heart
            img[(size * 6 - i - 1, i + size + 1)] = '/'  # right side bottom slant of heart

        # Interior of heart:
        for i in range(size):
            for j in range(size):
                img[(size + i, j + 1)] = heart_interior  # left side top
                img[(size * 4 + i, j + 1)] = heart_interior  # right side top
       
            for j in range(i):
                img[(i, size - j)] = heart_interior
                img[(size * 2 + (size - i - 1), size - j)] = heart_interior 

                img[(size * 3 + i, size - j)] = heart_interior
                img[(size * 5 + (size - i - 1), size - j)] = heart_interior 

        for j in range(size * 3):
            for i in range(size * 3 - 1 - j):
                img[((size * 3) - i - 1, j + size + 1)] = heart_interior
                img[((size * 3) + i, j + size + 1)] = heart_interior

        return img

    def normalize_img(img):
        """Normalize image coordinates to start from (0,0)."""
        normalized = {}

        if len(img) == 0:
            return {}, 0, 0

        x, y = next(iter(img.keys()))
        minx = maxx = x
        miny = maxy = y

        for x, y in img.keys():
            if x < minx:
                minx = x
            if x > maxx:
                maxx = x
            if y < miny:
                miny = y
            if y > maxy:
                maxy = y

        for x, y in img.keys():
            normalized[(x - minx, y - miny)] = img[(x, y)]

        return normalized, maxx + 1, maxy + 1

    SKULL_X_REPEAT = _width // SKULL_TEMPLATE_WIDTH
    next_rows = []
    step = 0
    row_count = 0
    
    while True:
        # Ensure we have enough buffered rows
        while len(next_rows) < (max_heart_size * 4 + 1):
            skull_row = SKULL_TEMPLATE[step % SKULL_TEMPLATE_HEIGHT] * SKULL_X_REPEAT
            # Make sure the row is long enough for hearts
            skull_row += ' ' * (_width - len(skull_row))
            next_rows.append(list(skull_row[:_width]))
            step += 1

        # Generate hearts at random locations
        for x in range(_width - (max_heart_size * 7)):
            if random.random() < heart_probability:
                heart_size = random.randint(min_heart_size, max_heart_size)
                img, maxx, maxy = normalize_img(get_heart(heart_size))
                for ix in range(maxx):
                    for iy in range(maxy):
                        if ((ix, iy) in img and 
                            iy < len(next_rows) and 
                            ix + x < _width):
                            next_rows[iy][ix + x] = img[(ix, iy)]

        # Output the top row and remove it
        row = next_rows[0]
        del next_rows[0]
        print(''.join(row))
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
            
        # Batch output for performance
        if step % batch_size == 0:
            time.sleep(delay)


def pac_wall(width=None, delay=0.1, size=5, empty_char=' ', chars='\\/-|', max_rows=None):
    """Creates vertical columns of alternating characters and spaces in a wall pattern."""
    
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
    
    def pacwall_generator():
        """Generator that yields rows for the pacwall pattern."""
        while True:
            columns = []
            for i in range(_width // (size * 2)):
                random_char = random.choice(chars)
                for j in range(size):
                    columns.append(random_char)
                    columns.append(empty_char)
            
            # Ensure we have enough columns to fill the width
            while len(columns) < _width:
                columns.append(empty_char)
                
            # Trim to exact width
            columns = columns[:_width]

            for j in range(size):
                yield ''.join(columns)

    scroll_iterator = pacwall_generator()
    row_count = 0
    
    while True:
        for i in range(size):
            print(next(scroll_iterator))
            row_count += 1
            if max_rows and row_count >= max_rows:
                return
        time.sleep(delay)


def inchworm(width=None, delay=0.5, worm_length=3, stretched_char='o', bunched_char='O', max_cycles=None):
    """Animated worm that stretches and bunches as it moves across the screen."""
    
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
    
    stretched_body = stretched_char + (stretched_char * (worm_length * 2)) + stretched_char
    bunched_body = stretched_char + (bunched_char * worm_length) + stretched_char
    
    cycle_count = 0
    
    while True:
        indent = 0
        while indent + worm_length * 2 + 2 < _width:
            # Calculate how many backspaces we need to clear the previous worm
            backspaces_needed = indent + worm_length * 2 + 2
            
            # Print stretched worm
            indentation_str = ' ' * indent
            # Clear previous content and print stretched worm
            print('\r' + ' ' * _width + '\r', end='', flush=True)  # Clear line
            print(indentation_str + stretched_body, flush=True, end='')
            time.sleep(delay)

            indent += worm_length

            # Print bunched worm
            indentation_str = ' ' * indent
            # Clear previous content and print bunched worm
            print('\r' + ' ' * _width + '\r', end='', flush=True)  # Clear line
            print(indentation_str + bunched_body, flush=True, end='')
            time.sleep(delay)
        
        # Clear the line and start a new one for the next cycle
        print('\r' + ' ' * _width + '\r', end='', flush=True)
        print()  # Move to next line
        
        cycle_count += 1
        if max_cycles and cycle_count >= max_cycles:
            return


def connected_pipes(width=None, delay=0.2, gap_probability=0.96, vertical_style_factor=1.0, max_rows=None):
    """Network of connected pipes using Unicode box-drawing characters."""
    
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
    
    # Unicode box-drawing characters
    UP_DOWN_CHAR         = chr(9474)  # '│'
    LEFT_RIGHT_CHAR      = chr(9472)  # '─'
    DOWN_RIGHT_CHAR      = chr(9484)  # '┌'
    DOWN_LEFT_CHAR       = chr(9488)  # '┐'
    UP_RIGHT_CHAR        = chr(9492)  # '└'
    UP_LEFT_CHAR         = chr(9496)  # '┘'
    UP_DOWN_RIGHT_CHAR   = chr(9500)  # '├'
    UP_DOWN_LEFT_CHAR    = chr(9508)  # '┤'
    DOWN_LEFT_RIGHT_CHAR = chr(9516)  # '┬'
    UP_LEFT_RIGHT_CHAR   = chr(9524)  # '┴'
    CROSS_CHAR           = chr(9532)  # '┼'
    EMPTY = ' '

    # Initialize the previous row with up-left-right characters
    prev_row = [UP_LEFT_RIGHT_CHAR] * _width
    row_count = 0
    
    while True:
        row = []  # Characters to print in this row
        
        for i, prev_char in enumerate(prev_row):
            # Figure out if we need to connect the left side
            if i == 0:
                left_connect = False
            else:
                if row[i - 1] in (LEFT_RIGHT_CHAR, DOWN_RIGHT_CHAR, UP_RIGHT_CHAR, 
                                UP_DOWN_RIGHT_CHAR, DOWN_LEFT_RIGHT_CHAR, UP_LEFT_RIGHT_CHAR, CROSS_CHAR):
                    left_connect = True
                else:
                    left_connect = False

            # Figure out if we need to connect the up side
            if prev_char in (UP_DOWN_CHAR, DOWN_RIGHT_CHAR, DOWN_LEFT_CHAR, 
                           UP_DOWN_RIGHT_CHAR, UP_DOWN_LEFT_CHAR, DOWN_LEFT_RIGHT_CHAR, CROSS_CHAR):
                up_connect = True
            else:
                up_connect = False

            # The downward and right side connections are random
            down_connect = random.choice((True, False))
            if random.random() < gap_probability:
                down_connect = False

            if i == _width - 1:
                # Make the rightmost column never connect off the right edge
                right_connect = False
                # Additional check so that we don't make the pipe go off the right edge
                shape = (up_connect, down_connect, left_connect, right_connect)
                if shape == (False, False, True, False):
                    # Make this a left-down pipe
                    down_connect = True
                elif shape == (False, True, False, False):
                    # Make this an empty space
                    down_connect = False
                elif shape == (True, False, False, False):
                    # Make this an up-down pipe
                    down_connect = True
            else:
                right_connect = random.choice((True, False))
                if random.random() < gap_probability:
                    right_connect = False

            # Override right_connect value if vertical_style_factor is greater than 0.0
            if random.random() < vertical_style_factor:
                right_connect = False

            # Get the character to print based on the connections to the four sides
            shape = (up_connect, down_connect, left_connect, right_connect)
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
                (False, True, False, False):  DOWN_RIGHT_CHAR,
                (False, False, True, True):   LEFT_RIGHT_CHAR,
                (False, False, True, False):  random.choice((DOWN_LEFT_RIGHT_CHAR, DOWN_LEFT_CHAR, LEFT_RIGHT_CHAR)),
                (False, False, False, True):  DOWN_RIGHT_CHAR,
                (False, False, False, False): EMPTY,
            }[shape]
            
            row.append(char)
        
        print(''.join(row))
        prev_row = row
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
        time.sleep(delay)


def diagonal_sweep(width=None, delay=0.002, empty_char=' ', sweep_char='@', max_rows=None):
    """Diagonal sweep pattern that alternates between drawing and erasing across columns."""
    
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
    
    pos = 0
    columns = [empty_char] * _width
    sweep_on = True
    row_count = 0
    
    while True:
        if sweep_on:
            columns[pos] = sweep_char
        else:
            columns[pos] = empty_char

        pos += 1
        if pos >= _width:
            pos = 0
            sweep_on = not sweep_on

        print(''.join(columns))
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
        time.sleep(delay)


def earthworm_tunnels(width=None, delay=0.02, empty_char=' ', dirt_chars='\\/', worm_char=' ', grow_back_in=30, num_worms=8, max_move=4, max_rows=None):
    # TODO Needs correction
    """
    Simulates worms tunneling through dirt with regrowth mechanics
    """
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
    
    # Initialize the dirt field
    dirt_field = []
    dirt_timers = []
    worms = []
    
    # Initialize worm positions
    for _ in range(num_worms):
        x = random.randint(0, _width - 1)
        y = random.randint(0, 20)
        worms.append([x, y])

    row_count = 0
    while True:
        # Add new rows of dirt if needed
        while len(dirt_field) <= max(worm[1] for worm in worms) + 20:
            new_row = []
            new_timer_row = []
            for x in range(_width):
                new_row.append(random.choice(dirt_chars))
                new_timer_row.append(0)
            dirt_field.append(new_row)
            dirt_timers.append(new_timer_row)
        
        # Move worms
        for worm in worms:
            # Clear current position
            if 0 <= worm[1] < len(dirt_field) and 0 <= worm[0] < _width:
                dirt_field[worm[1]][worm[0]] = worm_char
                dirt_timers[worm[1]][worm[0]] = grow_back_in
            
            # Move worm randomly
            dx = random.randint(-max_move, max_move)
            dy = random.randint(-1, max_move)
            
            worm[0] = max(0, min(_width - 1, worm[0] + dx))
            worm[1] = max(0, worm[1] + dy)
        
        # Update dirt regrowth timers
        for y in range(len(dirt_field)):
            for x in range(_width):
                if dirt_timers[y][x] > 0:
                    dirt_timers[y][x] -= 1
                    if dirt_timers[y][x] == 0:
                        dirt_field[y][x] = random.choice(dirt_chars)
        
        # Print current state (scroll up)
        if len(dirt_field) > 0:
            print(''.join(dirt_field[0]))
            dirt_field.pop(0)
            dirt_timers.pop(0)
            
            # Adjust worm positions
            for worm in worms:
                worm[1] = max(0, worm[1] - 1)
            
            row_count += 1
            if max_rows and row_count >= max_rows:
                return
        
        time.sleep(delay)


def towers_and_towers(width=None, delay=0.0075, after_tower_delay=0.75, wipe_after=8, max_rows=None):
    """
    Animated tower construction with overlapping structures that build up and get wiped
    """
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
    
    EMPTY_CHAR = ' '
    CORNER_CHAR = '+'
    TOP_CHAR = '-'
    SIDE_CHAR = '|'
    INTERIOR_CHARS = ':|. '
    
    MIN_TOWER_WIDTH = 8
    MAX_TOWER_WIDTH = 20
    
    MIN_TOWER_HEIGHT = 4
    MAX_TOWER_HEIGHT = 17
    
    TOWER_HEIGHT_MAX_DIFF = 8

    step = 1
    columns = [EMPTY_CHAR] * _width
    row_count = 0
    
    while True:
        if step % wipe_after == 0:
            for i in range(60):
                print()
                row_count += 1
                if max_rows and row_count >= max_rows:
                    return
                time.sleep(delay)
            time.sleep(after_tower_delay)
            columns = [EMPTY_CHAR] * _width
        
        # Tower 1 top (tower 1 is slightly higher than tower 2):
        tower1_left = random.randint(0, max(0, (_width // 2) - MAX_TOWER_WIDTH))
        tower1_width = random.randint(MIN_TOWER_WIDTH, min(MAX_TOWER_WIDTH, _width - tower1_left - 1))
        
        if tower1_left + tower1_width < _width:
            columns[tower1_left] = CORNER_CHAR
            columns[tower1_left + tower1_width] = CORNER_CHAR
            for i in range(tower1_left + 1, tower1_left + tower1_width):
                if i < _width:
                    columns[i] = TOP_CHAR
        
        print(''.join(columns))
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
        time.sleep(delay)
        
        # Tower 1 top body that is above tower 2's top:
        if tower1_left < _width:
            columns[tower1_left] = SIDE_CHAR
        if tower1_left + tower1_width < _width:
            columns[tower1_left + tower1_width] = SIDE_CHAR
        
        interior_char = INTERIOR_CHARS[step % len(INTERIOR_CHARS)]
        for i in range(tower1_left + 1, tower1_left + tower1_width):
            if i < _width:
                columns[i] = interior_char
        
        for i in range(random.randint(1, TOWER_HEIGHT_MAX_DIFF)):
            print(''.join(columns))
            row_count += 1
            if max_rows and row_count >= max_rows:
                return
            time.sleep(delay)
        
        # Tower 2 top:
        tower2_left = random.randint(0, max(0, _width - MAX_TOWER_WIDTH))
        tower2_width = random.randint(MIN_TOWER_WIDTH, min(MAX_TOWER_WIDTH, _width - tower2_left - 1))
        
        if tower2_left + tower2_width < _width:
            columns[tower2_left] = CORNER_CHAR
            columns[tower2_left + tower2_width] = CORNER_CHAR
            for i in range(tower2_left + 1, tower2_left + tower2_width):
                if i < _width:
                    columns[i] = TOP_CHAR
        
        print(''.join(columns))
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
        time.sleep(delay)
        
        # Tower 2 body (and 1):
        if tower2_left < _width:
            columns[tower2_left] = SIDE_CHAR
        if tower2_left + tower2_width < _width:
            columns[tower2_left + tower2_width] = SIDE_CHAR
        
        interior_char = INTERIOR_CHARS[step % len(INTERIOR_CHARS)]
        for i in range(tower2_left + 1, tower2_left + tower2_width):
            if i < _width:
                columns[i] = interior_char
        
        for i in range(random.randint(MIN_TOWER_HEIGHT, MAX_TOWER_HEIGHT)):
            print(''.join(columns))
            row_count += 1
            if max_rows and row_count >= max_rows:
                return
            time.sleep(delay)
        
        time.sleep(after_tower_delay)
        step += 1



def any_size_diagonal_maze(width=None, delay=0.1, maze_size=4, max_rows=None):
    """
    Creates a diagonal maze pattern with random forward and back slashes
    """
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
    
    EMPTY = ' '
    FORWARD_SLASH = chr(9585)  # ╱
    BACK_SLASH = chr(9586)     # ╲
    
    columns = [FORWARD_SLASH] * (_width // maze_size)
    row_count = 0
    
    while True:
        # Set up the slashes in columns:
        for i in range(len(columns)):
            if random.randint(0, 1) == 0:
                columns[i] = FORWARD_SLASH
            else:
                columns[i] = BACK_SLASH
        
        # Print the columns:
        for row_num in range(maze_size):
            line = []
            for i in range(len(columns)):
                if columns[i] == FORWARD_SLASH:
                    line.append(EMPTY * (maze_size - row_num - 1) + FORWARD_SLASH + EMPTY * (row_num))
                elif columns[i] == BACK_SLASH:
                    line.append(EMPTY * (row_num) + BACK_SLASH + EMPTY * (maze_size - row_num - 1))
            
            print(''.join(line))
            row_count += 1
            if max_rows and row_count >= max_rows:
                return
            time.sleep(delay)


def thorns(width=None, delay=0.005, thorn_char='-', max_rows=None):
    """
    Creates random length thorn lines centered on the screen
    """
    
    LEVELS = [1, 1, 1, 1, 1, 1, 1, 3, 6]
    MULTIPLIER = 10
    
    row_count = 0
    
    while True:
        if width is None:
            _width = shutil.get_terminal_size()[0]
        else:
            _width = width
        if sys.platform == 'win32':
            _width -= 1  # Windows terminals insert a newline if something is printed in the last column

        line_length = int(random.choice(LEVELS) * ((random.random() + 1) * MULTIPLIER))
        line = thorn_char * line_length
        
        if len(line) > _width:
            line = thorn_char * _width
        
        print(line.center(_width))
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
        time.sleep(delay)


def triangle_hall(width=None, delay=0.008, empty_char=' ', strut_char='#', max_rows=None):
    """
    Animated strut points that create triangular patterns by moving left and right
    """
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
    
    strut_points = [(0, True)]  # list of (position, going_right_bool)
    next_strut_point_at = random.randint(1, _width // 2)
    row_count = 0
    
    while True:
        row = [empty_char] * _width
        
        # There's a buggy case where somehow strut_points can end up empty. Let's just restart it then:
        if len(strut_points) == 0:
            strut_points = [(0, True)]  # list of (position, going_right_bool)
            next_strut_point_at = random.randint(1, _width // 2)
        
        # Add a new strut point if it is time
        if strut_points[-1][0] == next_strut_point_at:
            strut_points.append((next_strut_point_at, not strut_points[-1][1]))
            
            if strut_points[-1][1]:
                # next next_strut_point_at between here and right edge
                if (_width - 1) - next_strut_point_at > (_width // 2):
                    # The distance to the right edge is too far, so let's do somewhere closer
                    next_strut_point_at = random.randint(next_strut_point_at, (_width - 1 - next_strut_point_at) // 2 + next_strut_point_at)
                else:
                    next_strut_point_at = random.randint(next_strut_point_at, _width - 1)
            else:
                # next next_strut_point_at between here and left edge
                if next_strut_point_at - 0 > (_width // 2):
                    # the distance to the left edge is too far, so let's do somewhere closer
                    next_strut_point_at = random.randint(next_strut_point_at // 2, next_strut_point_at)
                else:
                    next_strut_point_at = random.randint(0, next_strut_point_at)
        
        # Create the row characters
        delete_indexes = []
        for i, (pos, going_right) in enumerate(strut_points):
            if 0 <= pos < _width:
                row[pos] = strut_char
            
            # Move strut points (or mark them for deletion)
            if pos == _width - 1 and going_right:
                delete_indexes.append(i)
            elif pos == 0 and not going_right:
                delete_indexes.append(i)
            elif going_right:
                strut_points[i] = (pos + 1, True)
            elif not going_right:
                strut_points[i] = (pos - 1, False)
        
        # Remove strut points that have gone off the sides:
        for i in range(len(delete_indexes) - 1, -1, -1):
            del strut_points[delete_indexes[i]]
        
        print(''.join(row))
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
        time.sleep(delay)


def vertical_struts(width=None, delay=0.01, min_vertical_span=10, max_vertical_span=30, 
                   empty_char=' ', strut_char='#', max_rows=None):
    """
    Creates vertical struts with horizontal crossbeams at random positions
    """
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
    
    row_count = 0
    
    while True:
        col = random.randint(0, _width - 1)
        row = [empty_char] * _width
        row[col] = strut_char
        
        row_str = ''.join(row)
        span = random.randint(min_vertical_span, max_vertical_span)
        
        for i in range(span):
            print(row_str)
            row_count += 1
            if max_rows and row_count >= max_rows:
                return
            time.sleep(delay)
        
        # Print horizontal line:
        print(strut_char * _width)
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
        time.sleep(delay)


def hex_portals(width=None, delay=0.1, empty_chars='/\\_    ', density=0.0025, 
               interior_chars='.                   ', interior_density=1.0, 
               min_size=4, max_size=10, max_rows=None):
    """
    Creates hexagonal portals with optional interior patterns scrolling down the screen
    """
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column

    next_rows = []
    row_count = 0
    
    while True:
        # Make sure there are enough rows in `next_rows`:
        for i in range((max_size * 2 + 2) - len(next_rows)):
            next_rows.append([random.choice(empty_chars) for i in range(_width)])
        
        for pos in range(0, _width - (max_size * 4 + 1)):
            if random.random() >= density:
                # Don't create a hexagon here.
                continue
            
            size = random.randint(min_size, max_size)
            
            # Draw new hexagon to next_rows:
            for i in range(pos + 1 + size, pos + 1 + size + (2 * size + 1)):
                if i < _width:
                    next_rows[0][i] = '_'  # Top row of underscores
                    if size * 2 < len(next_rows) and i < _width:
                        next_rows[size * 2][i] = '_'  # Bottom row of underscores
            
            for i in range(size):
                # Top left slashes
                if (size - i < len(next_rows) and 
                    pos + 1 + i < _width):
                    next_rows[size - i][pos + 1 + i] = '/'
                
                # Bottom left slashes
                if (size + 1 + i < len(next_rows) and 
                    pos + 1 + i < _width):
                    next_rows[size + 1 + i][pos + 1 + i] = '\\'
                
                # Top right slashes
                right_pos = pos + 1 + (size * 3) + 1 + (size - i - 1)
                if (size - i < len(next_rows) and right_pos < _width):
                    next_rows[size - i][right_pos] = '\\'
                
                # Bottom right slashes
                if (size + 1 + i < len(next_rows) and right_pos < _width):
                    next_rows[size + 1 + i][right_pos] = '/'
            
            if interior_chars:
                # Draw interior characters on inside of hexagon
                for i in range(1, size + 1):
                    for j in range(size - i + 2, size * 3 + 1 + i):
                        if pos + j < _width:
                            if random.random() < interior_density:
                                if i < len(next_rows):
                                    next_rows[i][pos + j] = random.choice(interior_chars)
                            if (random.random() < interior_density and i != 1 and 
                                size * 2 - i + 1 < len(next_rows)):
                                next_rows[size * 2 - i + 1][pos + j] = random.choice(interior_chars)
        
        # Display the next rows:
        print(''.join(next_rows[0]))
        del next_rows[0]
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
        time.sleep(delay)



def toggler1(width=None, delay=0.05, toggler_density=10, right_increment=1, 
            char1='.', char2='@', max_rows=None):
    """
    Moving togglers that flip characters between two states as they travel
    """
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
    
    LEFT_INCREMENT = right_increment * -1
    
    togglers = []  # List of [x position, direction moving]
    row_count = 0
    
    while True:
        if width is None:
            _width = shutil.get_terminal_size()[0]
        else:
            _width = width
        if sys.platform == 'win32':
            _width -= 1  # Windows terminals insert a newline if something is printed in the last column

        columnChars = [char1] * _width

        # Adjust columnChars length if width changed
        if len(columnChars) != _width:
            if len(columnChars) < _width:
                columnChars.extend([char1] * (_width - len(columnChars)))
            else:
                columnChars = columnChars[:_width]
        
        if random.randint(0, 99) < toggler_density:
            # Add a new toggler
            togglers.append([random.randint(0, _width - 1), random.choice((LEFT_INCREMENT, right_increment))])
        
        # Remove out of bounds togglers:
        for i in range(len(togglers) - 1, -1, -1):
            if togglers[i][0] < 0 or togglers[i][0] >= _width:
                del togglers[i]
        
        # Move the togglers and toggle the column chars:
        for i in range(len(togglers)):
            togglerPosition = togglers[i][0]
            togglerDirection = togglers[i][1]
            
            if 0 <= togglerPosition < len(columnChars):
                if columnChars[togglerPosition] == char1:
                    columnChars[togglerPosition] = char2
                else:
                    columnChars[togglerPosition] = char1
            
            togglers[i][0] += togglerDirection  # move the toggler
        
        print(''.join(columnChars))
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
        time.sleep(delay)


def toggler2(width=None, delay=0.05, toggler_density=10, right_increment=3, 
            char1='.', char2='@', max_rows=None):
    """
    Paired togglers that create triangular wave patterns by moving in opposite directions
    """
    
    LEFT_INCREMENT = right_increment * -1

    togglers = []  # List of [x position, direction moving]
    row_count = 0
    
    while True:
        if width is None:
            _width = shutil.get_terminal_size()[0]
        else:
            _width = width
        if sys.platform == 'win32':
            _width -= 1  # Windows terminals insert a newline if something is printed in the last column

        columnChars = [char1] * _width
        
        # Adjust columnChars length if width changed
        if len(columnChars) != _width:
            if len(columnChars) < _width:
                columnChars.extend([char1] * (_width - len(columnChars)))
            else:
                columnChars = columnChars[:_width]
        
        if random.randint(0, 99) < toggler_density:
            # Add two new togglers
            position = random.randint(right_increment, _width - right_increment)
            togglers.append([position - right_increment, LEFT_INCREMENT])
            togglers.append([position, right_increment])
        
        # Remove out of bounds togglers:
        for i in range(len(togglers) - 1, -1, -1):
            if togglers[i][0] < 0 or togglers[i][0] >= _width:
                del togglers[i]
        
        # Move the togglers and toggle the column chars:
        for i in range(len(togglers)):
            togglerPosition = togglers[i][0]
            togglerDirection = togglers[i][1]
            
            if 0 <= togglerPosition < len(columnChars):
                if columnChars[togglerPosition] == char1:
                    columnChars[togglerPosition] = char2
                else:
                    columnChars[togglerPosition] = char1
            
            togglers[i][0] += togglerDirection  # move the toggler
        
        print(''.join(columnChars))
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
        time.sleep(delay)


def tri_grid_scaffold(width=None, delay=0.1, change_amount=4, max_rows=None):
    """
    Creates a triangular grid scaffolding pattern with varying density
    """
    
    density = 0
    changeAmt = change_amount
    row_count = 0
    
    while True:
        if width is None:
            _width = shutil.get_terminal_size()[0]
        else:
            _width = width
        if sys.platform == 'win32':
            _width -= 1  # Windows terminals insert a newline if something is printed in the last column

        triangleWidth = (_width - 2) // 4
        
        # Increase/decrease the density of triangles, until you
        # reach 0 or 100, then reverse the direction of density change:
        density += changeAmt
        if density <= 0 or density >= 100:
            changeAmt *= -1
        
        for j in range(2):
            # On j == 0, handle the two rows of begins-with-rightside-up-triangles:
            #  /\  /\  /\
            # /__\/__\/__\
            if j == 0:
                row1 = []
                row2 = []
            # On j == 1, handle the two rows of begins-with-upside-down-triangles:
            # \  /\  /
            # _\/__\/_
            elif j == 1:
                row1 = ['\\ ']
                row2 = ['_\\']
            
            for i in range(triangleWidth):
                if random.randint(0, 99) < density:
                    row1.append(' /')
                    row2.append('/')
                else:
                    row1.append('  ')
                    row2.append(' ')
                
                if random.randint(0, 99) < density:
                    row2.append('__')
                else:
                    row2.append('  ')
                
                if random.randint(0, 99) < density:
                    row1.append('\\ ')
                    row2.append('\\')
                else:
                    row1.append('  ')
                    row2.append(' ')
            
            print(''.join(row1))
            row_count += 1
            if max_rows and row_count >= max_rows:
                return
            time.sleep(delay)
            
            print(''.join(row2))
            row_count += 1
            if max_rows and row_count >= max_rows:
                return
            time.sleep(delay)


def orbital_travels(width=None, delay=0.05, empty_char=' ', 
                   chars='@O0o*.,vV', min_orbiters=7, max_orbiters=15, max_rows=None):
    """
    Multiple characters orbiting in sine wave patterns at different speeds
    """
    
    # Initialize orbital characters
    orbital_chars = []
    sine_step_incs = []
    sine_steps = []
    
    for i in range(random.randint(min_orbiters, max_orbiters)):
        orbital_chars.append(random.choice(chars))
        sine_step_incs.append(random.random() * 0.1 + 0.0001)
        sine_steps.append(random.random() * math.pi)
    
    row_count = 0
    
    while True:
        if width is None:
            _width = shutil.get_terminal_size()[0]
        else:
            _width = width
        if sys.platform == 'win32':
            _width -= 1  # Windows terminals insert a newline if something is printed in the last column

        row = [empty_char] * _width
        
        for i in range(len(orbital_chars)):
            # Calculate position using sine wave (0 to width-1)
            position = int((math.sin(sine_steps[i]) + 1) / 2 * (_width - 1))
            if 0 <= position < _width:
                row[position] = orbital_chars[i]
            sine_steps[i] += sine_step_incs[i]
        
        print(''.join(row))
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
        time.sleep(delay)
    

def snail_trail(width=None, min_trail_len=5, trail_char='_', snail_chars='@V', 
               trail_time=0.9, min_spacing=1, max_spacing=6, max_rows=None):
    """
    Animated snails that leave trails as they crawl across the screen
    """
    
    row_count = 0
    
    while True:
        if width is None:
            _width = shutil.get_terminal_size()[0]
        else:
            _width = width
        if sys.platform == 'win32':
            _width -= 1  # Windows terminals insert a newline if something is printed in the last column

        trail_length = random.randint(min_trail_len, _width - 2)
        
        # Animate the snail crawling and building its trail
        for i in range(trail_length):
            trail = trail_char * i + snail_chars
            print(trail, end='', flush=True)
            time.sleep(trail_time / trail_length)
            # Backspace to clear the line
            print('\b' * len(trail), end='', flush=True)
        
        # Final position with complete trail
        final_trail = trail_char * trail_length + snail_chars
        print(final_trail, end='', flush=True)
        
        # Add random vertical spacing
        spacing = random.randint(min_spacing, max_spacing)
        print('\n' * spacing)
        
        row_count += spacing + 1  # +1 for the snail trail row
        if max_rows and row_count >= max_rows:
            return


def password_cracker(width=None, delay=0.01, max_rows=None, one_line=False):
    """
    Matrix-style password cracking animation that gradually reveals a hidden message
    """
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
    
    # The hidden message to reveal
    message = "The sky above the port was the color of television, tuned to a dead channel."
    
    # Ensure the message fits within terminal width
    if len(message) > _width:
        message = message[:_width-3] + "..."
    
    # Characters to use for random substitution
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
    
    # Create initial random string and track revealed positions
    current = list(''.join(random.choice(chars) for _ in range(len(message))))
    revealed = [False] * len(message)  # Track which characters have been revealed
    positions_to_reveal = list(range(len(message)))  # List of positions to reveal
    random.shuffle(positions_to_reveal)  # Randomize the order
    
    row_count = 0
    
    # Gradually reveal the message in random order
    for reveal_count in range(len(message)):        
        # Randomly change characters that haven't been revealed yet
        for _ in range(3):  # Multiple passes for more dynamic effect
            display_str = list(current)
            for j in range(len(message)):
                if not revealed[j] and random.random() < 0.7:  # 70% chance to change each unrevealed char
                    display_str[j] = random.choice(chars)
            
            print(''.join(display_str), end='\r' if one_line else '\n', flush=True)
            time.sleep(delay)
        
        # Reveal the next character at a random position
        pos_to_reveal = positions_to_reveal[reveal_count]
        revealed[pos_to_reveal] = True
        current[pos_to_reveal] = message[pos_to_reveal]
        
        print(''.join(current), end='\r' if one_line else '\n', flush=True)
        time.sleep(delay * 2)  # Pause longer when revealing
        
        row_count += 1
        if max_rows and row_count >= max_rows:
            print()  # Final newline
            return
    
    # Final reveal
    print(message, flush=True)
    print()  # Add final newline


def dna(delay=0.1, max_rows=None):
    """
    Animated DNA double helix structure
    """
    dna_rows = [
        '    #C-G#',
        '   #C---G#',
        '  #A-----T#',
        ' #T------A#',
        '#A------T#',
        '#G-----C#',
        ' #C---G#',
        ' #G-C#',
        '  ##',
        ' #G-C#',
        ' #G---C#',
        '#A-----T#',
        '#A------T#',
        ' #A------T#',
        '  #C-----G#',
        '   #C---G#',
        '    #G-C#',
        '     ##',
    ]
    
    row_count = 0
    
    while True:  # Main program loop
        for row in dna_rows:
            print(row)
            time.sleep(delay)
            
            row_count += 1
            if max_rows and row_count >= max_rows:
                return


def spike(delay=0.1, width=None, spike_char='-', max_rows=None):
    """
    Growing and shrinking spike pattern using terminal width
    """
    row_count = 0
    
    while True:
        if width is None:
            _width = shutil.get_terminal_size()[0]
        else:
            _width = width
        if sys.platform == 'win32':
            _width -= 1  # Windows terminals insert a newline if something is printed in the last column

        max_spike_length = int(math.sqrt(_width))
        
        # Growing phase
        for i in range(1, max_spike_length + 1):
            print(spike_char * (i * i))
            time.sleep(delay)
            
            row_count += 1
            if max_rows and row_count >= max_rows:
                return
        
        # Shrinking phase
        for i in range(max_spike_length, 0, -1):
            print(spike_char * (i * i))
            time.sleep(delay)
            
            row_count += 1
            if max_rows and row_count >= max_rows:
                return


def zigzag(delay=0.05, zig_steps=20, pattern='********', width=None, max_rows=None):
    """
    Simple zig zag animation that bounces left and right
    """
    indent_size = 0  # How many spaces to indent
    row_count = 0
    
    while True:  # The main program loop
        # Get current terminal width to prevent overflow
        if width is None:
            _width = shutil.get_terminal_size()[0]
        else:
            _width = width
        if sys.platform == 'win32':
            _width -= 1  # Windows terminals insert a newline if something is printed in the last column

        max_indent = max(0, _width - len(pattern))
        
        # Zig to the right
        for i in range(min(zig_steps, max_indent)):
            indent_size = indent_size + 1
            indentation = ' ' * indent_size
            print(indentation + pattern)
            time.sleep(delay)
            
            row_count += 1
            if max_rows and row_count >= max_rows:
                return
        
        # Zag to the left  
        for i in range(min(zig_steps, max_indent)):
            indent_size = indent_size - 1
            indentation = ' ' * indent_size
            print(indentation + pattern)
            time.sleep(delay)
            
            row_count += 1
            if max_rows and row_count >= max_rows:
                return


def diamond_sky(delay=0.1, width=None, min_diamond_size=1, max_diamond_size=8, 
                chance_for_filled=0.3, diamonds_per_row=2, max_rows=None):
    """
    Falling diamonds of various sizes with random patterns
    """
    empty_chars = '                ...,'  # Characters for background
    
    def get_outline_diamond(size):
        """Create an outlined diamond pattern"""
        assert size > 0
        rows = []
        # Make the top half of the diamond
        for i in range(size):
            rows.append(([None] * (size - i - 1)) + ['/'] + ([' '] * (i * 2)) + ['\\'])
        # Make the bottom half of the diamond
        for i in range(size):
            rows.append(([None] * i) + ['\\'] + ([' '] * ((size - i - 1) * 2)) + ['/'])
        return rows
    
    def get_filled_diamond(size):
        """Create a filled diamond pattern"""
        assert size > 0
        rows = []
        # Make the top half of the diamond
        for i in range(size):
            rows.append(([None] * (size - i - 1)) + (['/'] * (i + 1)) + (['\\'] * (i + 1)))
        # Make the bottom half of the diamond
        for i in range(size):
            rows.append(([None] * i) + (['\\'] * (size - i)) + (['/'] * (size - i)))
        return rows
    
    next_rows = []
    row_count = 0
    
    while True:
        if width is None:
            _width = shutil.get_terminal_size()[0]
        else:
            _width = width
        if sys.platform == 'win32':
            _width -= 1  # Windows terminals insert a newline if something is printed in the last column

        # Generate diamonds for this iteration
        for j in range(diamonds_per_row):
            size = random.randint(min_diamond_size, max_diamond_size)
            
            if random.random() < chance_for_filled:
                diamond = get_filled_diamond(size)
            else:
                diamond = get_outline_diamond(size)
            
            x_start = random.randint(0, max(0, _width - 1 - (size * 2)))
            
            # Make sure there are enough rows in next_rows
            while len(next_rows) < size * 2:
                next_rows.append([random.choice(empty_chars) for i in range(_width)])
            
            # Add the diamond to next_rows
            for y, row in enumerate(diamond):
                for x, char in enumerate(row):
                    if char is None:
                        continue  # Skip None characters (transparent spaces)
                    if x + x_start < _width:
                        next_rows[y][x + x_start] = char
        
        # Print the row and then remove it
        if next_rows:
            print(''.join(next_rows[0]))
            del next_rows[0]
            time.sleep(delay)
            
            row_count += 1
            if max_rows and row_count >= max_rows:
                return


class Duckling:
    """A duckling with random body features for the ducklings screensaver."""
    
    def __init__(self):
        """Create a new duckling with random body features."""
        # Constants for duckling features
        LEFT = 'left'
        RIGHT = 'right'
        BEADY = 'beady'
        WIDE = 'wide'
        HAPPY = 'happy'
        ALOOF = 'aloof'
        CHUBBY = 'chubby'
        VERY_CHUBBY = 'very chubby'
        OPEN = 'open'
        CLOSED = 'closed'
        OUT = 'out'
        DOWN = 'down'
        UP = 'up'
        HEAD = 'head'
        BODY = 'body'
        FEET = 'feet'
        
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])
        
        if self.body == CHUBBY:
            # Chubby ducklings can only have beady eyes
            self.eyes = BEADY
        else:
            self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])
        
        self.part_to_display_next = HEAD
    
    def get_head_str(self):
        """Returns the string of the duckling's head."""
        LEFT = 'left'
        RIGHT = 'right'
        BEADY = 'beady'
        WIDE = 'wide'
        HAPPY = 'happy'
        ALOOF = 'aloof'
        CHUBBY = 'chubby'
        VERY_CHUBBY = 'very chubby'
        OPEN = 'open'
        CLOSED = 'closed'
        
        head_str = ''
        if self.direction == LEFT:
            # Get the mouth
            if self.mouth == OPEN:
                head_str += '>'
            elif self.mouth == CLOSED:
                head_str += '='
            
            # Get the eyes
            if self.eyes == BEADY and self.body == CHUBBY:
                head_str += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                head_str += '" '
            elif self.eyes == WIDE:
                head_str += "''"
            elif self.eyes == HAPPY:
                head_str += '^^'
            elif self.eyes == ALOOF:
                head_str += '``'
            
            head_str += ') '  # Get the back of the head
        
        if self.direction == RIGHT:
            head_str += ' ('  # Get the back of the head
            
            # Get the eyes
            if self.eyes == BEADY and self.body == CHUBBY:
                head_str += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                head_str += ' "'
            elif self.eyes == WIDE:
                head_str += "''"
            elif self.eyes == HAPPY:
                head_str += '^^'
            elif self.eyes == ALOOF:
                head_str += '``'
            
            # Get the mouth
            if self.mouth == OPEN:
                head_str += '<'
            elif self.mouth == CLOSED:
                head_str += '='
        
        if self.body == CHUBBY:
            # Get an extra space so chubby ducklings are the same
            # width as very chubby ducklings
            head_str += ' '
        
        return head_str
    
    def get_body_str(self):
        """Returns the string of the duckling's body."""
        LEFT = 'left'
        RIGHT = 'right'
        CHUBBY = 'chubby'
        VERY_CHUBBY = 'very chubby'
        OUT = 'out'
        DOWN = 'down'
        UP = 'up'
        
        body_str = '('  # Get the left side of the body
        if self.direction == LEFT:
            # Get the interior body space
            if self.body == CHUBBY:
                body_str += ' '
            elif self.body == VERY_CHUBBY:
                body_str += '  '
            
            # Get the wing
            if self.wing == OUT:
                body_str += '>'
            elif self.wing == UP:
                body_str += '^'
            elif self.wing == DOWN:
                body_str += 'v'
        
        if self.direction == RIGHT:
            # Get the wing
            if self.wing == OUT:
                body_str += '<'
            elif self.wing == UP:
                body_str += '^'
            elif self.wing == DOWN:
                body_str += 'v'
            
            # Get the interior body space
            if self.body == CHUBBY:
                body_str += ' '
            elif self.body == VERY_CHUBBY:
                body_str += '  '
        
        body_str += ')'  # Get the right side of the body
        
        if self.body == CHUBBY:
            # Get an extra space so chubby ducklings are the same
            # width as very chubby ducklings
            body_str += ' '
        
        return body_str
    
    def get_feet_str(self):
        """Returns the string of the duckling's feet."""
        CHUBBY = 'chubby'
        VERY_CHUBBY = 'very chubby'
        
        if self.body == CHUBBY:
            return ' ^^  '
        elif self.body == VERY_CHUBBY:
            return ' ^ ^ '
    
    def get_next_body_part(self):
        """Calls the appropriate display method for the next body
        part that needs to be displayed. Sets part_to_display_next to
        None when finished."""
        HEAD = 'head'
        BODY = 'body'
        FEET = 'feet'
        
        if self.part_to_display_next == HEAD:
            self.part_to_display_next = BODY
            return self.get_head_str()
        elif self.part_to_display_next == BODY:
            self.part_to_display_next = FEET
            return self.get_body_str()
        elif self.part_to_display_next == FEET:
            self.part_to_display_next = None
            return self.get_feet_str()


def ducklings(pause=0.2, density=0.10, width=None, max_rows=None):
    """
    Screensaver of many adorable ducklings
    """
    DUCKLING_WIDTH = 5
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
    
    duckling_lanes = [None] * (_width // DUCKLING_WIDTH)
    row_count = 0
    
    while True:  # Main program loop
        for lane_num, duckling_obj in enumerate(duckling_lanes):
            # See if we should create a duckling in this lane
            if (duckling_obj is None and random.random() <= density):
                # Place a duckling in this lane
                duckling_obj = Duckling()
                duckling_lanes[lane_num] = duckling_obj
            
            if duckling_obj is not None:
                # Draw a duckling if there is one in this lane
                print(duckling_obj.get_next_body_part(), end='')
                # Delete the duckling if we've finished drawing it
                if duckling_obj.part_to_display_next is None:
                    duckling_lanes[lane_num] = None
            else:
                # Draw five spaces since there is no duckling here
                print(' ' * DUCKLING_WIDTH, end='')
        
        print()  # Print a newline
        sys.stdout.flush()  # Make sure text appears on the screen
        time.sleep(pause)
        
        row_count += 1
        if max_rows and row_count >= max_rows:
            return


def full_of_squares(delay=0.1, width=None, min_square_size=1, max_square_size=7,
                   chance_of_filled=0.0, squares_per_row=3, max_rows=None):
    """
    Falling squares using Unicode box-drawing characters
    """
    
    # Unicode box-drawing characters
    UP_DOWN_CHAR = chr(9474)         # '│'
    LEFT_RIGHT_CHAR = chr(9472)      # '─'
    DOWN_RIGHT_CHAR = chr(9484)      # '┌'
    DOWN_LEFT_CHAR = chr(9488)       # '┐'
    UP_RIGHT_CHAR = chr(9492)        # '└'
    UP_LEFT_CHAR = chr(9496)         # '┘'
    UP_DOWN_RIGHT_CHAR = chr(9500)   # '├'
    UP_DOWN_LEFT_CHAR = chr(9508)    # '┤'
    DOWN_LEFT_RIGHT_CHAR = chr(9516) # '┬'
    UP_LEFT_RIGHT_CHAR = chr(9524)   # '┴'
    CROSS_CHAR = chr(9532)           # '┼'
    
    # Characters for background and interior
    empty_chars = ' ' * 25 + '...,' + chr(9633)
    square_interior = ' '
    
    def get_outline_square(size):
        """Create an outlined square using box-drawing characters"""
        assert size >= 0
        
        rows = []
        # Make the top row of the square
        rows.append(DOWN_RIGHT_CHAR + (LEFT_RIGHT_CHAR * (size * 2)) + DOWN_LEFT_CHAR)
        
        # Make the middle segment of the square
        for i in range(size):
            rows.append(UP_DOWN_CHAR + (''.join([random.choice(square_interior) for j in range((size * 2))])) + UP_DOWN_CHAR)
        
        # Make the bottom row of the square
        rows.append(UP_RIGHT_CHAR + (LEFT_RIGHT_CHAR * (size * 2)) + UP_LEFT_CHAR)
        
        return rows
    
    def get_filled_square(size):
        """Create a filled square using box-drawing characters"""
        assert size >= 0
        
        rows = []
        # Make the top row of the square
        rows.append(DOWN_RIGHT_CHAR + (DOWN_LEFT_RIGHT_CHAR * (size * 2)) + DOWN_LEFT_CHAR)
        
        # Make the middle segment of the square
        for i in range(size):
            rows.append(UP_DOWN_RIGHT_CHAR + (CROSS_CHAR * (size * 2)) + UP_DOWN_LEFT_CHAR)
        
        # Make the bottom row of the square
        rows.append(UP_RIGHT_CHAR + (UP_LEFT_RIGHT_CHAR * (size * 2)) + UP_LEFT_CHAR)
        
        return rows
    
    next_rows = []
    row_count = 0
    
    while True:
        if width is None:
            _width = shutil.get_terminal_size()[0]
        else:
            _width = width
        if sys.platform == 'win32':
            _width -= 1  # Windows terminals insert a newline if something is printed in the last column

        # Generate squares for this iteration
        for j in range(squares_per_row):
            size = random.randint(min_square_size, max_square_size)
            
            if random.random() < chance_of_filled:
                square = get_filled_square(size)
            else:
                square = get_outline_square(size)
            
            x_start = random.randint(0, max(0, _width - 1 - (size * 2 + 2)))
            
            # Make sure there are enough rows in next_rows
            if len(next_rows) < size + 2:
                for k in range(((size + 2) - len(next_rows))):
                    next_rows.append([random.choice(empty_chars) for i in range(_width)])
            
            # Add the square to next_rows
            for y, row in enumerate(square):
                for x, char in enumerate(row):
                    if x + x_start < _width:
                        next_rows[y][x + x_start] = char
        
        # Print the row and then remove it
        if next_rows:
            print(''.join(next_rows[0]))
            del next_rows[0]
            time.sleep(delay)
            
            row_count += 1
            if max_rows and row_count >= max_rows:
                return


def in_and_out(delay=0.04, width=None, empty_chars='. ', traveler_chars='@Oo',
               stay_in_min=6, stay_in_max=20, max_capacity=22, capacity_inc_every=10,
               capacity_dec_every=3, new_traveler_prob=0.3, max_rows=None):
    """
    Travelers moving in and out from screen edges with dynamic capacity
    """    
    capacity = 1
    step = 0
    increasing_capacity = True
    travelers = []  # [position, destination, duration, direction, char]
    row_count = 0
    
    while True:
        if width is None:
            _width = shutil.get_terminal_size()[0]
        else:
            _width = width
        if sys.platform == 'win32':
            _width -= 1  # Windows terminals insert a newline if something is printed in the last column

        step += 1  # next step
        
        # Manage capacity changes
        if increasing_capacity and step == capacity_inc_every:
            step = 0
            capacity += 1
            if capacity == max_capacity:
                increasing_capacity = False
        elif not increasing_capacity and step >= capacity_dec_every and len(travelers) < capacity:
            step = 0
            capacity -= 1
            if capacity == 0:
                increasing_capacity = True
        
        # Add new travelers
        if len(travelers) < capacity and random.random() <= new_traveler_prob:
            if random.randint(0, 1) == 0:
                # Add to left side
                travelers.append([
                    0, 
                    random.randint(5, _width - 1 - 5), 
                    random.randint(stay_in_min, stay_in_max), 
                    'L', 
                    random.choice(traveler_chars)
                ])
            else:
                # Add to right side
                travelers.append([
                    _width - 1, 
                    random.randint(5, _width - 1 - 5), 
                    random.randint(stay_in_min, stay_in_max), 
                    'R', 
                    random.choice(traveler_chars)
                ])
        
        # Print all travelers
        line = [random.choice(empty_chars) for i in range(_width)]
        for traveler in travelers:
            line[traveler[0]] = traveler[4]
        print(''.join(line))
        
        # Move all travelers
        to_delete = []
        for i, traveler in enumerate(travelers):
            if ((traveler[0] == 0 and traveler[3] == 'L' and traveler[2] == 0) or 
                (traveler[0] == _width - 1 and traveler[3] == 'R' and traveler[2] == 0)):
                # traveler is just about to move out of space
                to_delete.append(i)
            elif traveler[0] != traveler[1] and traveler[2] != 0:
                # Move traveler in
                if traveler[3] == 'L':
                    traveler[0] += 1  # move in, from left
                elif traveler[3] == 'R':
                    traveler[0] -= 1  # move in, from right
            elif traveler[0] != traveler[1] and traveler[2] == 0:
                # Move traveler out
                if traveler[3] == 'L':
                    traveler[0] -= 1  # move out, from left
                elif traveler[3] == 'R':
                    traveler[0] += 1  # move out, from right
            else:
                # traveler is in and staying, decrement stay duration
                traveler[2] -= 1
                if traveler[2] == 0:
                    # Start to move out
                    if traveler[3] == 'L':
                        traveler[0] -= 1
                    elif traveler[3] == 'R':
                        traveler[0] += 1
        
        # Delete exited travelers
        for i in reversed(to_delete):
            del travelers[i]
        
        time.sleep(delay)
        
        row_count += 1
        if max_rows and row_count >= max_rows:
            return


def matrix(delay=0.1, width=None, min_stream_length=6, max_stream_length=14,
           stream_chars=['0', '1'], density=0.02, max_rows=None):
    """
    Matrix-style digital rain with falling streams of characters
    """
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
    
    # For each column, when the counter is 0, no stream is shown.
    # Otherwise, it acts as a counter for how many times a character
    # should be displayed in that column.
    columns = [0] * _width
    row_count = 0
    
    while True:
        # Set up the counter for each column
        for i in range(_width):
            if columns[i] == 0:
                if random.random() <= density:
                    # Restart a stream on this column
                    columns[i] = random.randint(min_stream_length, max_stream_length)
            
            # Display an empty space or a stream character
            if columns[i] > 0:
                print(random.choice(stream_chars), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        
        print()  # Print a newline at the end of the row of columns
        time.sleep(delay)
        
        row_count += 1
        if max_rows and row_count >= max_rows:
            return


def sine_message(message='Hello!', delay=0.1, step_increase=0.2, width=None, max_rows=None):
    """
    Message that oscillates horizontally using sine wave motion
    """
    step = 0.0
    row_count = 0
    
    while True:  # Main program loop
        # Update width in case terminal was resized
        if width is None:
            _width = shutil.get_terminal_size()[0]
        else:
            _width = width
        if sys.platform == 'win32':
            _width -= 1  # Windows terminals insert a newline if something is printed in the last column

        # Calculate sine wave position
        multiplier = (_width - len(message)) / 2
        sin_of_step = math.sin(step)
        padding = ' ' * int((sin_of_step + 1) * multiplier)
        
        print(padding + message)
        time.sleep(delay)
        step += step_increase
        
        row_count += 1
        if max_rows and row_count >= max_rows:
            return


def proton_stream(delay=0.01, width=None, num_streams=5, move_chance=0.75,
                 empty_char=' ', stream_chars='oO@', max_rows=None):
    """
    Multiple streams that move while maintaining distance constraints
    """
    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column

    max_distance = num_streams * 4  # How many spaces streams must be within each other
    
    # Initialize streams at center of screen
    streams = [_width // 2] * num_streams
    row_count = 0
    
    while True:
        # Update width in case terminal was resized
        _width = (width or shutil.get_terminal_size()[0]) - 1
        
        columns = [empty_char] * _width
        
        # Move streams randomly while maintaining distance constraints
        for i, stream in enumerate(streams):
            if random.random() < move_chance:
                # Try to move stream
                if random.random() < 0.5:
                    # Try to move left
                    new_pos = stream - 1
                    if (new_pos >= 0 and 
                        all([abs(new_pos - other) <= max_distance for other in streams])):
                        streams[i] = new_pos
                else:
                    # Try to move right
                    new_pos = stream + 1
                    if (new_pos < _width and 
                        all([abs(new_pos - other) <= max_distance for other in streams])):
                        streams[i] = new_pos
        
        # Place stream characters in columns
        for i, stream in enumerate(streams):
            if 0 <= stream < _width:
                columns[stream] = stream_chars[i % len(stream_chars)]
        
        print(''.join(columns))
        time.sleep(delay)
        
        row_count += 1
        if max_rows and row_count >= max_rows:
            return


def striped_triangles(delay=0.1, width=None, max_rows=None):
    """Animated triangular patterns with changing density and alternating orientations."""        
    density = 0
    changeAmt = 4
    row_count = 0
    
    while True:
        if width is None:
            _width = shutil.get_terminal_size()[0]
        else:
            _width = width
        if sys.platform == 'win32':
            _width -= 1  # Windows terminals insert a newline if something is printed in the last column

    # The width of a pair of triangles is 7 characters:
    #   /\ \ \
        #  / /\ \
        # / / /\
        # 123456
        numTrianglePairs = (_width - 2) // 6

        # Increase/decrease the density of triangles, until you
        # reach 0 or 100, then reverse the direction of density change:
        density += changeAmt
        if density <= 0 or density >= 100:
            changeAmt *= -1

        # Draw a row that starts with an upright triangle on the left side.
        row1 = ['  ']
        row2 = [' ']
        row3 = []
        for i in range(numTrianglePairs):
            if random.randint(0, 99) < density:
                if random.randint(0, 1):
                    row1.append('\\')
                    row2.append('\\ \\')
                    row3.append('\\ \\ \\')
                else:
                    row1.append('/')
                    row2.append('/ /')
                    row3.append('/ / /')
            else:
                row1.append(' ')
                row2.append('   ')
                row3.append('     ')

            if random.randint(0, 99) < density:
                if random.randint(0, 1):
                    row1.append('\\ \\ \\')
                    row2.append('\\ \\')
                    row3.append('\\')
                else:
                    row1.append('/ / /')
                    row2.append('/ /')
                    row3.append('/')
            else:
                row1.append('     ')
                row2.append('   ')
                row3.append(' ')
                
        print(''.join(row1))
        sys.stdout.flush()
        time.sleep(delay)
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
            
        print(''.join(row2))
        sys.stdout.flush()
        time.sleep(delay)
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
            
        print(''.join(row3))
        sys.stdout.flush()
        time.sleep(delay)
        row_count += 1
        if max_rows and row_count >= max_rows:
            return


        # Draw a row that starts with an upside down triangle on the left side.
        row1 = []
        row2 = [' ']
        row3 = ['  ']
        for i in range(numTrianglePairs):
            if random.randint(0, 99) < density:
                if random.randint(0, 1):
                    row1.append('\\ \\ \\')
                    row2.append('\\ \\')
                    row3.append('\\')
                else:
                    row1.append('/ / /')
                    row2.append('/ /')
                    row3.append('/')
            else:
                row1.append('     ')
                row2.append('   ')
                row3.append(' ')

            if random.randint(0, 99) < density:
                if random.randint(0, 1):
                    row1.append('\\')
                    row2.append('\\ \\')
                    row3.append('\\ \\ \\')
                else:
                    row1.append('/')
                    row2.append('/ /')
                    row3.append('/ / /')
            else:
                row1.append(' ')
                row2.append('   ')
                row3.append('     ')

        print(''.join(row1))
        sys.stdout.flush()
        time.sleep(delay)
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
            
        print(''.join(row2))
        sys.stdout.flush()
        time.sleep(delay)
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
            
        print(''.join(row3))
        sys.stdout.flush()
        time.sleep(delay)
        row_count += 1
        if max_rows and row_count >= max_rows:
            return



def math_func(delay=0.05, width=None, max_rows=None):
    """Mathematical visualization using Unicode block characters."""
    # Constants for the block characters used to represent pixels:
    TOP_BLOCK    = chr(9600)  # ▀
    BOTTOM_BLOCK = chr(9604)  # ▄
    FULL_BLOCK   = chr(9608)  # █
    
    FUNC = eval('lambda x, y: (x ^ y) % 5')
    
    
    y = 0
    row_count = 0
    
    while True:
        if width is None:
            _width = shutil.get_terminal_size()[0]
        else:
            _width = width
        if sys.platform == 'win32':
            _width -= 1  # Windows terminals insert a newline if something is printed in the last column

        for x in range(_width):
            topBit = FUNC(x, y)
            bottomBit = FUNC(x, y + 1)

            # Patterns often look better if we use True for the black pixels:
            topBit = not topBit
            bottomBit = not bottomBit

            if topBit and bottomBit:
                print(FULL_BLOCK, end='')
            elif topBit and not bottomBit:
                print(TOP_BLOCK, end='')
            elif not topBit and bottomBit:
                print(BOTTOM_BLOCK, end='')
            else:
                print(' ', end='')
        print(flush=True)

        y += 2
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
            
        time.sleep(delay)
                


def cube_wall(delay=0.1, width=None, max_rows=None, density=35):
    """Creates a wall of 3D cubes with random shading patterns."""
    
    row_count = 0
    
    while True:
        if width is None:
            _width = shutil.get_terminal_size()[0]
        else:
            _width = width
        if sys.platform == 'win32':
            _width -= 1  # Windows terminals insert a newline if something is printed in the last column

        segmentWidth = _width // 21

        row1 = []
        row2 = []
        row3 = []
        row4 = []
        row5 = []
        row6 = []

        for i in range(segmentWidth):
            if random.randint(0, 99) < density:
                top1Shading = '/////'
                top1ShadingBottom = '_/_/_'
            else:
                top1Shading = '     '
                top1ShadingBottom = '_____'
                
            if random.randint(0, 99) < density:
                top2Shading = '/////'
                top2ShadingBottom = '_/_/_'
            else:
                top2Shading = '     '
                top2ShadingBottom = '_____'
                
            if random.randint(0, 99) < density:
                bottom1Shading = '\\\\\\\\\\'
                bottom1ShadingBottom = '_\\_\\_'
            else:
                bottom1Shading = '     '
                bottom1ShadingBottom = '_____'
                
            if random.randint(0, 99) < density:
                bottom2Shading = '\\\\\\\\\\'
                bottom2ShadingBottom = '_\\_\\_'
            else:
                bottom2Shading = '     '
                bottom2ShadingBottom = '_____'

            if random.randint(0, 99) < density:
                if random.randint(0, 1):
                    side1Shading = '\\\\'
                else:
                    side1Shading = '//'
            else:
                side1Shading = '  '

            row1.append(f'  /{top1Shading}/\\{bottom2Shading}\\  ')
            row2.append(f' /{top1Shading}/{side1Shading}\\{bottom2Shading}\\ ')
            row3.append(f'/{top1ShadingBottom}/{side1Shading * 2}\\{bottom2ShadingBottom}\\')
            row4.append(f'\\{bottom1Shading}\\{side1Shading * 2}/{top2Shading}/')
            row5.append(f' \\{bottom1Shading}\\{side1Shading}/{top2Shading}/ ')
            row6.append(f'  \\{bottom1ShadingBottom}\\/{top2ShadingBottom}/  ')

        print(''.join(row1))
        sys.stdout.flush()
        time.sleep(delay)
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
            
        print(''.join(row2))
        sys.stdout.flush()
        time.sleep(delay)
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
            
        print(''.join(row3))
        sys.stdout.flush()
        time.sleep(delay)
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
            
        print(''.join(row4))
        sys.stdout.flush()
        time.sleep(delay)
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
            
        print(''.join(row5))
        sys.stdout.flush()
        time.sleep(delay)
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
            
        print(''.join(row6))
        sys.stdout.flush()
        time.sleep(delay)
        row_count += 1
        if max_rows and row_count >= max_rows:
            return



def bundfc(delay=0.08, width=None, max_rows=None, change_div=40, mutation_rate=0.0):
    """Scroll art inspired by the architecture of the Bund Financial Center in Shanghai."""
    
    CHARS = '.:+oO@#@Oo+:.'
    BACKGROUND = ' '
    
    def get_random_wave(z=0):
        wave = {}
        
        wave['side'] = 'left'  # random.choice(['left', 'left'])
        if z >= len(CHARS):
            wave['side'] = 'right'
            z -= len(CHARS)
        
        wave['speed'] = min(random.random() + 0.3, 1.0) * 10
        wave['amplitude'] = random.randint(_width // 6, _width // 3) / ((z / 2) + 1)
        wave['char'] = CHARS[z]  # random.choice(CHARS)
        
        return wave

    if width is None:
        _width = shutil.get_terminal_size()[0]
    else:
        _width = width
    if sys.platform == 'win32':
        _width -= 1  # Windows terminals insert a newline if something is printed in the last column
    
    waves = [get_random_wave(x) for x in range(len(CHARS) * 2)]
    step = 42  # Don't start at 0, just to avoid all the waves starting at 0 as well.
    row_count = 0
    
    while True:
        row = [BACKGROUND for x in range(_width)]
        
        for wave in waves:
            if random.random() < mutation_rate:
                wave['amplitude'] += random.randint(-1, 1)
            
            wave_length = int((math.sin((step / change_div) * wave['speed']) + 1) * wave['amplitude'])
            if wave['side'] == 'left':
                for i in range(0, min(wave_length, _width)):
                    row[i] = wave['char']
            elif wave['side'] == 'right':
                for i in range(max(0, _width - 1 - wave_length), _width):
                    if i < _width:
                        row[i] = wave['char']
        
        print(''.join(row))
        row_count += 1
        if max_rows and row_count >= max_rows:
            return
            
        time.sleep(delay)
        step += 1
        
