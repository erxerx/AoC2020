from time import time
import operator
start = time()
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
        r, g, b = tuple(map(sum, zip((r, g, b), h_move[int(move)])))
    if (r, g, b) in h_grid:
        h_grid.pop((r, g, b))
        blacks -= 1
    else:
        h_grid[(r, g, b)] = 1
        blacks += 1
# print(blacks)
# part1: 282
for day in range(100):
    n_grid = {}
    blacks = 0
    for current in h_grid:
        for move in h_move:
            look = tuple(map(operator.add, current, move))
            if look in n_grid: continue
            nearby = 0
            for tile in h_grid:
                if tuple(map(operator.sub, look, tile)) in h_move[1:]: nearby += 1
            if ((look in h_grid and h_grid[look]) and (0 < nearby) and (nearby < 3)) or \
                    ((look not in h_grid or not h_grid[look]) and nearby == 2):
                n_grid[look] = 1
                blacks += 1
            else:
                n_grid[look] = 0
    h_grid = {}
    for i in n_grid:
        if n_grid[i]: h_grid[i] = 1
    print(day+1, len(h_grid))
print(f"Time : {time() - start} seconds")
# part2: 100 3445
# Time : 857.372636795044 seconds (ver1)
# Time : 372.2061810493469 seconds (ver2)
