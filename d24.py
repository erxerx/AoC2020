import operator

with open('d24.in1', 'r') as f:
    content = f.read()
routes = content.split('\n')
# idea from https://stackoverflow.com/questions/2459402/hexagonal-grid-coordinates-to-pixel-coordinates
h_move = [(0, 0, 0), (0, -1, 1), (1, -1, 0), (1, 0, -1), (0, 1, -1), (-1, 1, 0), (-1, 0, 1)]
h_grid = {}
blacks = 0
for route in routes:
    r, g, b = 0, 0, 0  # reset to middle tile
    for move in route:
        r, g, b = tuple(map(sum, zip((r, g, b), h_move[int(move)])))
    if (r, g, b) in h_grid:
        h_grid[(r, g, b)] = 1 - h_grid[(r, g, b)]
    else:
        h_grid[(r, g, b)] = 1
    blacks += (2 * h_grid[(r, g, b)] - 1)  # to convert 0 or 1 to -1 or +1
# print(blacks)
# part1: 282
n_state = set()
for i in h_grid:
    if i: n_state.add(i)
for day in range(5):
    h_state = n_state
    n_state = set()
    blacks = 0
    print(len(h_state), h_state)
    for current in h_state:
        for move in h_move:
            nearby = 0
            look = tuple(map(operator.add, current, move))
            if look in n_state: continue
            for tile in h_state:
                if tuple(map(operator.sub, tile, look)) in h_move[1:]: nearby += 1
            if ((look in h_state) and (0 < nearby) and (nearby < 3)) or \
                    ((look not in h_state) and nearby == 2):
                n_state.add(look)
                blacks += 1
