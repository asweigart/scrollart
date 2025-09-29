# Scroll Art

Scroll art is moving ASCII art produced by stdout text printed from a loop, "animated" as the text scrolls up the terminal.

"Scroll art" was coined by Al Sweigart. The simplicity of scroll art means that it's useful as a programming project for beginners. Scroll art can be made in any programming language. This package contains a large collection of scroll art, as well as functions for creating your own scroll art. You can see examples of scroll art at https://scrollart.com

## Quickstart

Install the `scrollart` package by running `pip install scrollart` and see which demos are available by running `python -m scrollart --help`.

For example, you can run `python -m scrollart starfield` or `python -m scrollart ducklings`.

Here's the output of the help text:

```
ScrollArt - Various animated scroll art displays

positional arguments:
  {starfield,stripeout,twists,tsuro,pipe_swap,skybursts,forth_and_back,moire,skulls_and_hearts,pac_wall,inchworm,connected_pipes,diagonal_sweep,earthworm_tunnels,towers_and_towers,any_size_diagonal_maze,thorns,triangle_hall,vertical_struts,hex_portals,toggler1,toggler2,tri_grid_scaffold,orbital_travels,snail_trail,password_cracker,dna,spike,zigzag,diamond_sky,ducklings,full_of_squares,in_and_out,matrix,sine_message,proton_stream,striped_triangles,math_func,cube_wall,bundfc}
                        The scroll art command to run

options:
  -h, --help            show this help message and exit

Available commands:
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
  bundfc             - Architectural waves inspired by Shanghai's Bund Financial Center
  ```