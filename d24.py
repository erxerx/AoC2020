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
# rl, gl, bl = 0, 0, 0  # reset to middle tile
# rh, gh, bh = 0, 0, 0  # reset to middle tile
h_state = set()
for i in h_grid:  # get only black tiles and get extremes
    if i: h_state.add(i)
#         if rl > i[0]: rl = i[0]
#         if gl > i[1]: gl = i[1]
#         if bl > i[2]: bl = i[2]
#         if rh < i[0]: rh = i[0]
#         if gh < i[1]: gh = i[1]
#         if bh < i[2]: bh = i[2]
# # print(h_state)
n_state = h_state
for day in range(5):
    h_state = n_state
    print(len(h_state), h_state)
    n_state = set()
    blacks = 0
    for current in h_state:
        for move in h_move[1:]:
            nearby = 0
            lookat = tuple(map(operator.add, current, move))
            if lookat in n_state: break
            for tile in h_state:
                if tuple(map(operator.sub, tile, lookat)) in h_move[1:]: nearby += 1
            # print((rr,gg,bb), nearby)
            if ((lookat in h_state) and (0 < nearby) and (nearby < 3)) or \
                    ((not lookat in h_state) and nearby == 2):
                n_state.add(lookat)
                blacks += 1
