# from itertools import product
with open('d24.in', 'r') as f:
    content = f.read()
routes = content.split('\n')
h_grid = {}
# idea from https://stackoverflow.com/questions/2459402/hexagonal-grid-coordinates-to-pixel-coordinates
h_move = [(0, 0, 0), (0, -1, 1), (1, -1, 0), (1, 0, -1), (0, 1, -1), (-1, 1, 0), (-1, 0, 1)]
blacks = 0
for route in routes:
    r, g, b = 0, 0, 0  # reset to middle tile
    for move in route:
        r, g, b = tuple(map(sum, zip((r, g, b), h_move[int(move)])))
    if (r, g, b) in h_grid: h_grid[(r, g, b)] = 1 - h_grid[(r, g, b)]
    else: h_grid[(r, g, b)] = 1
    blacks += (2 * h_grid[(r, g, b)] - 1)  # to convert 0 or 1 to -1 or +1
    print(route, r, g, b, blacks)
    # ...
    # 363613615161 -2 -3 5 282
