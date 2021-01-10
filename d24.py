with open('d24.in', 'r') as f:
    content = f.read()
routes = content.split('\n')
# idea from https://stackoverflow.com/questions/2459402/hexagonal-grid-coordinates-to-pixel-coordinates
h_move = [(0, 0, 0), (0, -1, 1), (1, -1, 0), (1, 0, -1), (0, 1, -1), (-1, 1, 0), (-1, 0, 1)]
h_grid = {}
blacks = 0
for route in routes:
    r, g, b = 0, 0, 0  # reset to middle tile
    for move in route:
        r += h_move[int(move)][0]
        g += h_move[int(move)][1]
        b += h_move[int(move)][2]
    if (r, g, b) in h_grid: h_grid[(r, g, b)] = 1 - h_grid[(r, g, b)]
    else: h_grid[(r, g, b)] = 1
    blacks += (2 * h_grid[(r, g, b)] - 1)  # to convert 0 or 1 to -1 or +1
    print(route, r, g, b, blacks)
    # ...
    # 363613615161 -2 -3 5 282
